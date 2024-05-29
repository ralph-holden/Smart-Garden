# # # IMPORTS # # #

import time
from microcontroller import cpu
import board
import busio
from digitalio import DigitalInOut
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from adafruit_io.adafruit_io import IO_MQTT

# # # OUR IMPORTS # # #

import digitalio
import analogio
import pwmio
import math
import adafruit_dht
import simpleio
#import servo
from tunes import * # theme tunes

# # # WiFi # # #

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# Raspberry Pi RP2040
esp32_cs = DigitalInOut(board.CS1)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)

spi = busio.SPI(board.SCK1, board.MOSI1, board.MISO1)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, secrets)

# Configure the RP2040 Pico LED Pin as an output
led_pin = DigitalInOut(board.LED)
led_pin.switch_to_output()


# Define callback functions which will be called when certain events happen.
# pylint: disable=unused-argument
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    print("Connected to Adafruit IO! ")


def subscribe(client, userdata, topic, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print("Subscribed to {0} with QOS level {1}".format(topic, granted_qos))


# pylint: disable=unused-argument
def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print("Disconnected from Adafruit IO!")


def on_led_msg(client, topic, message):
    # Method called whenever user/feeds/led has a new value
    print("New message on topic {0}: {1} ".format(topic, message))
    if message == "ON":
        led_pin.value = True
    elif message == "OFF":
        led_pin.value = False
    else:
        print("Unexpected message on LED feed.")


# Connect to WiFi
print("Connecting to WiFi...")
wifi.connect()
print("Connected!")

# Initialize MQTT interface with the esp interface
MQTT.set_socket(socket, esp)

# Initialize a new MQTT Client object
mqtt_client = MQTT.MQTT(
    broker="io.adafruit.com",
    port=1883,
    username=secrets["aio_username"],
    password=secrets["aio_key"],
)

# Initialize an Adafruit IO MQTT Client
io = IO_MQTT(mqtt_client)

# Connect the callback methods defined above to Adafruit IO
io.on_connect = connected
io.on_disconnect = disconnected
io.on_subscribe = subscribe

# Set up a callback for the led feed
io.add_feed_callback("led", on_led_msg)

# Connect to Adafruit IO
print("Connecting to Adafruit IO...")
io.connect()

# Subscribe to all messages on the led feed
io.subscribe("led")


# # # OUR DEVICES # # #

# pump
pump = digitalio.DigitalInOut(board.D10)
pump.direction = digitalio.Direction.OUTPUT

# moisture sensor
Moisture = analogio.AnalogIn(board.A1)

# humidity sensor
Humidity = adafruit_dht.DHT11(board.A5)

# override switch
# put code here! if button pressed, turns pump OFF in 'while True' loop
our_switch = digitalio.DigitalInOut(board.D7)
our_switch.direction = digitalio.Direction.OUTPUT

# moisture sensor threshold value - choose!!
threshold = 800

def get_voltage(pin):
    return pin.value

# Blue LED for pump ON
# turns on when moisture level is BELOW threshold
led_b = pwmio.PWMOut(board.D3, variable_frequency=True)
# led_b.direction = digitalio.Direction.OUTPUT

# Green LED for pump OFF
# turns on when moisture level ABOVE threshold
led_g = digitalio.DigitalInOut(board.D2)
led_g.direction = digitalio.Direction.OUTPUT

# motor
#pmw_motor = pwmio.PWMOut(board.A4, duty_cycle=2**15, frequency=50)

#motor = servo.Servo(pmw_motor)

#while True:
#    for angle in range(0, 180, 5):
#        motor.angle = angle
#        time.sleep(0.05)
#    for angle in range(180, 0, 5):
#        motor.angle = angle
#        time.sleep(0.05)


# # # ACTION LOOP # # #

prv_refresh_time = 0.0

while True:
    # # # LIVE BROADCASTING OF DATA # # #
    # Poll for incoming messages
    try:
        io.loop()
    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        wifi.reset()
        wifi.connect()
        io.reconnect()
        continue
    # Send a new temperature reading to IO every 30 seconds
    if (time.monotonic() - prv_refresh_time) > 30:
        # take the cpu's temperature
        cpu_temp = cpu.temperature
        # truncate to two decimal points
        cpu_temp = str(cpu_temp)[:5]
        print("CPU temperature is %s degrees C" % cpu_temp)
        # publish it to io
        print("Publishing %s to temperature feed..." % cpu_temp)
        io.publish("temperature", cpu_temp)
        print("CPU temperature Published!")

        # take the soil moisture
        soil_moisture = Moisture.value
        # truncate to two decimal points
        soil_moisture = str(soil_moisture)[:5]
        print("Soil moisture is", soil_moisture)
        # publish it to io
        print("Publishing soil moisture")
        io.publish("moisture", soil_moisture)
        print("Soil moisture published!")

        # take the humidity and room temperature
        reading_temperature = Humidity.temperature
        reading_humidity = Humidity.humidity
        # truncate to two decimal points
        reading_temperature = str(reading_temperature)[:5]
        reading_humidity = str(reading_humidity)[:5]
        print("Humidity is", reading_humidity, '%')
        print("Room Temperature is", reading_temperature, 'deg C')
        # publish it to io
        print("Publishing humidity and room temperature")
        io.publish("humidity", reading_humidity)
        io.publish("rtemperature", reading_temperature)
        print("Humidity and room temperature published!")
       
        prv_refresh_time = time.monotonic()

    # # # DEVICE CONTROLS # # #
    # pause switch
    if our_switch.value:
        pump.value = False
        print('PAUSED!')
        for i in range(10):
            led_b.duty_cycle = 65534
            led_g.value = True
            time.sleep(0.5)
            led_b.duty_cycle = 0
            led_g.value = False
            time.sleep(0.5)
        imperial_tune()
           
    # moisture reading for pump
    elif get_voltage(Moisture) <= threshold:
        pump.value = True
        led_b.duty_cycle = int(abs(math.sin(time.monotonic())) * 65535)
        led_g.value = False
    else:
        pump.value = False
        led_b.duty_cycle = 0
        led_g.value = True
    # print(get_voltage(Moisture))

# # # MUSIC 'FILES' FOR BUZZER
import simpleio
import board

#Sound frequencies
Do4=261.6
DoS4=277.2
Re4=293.7
ReS4=311.1
Mi4=329.6
Fa4=349.2
FaS4=370.0
So4=392.0
SoS4=415.3
La4=440.0
LaS4=466.2
Si4=493.9
Do5=523.3
DoS5=554.4
Re5=587.3
ReS5=622.3
Mi5=659.3
Fa5=698.5
FaS5=740.0
So5=784.0
SoS5=830.6
La5=880.0
LaS5=932.3
Si5=987.8

# oo ee oo ah ah
def funny_tune():
    simpleio.tone(board.D5,349.2, duration=0.5) #Mi
    simpleio.tone(board.D5,277.2, duration=0.5) #Do
    simpleio.tone(board.D5,233.1, duration=0.25) #La
    simpleio.tone(board.D5,277.2, duration=0.25) #Do
    simpleio.tone(board.D5,277.2, duration=0.5) #Do
   
    simpleio.tone(board.D5,233.1, duration=0.25) #La
    simpleio.tone(board.D5,277.2, duration=0.25) #Do
    simpleio.tone(board.D5,277.2, duration=0.5) #Do
    simpleio.tone(board.D5,207.7, duration=0.25) #So
    simpleio.tone(board.D5,207.7, duration=0.25) #So
    simpleio.tone(board.D5,233.1, duration=0.25) #La
    simpleio.tone(board.D5,207.7, duration=0.25) #So
   
    simpleio.tone(board.D5,349.2, duration=0.5) #Mi
    simpleio.tone(board.D5,277.2, duration=0.5) #Do
    simpleio.tone(board.D5,233.1, duration=0.25) #La
    simpleio.tone(board.D5,277.2, duration=0.25) #Do
    simpleio.tone(board.D5,277.2, duration=0.25) #Do
    simpleio.tone(board.D5,207.7, duration=0.25) #So
   
    simpleio.tone(board.D5,233.1, duration=0.25) #La
    simpleio.tone(board.D5,233.1, duration=0.25) #La
    simpleio.tone(board.D5,261.6, duration=0.25) #Si
    simpleio.tone(board.D5,261.6, duration=0.25) #Si
    simpleio.tone(board.D5,277.2, duration=1) #Do
   
# imperial march
def imperial_tune():
    simpleio.tone(board.D5,So4, duration=0.6)
    simpleio.tone(board.D5,So4, duration=0.6)
    simpleio.tone(board.D5,So4, duration=0.6)
    simpleio.tone(board.D5,ReS4, duration=0.45)
    simpleio.tone(board.D5,LaS4, duration=0.15)
   
    simpleio.tone(board.D5,So4, duration=0.6)
    simpleio.tone(board.D5,ReS4, duration=0.45)
    simpleio.tone(board.D5,LaS4, duration=0.15)
    simpleio.tone(board.D5,So4, duration=1.2)
   
    simpleio.tone(board.D5,Re5, duration=0.6)
    simpleio.tone(board.D5,Re5, duration=0.6)
    simpleio.tone(board.D5,Re5, duration=0.6)
    simpleio.tone(board.D5,ReS5, duration=0.45)
    simpleio.tone(board.D5,LaS4, duration=0.15)
   
    simpleio.tone(board.D5,FaS4, duration=0.6)
    simpleio.tone(board.D5,ReS4, duration=0.45)
    simpleio.tone(board.D5,LaS4, duration=0.15)
    simpleio.tone(board.D5,So4, duration=1.2)
   
    simpleio.tone(board.D5,So5, duration=0.6)
    simpleio.tone(board.D5,So4, duration=0.525)
    simpleio.tone(board.D5,So4, duration=0.075)
    simpleio.tone(board.D5,So5, duration=0.6)
    simpleio.tone(board.D5,FaS5, duration=0.525)
    simpleio.tone(board.D5,Fa5, duration=0.075)
   
    simpleio.tone(board.D5,Mi5, duration=0.2)
    simpleio.tone(board.D5,ReS5, duration=0.2)
    simpleio.tone(board.D5,Mi5, duration=0.725)
    simpleio.tone(board.D5,So4, duration=0.075)
    simpleio.tone(board.D5,Do5, duration=0.6)
    simpleio.tone(board.D5,Si4, duration=0.525)
    simpleio.tone(board.D5,LaS4, duration=0.075)
   
    simpleio.tone(board.D5,La4, duration=0.2)
    simpleio.tone(board.D5,SoS4, duration=0.2)
    simpleio.tone(board.D5,La4, duration=0.725)
    simpleio.tone(board.D5,ReS4, duration=0.075)
    simpleio.tone(board.D5,So4, duration=0.6)
    simpleio.tone(board.D5,ReS4, duration=0.525)
    simpleio.tone(board.D5,So4, duration=0.075)
   
    simpleio.tone(board.D5,LaS4, duration=0.6)
    simpleio.tone(board.D5,So4, duration=0.525)
    simpleio.tone(board.D5,LaS4, duration=0.075)
    simpleio.tone(board.D5,Re5, duration=1.2)
   
    simpleio.tone(board.D5,So5, duration=0.6)
    simpleio.tone(board.D5,So4, duration=0.525)
    simpleio.tone(board.D5,So4, duration=0.075)
    simpleio.tone(board.D5,So5, duration=0.6)
    simpleio.tone(board.D5,FaS5, duration=0.525)
    simpleio.tone(board.D5,Fa5, duration=0.075)
   
    simpleio.tone(board.D5,Mi5, duration=0.2)
    simpleio.tone(board.D5,ReS5, duration=0.2)
    simpleio.tone(board.D5,Mi5, duration=0.725)
    simpleio.tone(board.D5,So4, duration=0.075)
    simpleio.tone(board.D5,Do5, duration=0.6)
    simpleio.tone(board.D5,Si4, duration=0.525)
    simpleio.tone(board.D5,LaS4, duration=0.075)
   
    simpleio.tone(board.D5,La4, duration=0.2)
    simpleio.tone(board.D5,SoS4, duration=0.2)
    simpleio.tone(board.D5,La4, duration=0.725)
    simpleio.tone(board.D5,ReS4, duration=0.075)
    simpleio.tone(board.D5,So4, duration=0.6)
    simpleio.tone(board.D5,ReS4, duration=0.525)
    simpleio.tone(board.D5,LaS4, duration=0.075)
   
    simpleio.tone(board.D5,So4, duration=0.6)
    simpleio.tone(board.D5,ReS4, duration=0.525)
    simpleio.tone(board.D5,LaS4, duration=0.075)
    simpleio.tone(board.D5,So4, duration=1.2)
   
# Genshin opening
def genshin_tune():
    simpleio.tone(board.D5,So4, duration=0.74) #So
    simpleio.tone(board.D5,Do5, duration=1.48) #Do

    simpleio.tone(board.D5,Re5, duration=0.37) #Re
    simpleio.tone(board.D5,Mi5, duration=0.37) #Mi
    simpleio.tone(board.D5,FaS5, duration=1.48) #Fa Sharp
   
    simpleio.tone(board.D5,So5, duration=0.185) #So
    simpleio.tone(board.D5,FaS5, duration=0.185) #Fa Sharp
    simpleio.tone(board.D5,Mi5, duration=0.37) #Mi
    simpleio.tone(board.D5,Re5, duration=0.37) #Re
    simpleio.tone(board.D5,Mi5, duration=1.48) #Mi
   
    simpleio.tone(board.D5,Re5, duration=0.37) #Re
    simpleio.tone(board.D5,Do5, duration=0.37) #Do
    simpleio.tone(board.D5,Re5, duration=0.74) #Re
    simpleio.tone(board.D5,La4, duration=1.48) #La
   
    simpleio.tone(board.D5,Do5, duration=1.48) #Do
    simpleio.tone(board.D5,Do5, duration=0.37) #Do
    simpleio.tone(board.D5,Re5, duration=0.37) #Re
    simpleio.tone(board.D5,Si4, duration=0.74) #Si
    simpleio.tone(board.D5,La4, duration=0.74) #La
    simpleio.tone(board.D5,So4, duration=0.74) #So
    simpleio.tone(board.D5,La4, duration=0.74) #La
    simpleio.tone(board.D5,Mi5, duration=2.96) #Si

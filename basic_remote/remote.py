# z: avancer
# q: gauche
# s: reculer
# d: droite
# e/r : led 1 ou 0
# a : stop
# c : exit

import spytank
import time

print("  z: avancer\nq: gauche\ns: reculer\nd: droite\ne/r : led \na : stop\nc : exit\n")
print(" entre une lettre pour piloter le robot comme dans la  description")
lettre = input(">>")


vitesse= 200
if lettre == "z" :
    spytank.avance(vitesse)
elif lettre == "q" :
    spytank.gauche(vitesse)
elif lettre == "s" :
    spytank.recule(vitesse)
elif lettre == "d" :
    spytank.droite(150)
elif lettre == "e/r" :
    spytank.led(0,1)       
    spytank.led(1,1)  
    spytank.led(2,1)  
    spytank.led(3 ,1)       
elif lettre == "a" :
    spytank.stop()
elif lettre == "c" :
    pass
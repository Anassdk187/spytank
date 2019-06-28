import network
import click


ADDRESS ="10.0.0.188"
PORT=1111

print("z : avancer\nq : gauche\ns : reculer\nd : droite\ne/r : led\na : stop\nc : exit")
print("entre une lettre pour piloter le robot comme dans la description")


while True:
    
    socket = network.newClientSocket()
    socket.connect((ADDRESS,PORT))


    lettre = click.getchar()
    socket.send(lettre.encode())

    reponse = socket.recv(4096)
    print(reponse)
    
import socket
from TicTacToe import Board, GUI

mi_socket = socket.socket()
mi_socket.connect(('192.168.0.13', 8000))

prueba = GUI()
MESSAGE = prueba.app.mainloop()
mi_socket.send(MESSAGE)
respuesta = mi_socket.recv(1024)

print(respuesta)
mi_socket.close()
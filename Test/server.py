import socket
from _thread import *

server = "127.0.1.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("[STARTED] waiting for connections....")


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1]) 

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])   


pos = [(0,0), (100,100)]

def threaded_client(conn, currPlayer):
    conn.send(str.encode(make_pos(pos[currPlayer])))
    reply = ""
    while True:
            try:
                data = read_pos(conn.recv(2048).decode())
                pos[currPlayer] = data
                
                
                if not data:
                    print("[DISCONNECTED]")
                    break
                else:
                    if currPlayer == 1:
                        reply = pos[0]
                    else:
                        reply = pos[1]
                        
                    print("RECEIVED: ",data)
                    print("SENDING: ", reply)
                    
                    conn.sendall(str.encode(make_pos(reply)))
            except:
                break
            
    print("Lost Connection")
    conn.close()
        
currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("CONNECTED to:", addr)
    
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
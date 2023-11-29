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

def threaded_client(conn):
    conn.send(str.encode("CONNECTED"))
    reply = ""
    while True:
            try:
                data = conn.recv(2048)
                reply = data.decode("utf-8")
                
                if not data:
                    print("[DISCONNECTED]")
                    break
                else:
                    print("RECEIVED: ",reply)
                    print("SENDING: ", reply)
                    
                    conn.sendall(str.encode(reply))
            except:
                break
            
    print("Lost Connection")
    conn.close()
        

while True:
    conn, addr = s.accept()
    print("CONNECTED to:", addr)
    
    start_new_thread(threaded_client, (conn,))
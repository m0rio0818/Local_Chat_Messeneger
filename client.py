import os
import socket
import sys

class Client:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server_address = "./socket_file"
    
    def start(self):
        self.connect()
        self.sendMessage()
    
    def connect(self):
        try:
            self.sock.connect(self.server_address)
        except socket.error as e:
            print("Error ", e)
            sys.exit(1)
              
    def sendMessage(self):
        message = input("input data which you want to send to the server: ")
        bMessage = bytes(message, "utf-8")
        self.sock.sendall(bMessage)
        self.sock.settimeout(2)
        
        try:
            while True:
                data = self.sock.recv(4096).decode()
                if data:
                    print("Server response : ", data)
                else:
                    break
        except TimeoutError as e:
            print(e, "socket timeout, ending listening for server messages")

        self.sock.close()        
        
    
        
        
def main():
    server = Client()
    server.start()
        
if __name__ == "__main__":
    main()
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
        message = input("input data you want to send to the server. ")
        bMessage = bytes(message, "utf-8")
        print(bMessage)
        
        
    
        
        
def main():
    server = Client()
    server.start()
        
if __name__ == "main":
    main()
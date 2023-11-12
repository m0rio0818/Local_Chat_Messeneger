import socket
import os
from faker import Faker


class Server:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server_address = "./socket_file"
        
    def start(self):
        try:
            os.unlink(self.server_address)
        except FileNotFoundError:
            pass
        print("Starting up on {}".format(self.server_address))
        self.bind()
        self.accept()
        
    def bind(self):
        self.sock.bind(self.server_address)
        self.sock.listen(1)
    
    def accept(self):
        # 受信を続ける。
        while True:
            connection, client_address = self.sock.accept()
            print("Connection from", client_address)
            self.recive(connection, client_address)
    
    def recive(self, connection, client_address):
        while True:
            data = connection.recv(32)
            data_str = data.decode("utf-8")
            print("Recived Data: ", data_str)
            self.send(connection, client_address, data)
    
    def send(self, connection, address ,data):
        if data:
            response = "Processing: " + data
            connection.sendall(data.encode(),response)
        else:
            print("No data from", address)
        
def main():
    server = Server()
    server.start()
        
if __name__ == "main":
    main()
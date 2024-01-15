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
        self.connect()
        self.accept()
        
    def connect(self):
        self.sock.bind(self.server_address)
        self.sock.listen(1)
    
    def accept(self):
        faker = Faker()
        while True:
            connection, client_address = self.sock.accept()
            try:
                print("Connection from", client_address)
                while True:
                    data = connection.recv(32)
                    data_str = data.decode("utf-8")
                    print("Recived ", data_str)
                    
                    if data:
                        responose = b"Hello " + faker.name() + " san, from " + faker.address()
                        connection.sendall(responose)
                    else:
                        print("no data from ", client_address)
                        break
            finally:
                print("Closing current connection")
                connection.close()
                
def main():
    server = Server()
    server.start()
        
if __name__ == "__main__":
    main()
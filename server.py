import socket, const
from util import Util

class Server:
    """Handles hosting a server for the chat program."""

    def __init__(self):
        self.HOST = socket.gethostbyname(socket.gethostname())
        self.nickname = "Server"
        self.isChatActive = True
        print(f"Your IP address is {self.HOST}\nListening for a user...")
        self.run()

    def run(self):
        """Runs the server."""

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((self.HOST, const.PORT))
            server.listen()
            conn, addr = server.accept()
            print(f"Connected to {addr}.")

            with conn:
                while True:
                    Util.alert()
                    data = conn.recv(1024)
                    message = data.decode()
                    if message.startswith("/disconnect"):
                        Util.disconnect(message=message)
                    print(f"{message}")

                    userInput = input(f"{self.nickname}: ")

                    if userInput.startswith("/nickname"):
                        self.nickname = Util.changeNickname(userInput, conn, self.nickname)
                    elif userInput.startswith("/disconnect"):
                        Util.disconnect(isDisconnector=True, socket=conn, nickname=self.nickname)
                    else:
                        conn.sendall(Util.generateMessage(self.nickname, userInput).encode())
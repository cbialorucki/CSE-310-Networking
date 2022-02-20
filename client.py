import socket, const
from util import Util

class Client:
    """Handles connecting to a server for the chat program."""

    def __init__(self):
        self.nickname = "Client"
        self.isChatActive = True
        self.run(self.getIPAddress())
    
    def getIPAddress(self):
        """Prompts the user for an IP address. Returns a valid IP address."""

        print("Which IP address would you like to connect to?")
        ipAddress = input(">> ")
        if Util.IsValidIPAddress(ipAddress):
            return ipAddress
        else:
            print("That's an invalid IP address. Try again.")
            return self.getIPAddress()
    
    def run(self, ipAddress):
        """Connects to a server to chat with.

        :param ipAddress str: The IP address to connect to. 

        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((ipAddress, const.PORT))

            while True:
                Util.alert()
                userInput = input(f"{self.nickname}: ")

                if userInput.startswith("/nickname"):
                    self.nickname = Util.changeNickname(userInput, client, self.nickname)
                elif userInput == "/disconnect":
                    Util.disconnect(isDisconnector=True, socket=client, nickname=self.nickname)
                else:
                    client.sendall(Util.generateMessage(self.nickname, userInput).encode())

                data = client.recv(const.MAX_MESSAGE_SIZE)
                message = data.decode()
                if message.startswith("/disconnect"):
                    Util.disconnect(message=message)
                print(f"{message}")
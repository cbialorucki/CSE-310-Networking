import sys

class Util:
    """A utility class holding methods that are used for both the server and client."""

    @staticmethod
    def disconnect(isDisconnector=False, socket=None, message=None, nickname=None):
        """Disconnects the user from the chat.

        :param isDisconnector bool: Describes if the user is choosing to disconnect from the chat (True), or if the other user disconnected from them (False). (Default value = False)
        :param socket socket: The socket object to send a message to the other user. Only needed if the user is choosing to disconnect. (Default value = None)
        :param message str: The message that was received to disconnect from the user. Only needed if the other user disconnected from them. (Default value = None)
        :param nickname str: The nickname used by the user. Only needed if the user is choosing to disconnect from the chat. (Default value = None)

        """
        if isDisconnector:
            socket.sendall(f"/disconnect{nickname} disconnected from the chat.".encode())
        else:
            print(message.replace("/disconnect", ""))  
        sys.exit()
    
    @staticmethod
    def generateMessage(nickname, message):
        """Disconnects the user from the chat.

        :param message str: The message the user wants to send.
        :param nickname str: The nickname for the user.
        :returns: str: The properly formated string to send across the socket.

        """
        return f"{nickname}: {message}"
    
    @staticmethod
    def changeNickname(userInput, socket, oldNickname):
        """Disconnects the user from the chat.

        :param userInput str: The input from the user to initiate the nickname change.
        :param nickname str: The nickname for the user.
        :param socket socket: The socket object to send a message to the other user.
        :returns: str: The new nickname.

        """
        nickname = userInput.replace("/nickname", "").strip()
        print(f"You changed your nickname to {nickname}.")
        socket.sendall(f"{oldNickname} changed their nickname to {nickname}.".encode())
        return nickname
    
    @staticmethod
    def alert():
        """Plays an alert tone. This is used to tell the user that they can now respond."""
        print('\a', end="")
    
    @staticmethod
    def IsValidIPAddress(input):
        """Disconnects the user from the chat.

        :param input str: The IP address from the user.
        :returns: bool: True if the given input is a valid IP address, False if it is invalid.

        """
        splitItems = input.split('.')
        if len(splitItems) == 4:
            for number in splitItems:
                if not (number.isnumeric() and int(number) >= 0 and int(number) <= 255):
                    return False    
        else:
            return False
        return True
import client, server

def main():
    print("Welcome")
    print("Do you want to connect to a user or wait for a user to connect to you?")
    isInvalidInput = True
    while isInvalidInput:
        print("Type \"connect\" to connect to a user, or \"wait\" to wait for a user to connect to you.")
        userInput = input(">> ").strip().lower()
        if userInput == "connect":
            isInvalidInput = False
            client.Client()
        elif userInput == "wait":
            isInvalidInput = False
            server.Server()
        else:
            print("That input is not valid. Please try again.")

if __name__ == '__main__':
    main()

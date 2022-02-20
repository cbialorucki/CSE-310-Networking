# CSE 310 Networking

# Overview

This is a simple peer-to-peer chat application written in Python. To use this software, one user will need to connect to another. On two separate computers, open the program from main.py. On one computer, which we will call the 'server', type 'wait' and hit enter to set up a chat room. The IP address of that computer will be displayed in the application. On the other computer, which we will call the 'client', type 'connect' to connect to the 'server' computer. After that, it will ask you for the IP address of the computer you want to connect to. Enter the IP address of the 'server' computer, and you will connect to each other. You will then be able to communicate back and forth.

Nicknames can be set by sending "/nickname" followed by the new nickname you would like to use. You can also disconnect from the chat room by sending "/disconnect".

This software was developed to help teach me about how to use network sockets generally. It learned a lot completing this project and I hope to use sockets in the development of off-grid intranet systems.

[Software Demo Video](https://youtu.be/cTAdSscDhq0)

# Network Communication

I believe the architecture of this program more closely resembles a peer to peer network than a client/server model. While one user waits for the other to connect to it, both users share about equal amounts of information. Conversations are conducted directly to each other without another server in between.

This program communicates using a TCP connection. It uses port 65500 by default, but this can easily changed by editing the PORT variable in the const.py file.

Simple UTF-8 stings are sent between clients in this program.

# Development Environment

IDE and Tools
* Visual Studio Code
* Another PC, a virtual PC, or the Windows Subsystem for Linux
* A network connection

Programming Languages and Libraries
* Python
* socket

# Useful Websites

* [Socket Library - Python Official Documentation](https://docs.python.org/3/library/socket.html)
* [Python Socket - Real Python](https://realpython.com/python-sockets/)

# Future Work

* Adding a graphical user interface (GUI) would make this application much more useful to people who do not like using the command line.
* Using multi-threading, it would be possible for either user to send another message without waiting for the other user to send a message. This would help make conversations more natural.
* Adding support for sending files or binary data would also make this program more useful.

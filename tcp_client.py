import socket
import time

host = "localhost"
port = int(input("Port: "))
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((host, port))

    client.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

    response = client.recv(4096)

    print(response.decode())

main()
while True:
    again = input("Want to send again? y/n: ")
    if again == "y":
        main()
    elif again == "n":
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.close()
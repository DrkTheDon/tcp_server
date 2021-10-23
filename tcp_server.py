import socket 
import threading

IP = input("\nIP: ")
PORT = int(input("PORT: "))

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"[*] Listenting to {IP}:{PORT}")

    while True:
        client, address = server.accept()
        print(f"[+] Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_sock):
    with client_sock as sck:
        rq = sck.recv(1024)
        print(f"[+] Recieved: {rq.decode('utf-8')}")
        sck.send(b"Sent ACK")

if __name__ == "__main__":
    main()


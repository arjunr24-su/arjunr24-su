import socket
import threading
from cryptography.fernet import Fernet

# Replace 'YOUR_SERVER_IP' with the actual IP address of your server
SERVER_IP = '127.0.0.1'
SERVER_PORT = 1234

# Generate a key for symmetric encryption (should be the same as the server's key)
symmetric_key = b'YOUR_SYMMETRIC_KEY'
cipher_suite = Fernet(symmetric_key)

def receive_messages(sock):
    try:
        while True:
            message = sock.recv(2048).decode("utf-8")
            print(message)
    except ConnectionResetError:
        print("Connection to the server closed.")

def send_message(sock):
    try:
        while True:
            message = input("You: ")
            encrypted_message = cipher_suite.encrypt(message.encode("utf-8"))
            sock.sendall(encrypted_message)
    except KeyboardInterrupt:
        print("Closing the client.")

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((SERVER_IP, SERVER_PORT))
        print(f"Connected to the server at {SERVER_IP}:{SERVER_PORT}")

        # Send username to the server
        username = input("Enter your username: ")
        client.sendall(username.encode("utf-8"))

        # Start receiving and sending messages in separate threads
        receive_thread = threading.Thread(target=receive_messages, args=(client,))
        send_thread = threading.Thread(target=send_message, args=(client,))

        receive_thread.start()
        send_thread.start()

        receive_thread.join()
        send_thread.join()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    main()

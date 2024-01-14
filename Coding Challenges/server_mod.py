import socket
import threading
import cryptography
from cryptography.fernet import Fernet
import hashlib
import hmac

# Generate a key for symmetric encryption
symmetric_key = Fernet.generate_key()
cipher_suite = Fernet(symmetric_key)

# Function to calculate SHA-512 hash
def calculate_sha512_hash(data):
    sha512 = hashlib.sha512()
    sha512.update(data.encode("utf-8"))
    return sha512.hexdigest()

# Function to generate HMAC
def generate_hmac(key, data):
    return hmac.new(key.encode("utf-8"), data.encode("utf-8"), hashlib.sha256).hexdigest()

HOST = '127.0.0.1'
PORT = 1234
listener_limit = 5
active_clients = []

def listen_for_messages(client, username):
    try:
        while True:
            message = client.recv(2048).decode("utf-8")
            if message != "":
                final_msg = f"{username}~{message}"
                send_message_to_all(final_msg)
            else:
                print(f"The message sent from client {username} is empty")
    except ConnectionResetError:
        print(f"Connection reset by peer for {username}")
        client.close()
        active_clients.remove((username, client))

def send_messages_to_client(client, message):
    client.sendall(message.encode())

def send_message_to_all(message):
    for user in active_clients:
        send_messages_to_client(user[1], message)

# handle client
def client_handler(client):
    # server will listen for client messages that will contain Username
    while True:
        username = client.recv(2048).decode("utf-8").strip()  # Strip to handle usernames with spaces
        if username:
            active_clients.append((username, client))
            prompt_message = f"Server: {username} added to chat"
            send_message_to_all(prompt_message)
            break
        else:
            print("Username empty or contains only spaces")

    threading.Thread(target=listen_for_messages, args=(client, username)).start()

# main function
def main():
    # creating socket class object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # inet for IPv4,
    # try catch block
    try:
        server.bind((HOST, PORT))
        print(f"Running the server on Host {HOST}:{PORT}")
    except:
        print(f"Couldn't bind to host {HOST} and port {PORT}")

    # set server limit
    server.listen(listener_limit)

    # while loop to keep the client connection
    while True:
        # accept connection
        client, address = server.accept()
        print(f"Successfully Connected to {address[0]}:{address[1]}")

        # create thread for each client
        thread = threading.Thread(target=client_handler, args=(client,))
        thread.start()
        thread.join()  # Wait for the thread to finish before accepting the next client

if __name__ == "__main__":
    main()

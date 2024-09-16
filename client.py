import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 8000))

# Print the client's socket name
print(f"Client connected from: {client_socket.getsockname()}")

# Receive a message from the server
server_message = client_socket.recv(1024).decode()
print(f"Received from server: {server_message}")

# Send a message to the server
client_socket.send("Acknowledgement received from the client.".encode())

# Close the connection
client_socket.close()

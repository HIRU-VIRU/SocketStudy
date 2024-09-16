import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind(('localhost', 8000))

# Listen for incoming connections (max 1 connection)
server_socket.listen(1)
print("Server is waiting for a connection...")

# Accept the connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Send a message to the client
conn.send("Hello from the server!".encode())

# Receive a message from the client
data = conn.recv(1024)
print(f"Received from client: {data.decode()}")

# Close the connection
conn.close()
server_socket.close()

import socket
import os
from dotenv import load_dotenv

load_dotenv()

def connect_client(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connected to client:', addr)
    return client_socket

def recv_all(socket_instance, size):
    data = b''
    while True:
        part = socket_instance.recv(size)
        data += part
        if len(part) < size:
            break
    print('Received:', data)
    return data.decode()

def send_all(socket_instance, data, size):
    data = data.encode()
    for i in range(0, len(data), size):
        socket_instance.sendall(data[i:i+size])
    print('Sent:', data)

def handle_tool_client(tool_socket, model_socket, SIZE):
    try:
        # Receive message from tool client
        msg = recv_all(tool_socket, SIZE)
        print("Received message from tool:", msg)
        
        # Forward message to model client
        send_all(model_socket, msg, SIZE)
        
        # Receive response from model client
        response = recv_all(model_socket, SIZE)
        
        # Send response back to tool client
        send_all(tool_socket, response, SIZE)
    except Exception as e:
        print("Error handling tool client:", e)

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_IP')
    PORT = int(os.environ.get('SERVER_PORT'))
    SIZE = 1024
    ADDR = (HOST, PORT)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(ADDR)
        server_socket.listen(4)
        print("Server listening on", ADDR)
        
        print("Waiting for model client to connect...")
        model_socket = connect_client(server_socket)
        
        while True:
            print("Waiting for tool client to connect...")
            tool_socket = connect_client(server_socket)
            try:
                handle_tool_client(tool_socket, model_socket, SIZE)
            except Exception as e:
                print("Error handling tool client:", e)
            tool_socket.close()
            print("Tool client disconnected")
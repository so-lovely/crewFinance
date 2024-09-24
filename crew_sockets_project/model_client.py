import socket
import os
from dotenv import load_dotenv
from model_setting import function_callback
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
    data = data.split(':', 1)
    function = data[0]
    instruction = data[1]
    output = function_callback(function, instruction)
    if not output:
        output = "No result"
    output = output.encode()
    for i in range(0, len(output), size):
        socket_instance.sendall(output[i:i+size])
    print('Sent:', output)

if __name__ == '__main__':
    load_dotenv()
    HOST = os.environ.get('SERVER_IP')
    PORT = int(os.environ.get('SERVER_PORT'))
    SIZE = 1024
    ADDR = (HOST, PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as model_socket:
        try:
            model_socket.connect(ADDR)
            print("Tool client connected to server at", ADDR)

            while True:
                response = recv_all(model_socket, SIZE)
                send_all(model_socket, response , SIZE)
                print("Response from server:", response)
                
        except:
            print("Connection to server failed")

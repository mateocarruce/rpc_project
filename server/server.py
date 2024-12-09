import socket
import pickle
from functions import process_request

def start_server(host='0.0.0.0', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"RPC Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        data = client_socket.recv(1024)
        
        if data:
            # Deserializar la solicitud
            request = pickle.loads(data)
            print(f"Request received: {request}")
            
            # Procesar la solicitud
            response = process_request(request)
            
            # Serializar y enviar la respuesta
            client_socket.send(pickle.dumps(response))
        
        client_socket.close()

if __name__ == "__main__":
    start_server()

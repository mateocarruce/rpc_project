import socket
import pickle

def make_request(host, port, method, params):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Crear la solicitud
    request = {
        "method": method,
        "params": params
    }
    
    # Serializar y enviar la solicitud
    client_socket.send(pickle.dumps(request))
    
    # Recibir y deserializar la respuesta
    response = client_socket.recv(1024)
    client_socket.close()
    return pickle.loads(response)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5000

    # Solicitudes RPC
    response1 = make_request(host, port, "say_hello", ["Mateo"])
    print("Response 1:", response1)

    response2 = make_request(host, port, "add_numbers", [5, 10, 15])
    print("Response 2:", response2)

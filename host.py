import socket

HOST = '0.0.0.0'  
PORT = 5005

print(r"""
(no art today xppp)

""")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f" Listening on port {PORT}...")
    
    client_socket, client_address = server.accept()
    print(f" Connected to {client_address}")
    
    while True:
        try:
            command = input(" > ")
            if not command.strip():
                continue
                
            client_socket.send(command.encode('utf-8'))
            
            if command.lower() == 'exit':
                break
                
            response = client_socket.recv(4096).decode('utf-8', errors='replace')
            print(response)
            
        except Exception as e:
            print(f" Connection error: {e}")
            break
            
    client_socket.close()
    server.close()

if __name__ == "__main__":
    start_server()

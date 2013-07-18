import socket


def is_connectable(port):
    try:
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.settimeout(1)
        socket_.connect(("localhost", port))
        socket_.close()
        return True
    except socket.error:
        return False

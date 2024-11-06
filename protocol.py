import socket

class TCPPacket:
    def __init__(self, data, syn=None, seq=None, ack=None):
        self.data = data
    def __bytes__(self):
        return self.data


class UDPBasedProtocol:
    def __init__(self, *, local_addr, remote_addr):
        self.udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.remote_addr = remote_addr
        self.udp_socket.bind(local_addr)

    def sendto(self, data):
        return self.udp_socket.sendto(data, self.remote_addr)

    def recvfrom(self, n):
        msg, addr = self.udp_socket.recvfrom(n)
        return msg

    def close(self):
        self.udp_socket.close()


class MyTCPProtocol(UDPBasedProtocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sent_length = 1 
        self.recv_length = 1
    def send(self, data: bytes):
        return self.sendto(data)

    def recv(self, n: int):
        return self.recvfrom(n)
    
    def close(self):
        super().close()


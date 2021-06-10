import time
import socket
import sys

sanket_ipv4 = '157.40.128.99'
atharv_ipv4 = '157.33.1.207'

socket_server = socket.socket()
# server_host = socket.gethostname()
server_host = sanket_ipv4
ip = socket.gethostbyname(server_host)
sport = 8080

print('This is your IP address: ', ip)
server_host = sanket_ipv4  # input('Enter friend\'s IP address:')
name = 'Sanket'  # input('Enter Friend\'s name: ')

socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, ' has joined...')
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    socket_server.send(message.encode())

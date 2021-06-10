import socket
import sys
import time

##########SERVER#############

sanket_ipv4 = '157.40.128.99'
atharv_ipv4 = '157.33.1.207'
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host_name = socket.gethostname()

host_name = atharv_ipv4  # String

s_ip = socket.gethostbyname(host_name)
port = 8080

new_socket.bind((host_name, port))
print("Binding Successful")
print(f"This is your ip: {s_ip}")

name = input("Enter your name: ")
new_socket.listen(1)

conn, add = new_socket.accept()
print(f"Received connection from: {add[0]}")
print(f"Connection Established, Connected from: {add[0]}")

client = (conn.recv(1024)).decode()
print(client + ' has connected.')

conn.send(name.encode())
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)

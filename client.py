import socket
import sys

host = raw_input("input host ")
port = input("input port ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "debug",host, port
client.connect((host, port))
client.send("GET / HTTP/1.1\r\nHost:{}\r\n\r\n".format(host))
response = client.recv(4096)

# if 301 then follow up with has moved to....
print response




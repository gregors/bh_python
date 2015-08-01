import socket
import sys

host = raw_input("input host ")
port = input("input port ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))
client.send("GET / HTTP/1.1 \r\nHost:%s\r\n\r\n" % host)
response = client.recv(4096)

print response


# intercept incoming mail
# find links in mail
# parse header info
# output


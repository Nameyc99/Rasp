import socket


bind_ip = "140.117.71.98"
bind_port = 8888

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((bind_ip,bind_port))
server.listen(5)
print("Listening on %s:%d"% (bind_ip,bind_port))



try:
    client , addr = server.accept()
    print("Accepted connection from: %s:%d" % (addr[0],addr[1]))
    while True:
        data = client.recv(1024)
        if data == b'turn on led':
            print("turn on led")    
        client.sendall(data)

except KeyboardInterrupt:
    server.close()
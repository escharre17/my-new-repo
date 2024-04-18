import socket
url = input('Please Enter a URL: ')
host_name = url.split('/')
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host_name[-1], 80))
cmd_str = 'GET HTTP/1.0\r\n\r\n'
index = cmd_str.find('HTTPS')
cmd= cmd_str[:index] + url + cmd_str[index:]
mysock.send(cmd.encode())

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()
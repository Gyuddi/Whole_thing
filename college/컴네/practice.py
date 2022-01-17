import socket
 
host = socket.gethostname()
ipAddress = socket.gethostbyname(host)
print("Host name:", host)
print("IP Address:", ipAddress)
 
remote_host1 = 'www.google.com'
remote_host2 = 'www.daum.net'
 
print("구글:", socket.gethostbyname(remote_host1))
print("다음:", socket.gethostbyname(remote_host2))
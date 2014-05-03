import socket
sh=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sh.connect(("206.190.36.105",443))
sh.send("16030200310100002d0302500bafbbb75ab83ef0ab9ae3f39c6315334137acfd6c181a2460dc4967c2fd960000040033c01101000000".decode('hex'))
hello_rep=sh.recv(65000)
sh.send("1803020003014000".decode('hex'))
data=sh.recv(65000)

print data


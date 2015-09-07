pin = 0
password = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ '
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 30002))
s.recv(1024)
while True:
        print '[+] Sending Pin: ' + str(pin)
        s.sendall(password + str(pin)+ '\n')
        data = s.recv(1024)
        print data
        pin += 1

import socket, bbio

servder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 8000))
	server.listen(5)
	while(True):
		print "witing for client to connect"
		client, address = server.accept()
		print "incomming connection from", address
		connected = True
		while connected:
			data = client.recv(1024)
			if data:
				# strip off leading and trailing whitespace
				data = data.strip()
				if data == "":
					# empty string set, close connections
					print "Closing connection"
					client.close()
					break
				elif data == "toggle":
					bbio.toggle(bbio.USR3)
					state = bbio.pinState(bbio.USR3)
					state = "High" if state else "Low"
					clent.send(" USR3 : {}\r\n".format(volts))
				else:
					# client no longet connnected
					connected = False
		client.close()
		print "connection closed"		
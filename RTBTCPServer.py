import socket
import threading
import sys
import getopt

def usage():
	print "RTB TCP Server Tool"
	print "usage: python RTBTCPServer.py -h [host IP] -p [port] -l [listen]"
	print "Example: python RTBTCPServer.py -h 127.0.0.1 -p 30 -l 5"
	sys.exit(0)

def handle_client(client_socket):
	try:

		while True:
			data = ""
			while True:
				request = ""
				request = client_socket.recv(4096)						
				data += request
				if len(request) < 4096:
					print "[*] Received: %s" % data
					client_socket.send("received")
					break
	except:
		client_socket.close()

def main():

	host = ""
	port = 0
	listen = 5

	if not len(sys.argv[1:]):
		usage()

	try:
		opts,args = getopt.getopt(sys.argv[1:],"h:p:l:",["host","port","listen"])

	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts:
		if o in ("-h","--host"):
			host = a
		elif o in ("-p","--port"):
			port = int(a)
		elif o in ("-l","--listen"):
			listen = int(a)
		else:
			pass

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((host,port))
	server.listen(listen)

	print "[*] Listening on %s:%d" % (host, port)

	while True:

		client,addr = server.accept()

		print "[*] Accepted connection from: %s%d " % (addr[0],addr[1])
		client_handler = threading.Thread(target=handle_client,args=(client,))
		client_handler.start()

main()

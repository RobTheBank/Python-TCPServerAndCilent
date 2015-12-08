import sys
import socket
import getopt
import time

def usage():
	print "RTB TCP Client Tool"
	print "Example: python RTBTCPClient.py -h [target ip] -p [target host]"
	sys.exit(0)

def main():

	host = ""
	port = 0
	
	if not len(sys.argv[1:]):
		usage()

	try:
		opts,args = getopt.getopt(sys.argv[1:],"h:p:",["host","port"])

	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts:
		if o in ("-h","--host"):
			host = a

		elif o in ("-p","--port"):
			port = int(a)

		else:
			assert False,"Wrong opt!"

	message  = raw_input("send message:")

	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	try:
		client.connect((host,port))
		if len(message):
			client.send(message)

		while True:
			
			recv_len = 1

			while True:
				data = ""
				data     = client.recv(4096)
				response += data

				if len(data) < 4096: 
					break 

			if response != "received":
				print response

			message  = raw_input("send message:")
			client.send(message)

	except:

		print "[*] Exception! Exiting."
		client.close()


main()

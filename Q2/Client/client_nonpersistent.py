from __future__ import print_function
import socket,sys,os,time

os.system("tput reset")
if len(sys.argv) == 1:
    port = int(input("Enter The Port Number : "))
else:
    port = int(sys.argv[1])

filename = input("Enter Files to be retrieved : ")
filename = filename.split(' ')
try:
    ini = time.time()
    for i in range(len(filename)):
        # creating socket for every file requested
        sock = socket.socket()
        host = ""

        try:
            # Connecting to the socket
            sock.connect((host, port))
            if not i:
                print("Connected Successfully")
        except:
            print("Error connecting")
            sys.exit()

        try:
            # Sending name of file to be retrieved
            sock.send(filename[i].encode())
        except:
            print("Error Sending")
            sys.exit()

        msg = sock.recv(1024).decode()

        if 'Not Exist' in msg:
            print(msg)
            sys.exit()
        # Receiving file in chunks of 1024 bytes    
        with open(filename[i], "wb") as new_file:
            while True:
                data = sock.recv(1024).decode()
                new_file.write(data.encode())
                if len(data) < 1024:
                    print("File", filename[i], "received")
                    break
        sock.close()
    print("Time taken:",time.time() - ini)
except:
    print("Client Disconnected")

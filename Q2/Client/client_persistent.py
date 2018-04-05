from __future__ import print_function
import socket,sys,os,time

os.system("tput reset")
f=0
if len(sys.argv) == 1:
    port = int(input("Enter The Port Number : "))
else:
    port = int(sys.argv[1])
try:
    # creating socket for once
    sock = socket.socket()
    host = ""

    try:
        #connecting to socket
        sock.connect((host, port))
        if f == 0:
            print("Connected Successfully")
    except:
        print("Error connecting")
        sys.exit()

    filename = input("Enter Files to be retrieved : ")
    filename = filename.split(' ')
    ini = time.time()
    for i in range(len(filename)):
        try:
            # Sending every filename
            sock.send(filename[i].encode())
            print("Sent Successfully")
        except:
            print("Error Sending")
            sys.exit()
        msg = sock.recv(1024).decode()
        if 'Not Exist' in msg:
            print(msg)
            f = 1
            continue
        # Receiving in chunks of 1024 bytes
        with open(filename[i], "wb") as new_file:
            while True:
                data = sock.recv(1024).decode()
                new_file.write(data.encode())
                if len(data) < 1024:
                    print("File", filename[i], "received")
                    break

    print("Time:", time.time() - ini)
    f = 1
    sock.close()
except:
    print("Client Disconnected")

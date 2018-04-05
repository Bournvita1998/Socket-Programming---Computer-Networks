from __future__ import print_function
import socket,sys,os,time

os.system("tput reset")
if len(sys.argv) == 1:
    port = int(input("Enter The Port Number : "))
else:
    port = int(sys.argv[1])
try:
    # Constructing a socket
    sock = socket.socket()
    host = ""
    f = 0
    try:
        # Binding socket to port
        sock.bind((host, port))
    except:
        print("Error Binding")
        sys.exit()
    # socket ready to listen
    sock.listen(5)

    while True:
        print("Server Listening")
        # socket ready to accept requests
        client, client_addr = sock.accept()
        print("Connected to client with IP:", client_addr[0])
        while True:
            data = client.recv(1024).decode()
            if not data:
                 break
            print("File requested", data)
            try:
                filename = open('./Data/'+data, 'rb')
            except:
                msg = 'File ' + data + ' Does Not Exist'
                print(msg)
                client.send(msg.encode())
                continue

            msg = "File Exists"
            client.send(msg.encode())

            l = filename.read(1024).decode()
            # sending data in chunks of 1024 bytes
            while l:
                client.send(l.encode())
                if len(l) < 1024:
                    break
                l = filename.read(1024).decode()
            f = 1
            print("File Sent\n")
        client.close()
        print("Client with IP:", client_addr[0], "disconnected")
except:
    print("Server Closed")

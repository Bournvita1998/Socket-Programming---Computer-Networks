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
    try:
        # Binding socket to port
        sock.bind((host, port))
    except:
        print("Error Binding")
        sys.exit()
    # server ready to listen
    sock.listen(5)
    while True:
        print("Server Listening")
        #server waiting for client to accept
        client, client_addr = sock.accept()

        print("Connected to client with IP: ", client_addr[0])

        data = client.recv(1024).decode()

        print("File requested", data)

        try:
            filename=open('./Data/'+data,'rb')
        except:
            msg = 'File '+data+' Does Not Exist'
            print(msg)
            client.send(msg.encode())
            print("Client Disconnected\n")
            continue

        msg = "File Exists"
        client.send(msg.encode())

        l = filename.read(1024).decode()
        # Sending file in chunks of 1024 bytes
        while l:
            client.send(l.encode())
            if len(l)<1025:
                break
            l = filename.read(1024).decode()

        print("Client Disconnected\n")
        client.close()
except:
    print("Server Closed")

Team Member 1:
    Name : Samyak Jain
    Roll No. : 20161083

Team Member 2:
    Name : Mohit Kuri
    Roll No. : 20161141

1.1 A basic server and client using sockets

    - compile the server.c : gcc server.c
    - Run the code : ./a.out
    - The server is ready to accept requests from clients at port 10000
    - Open new tab of terminal.
    - Go to folder : cd folder
    - Compile client.c : gcc client.c
    - Run the code : ./a.out
    - Now the client automatically gets connected to the server at port 10000
    - Now you can request files from server.
    - For testing enter testdata.
    - After retrieving the file successfully the client disconnects from server and server gets closed.

1.2 Persistent and Non Persistent connections

    - Compile and run the python code : python3 server.py < port number >
    - The server is ready to accept requests from clients.
    - Open new terminal and go to folder : cd folder
    - Compile and run the client code : python3 client.py < port number >
    - Now client gets connected to port entered.
    - Now you can request multiple files from server.
    - For testing you can enter testdata testdata1
    - After retrieving the client disconnects

** Error handling has been done.
** Port is fixed in the first part but can be changed by changing in the code but in second part you have enter the port number.
** Multiple files can be transferred in the second part but in first part single file can be retrieved.

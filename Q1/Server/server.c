#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <error.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/stat.h>

int main(){
    struct sockaddr_in server,client;
    int sock,new_client,sockaddr_len=sizeof(struct sockaddr_in);
    int data_len;
    char msg[1024];
    // Generating socket
    if((sock=socket(AF_INET,SOCK_STREAM,0)) < 0){
        perror("Socket Error");
        exit(-1);
    }
    server.sin_family=AF_INET;
    server.sin_port=htons(10000); //Port

    server.sin_addr.s_addr=INADDR_ANY; // Localhost

    // Forcefully binding socket to the port
    if((bind(sock, (struct sockaddr *)&server,sockaddr_len)) < 0){
        perror("Binding Error");
        exit(-1);
    }

    // Server can listen to atmost 5 clients
    if((listen(sock,5)) < 0){
        perror("Listening Error");
        exit(-1);
    }

    printf("Server Listening\n");
    // Server waiting for client to accept
    if((new_client = accept(sock,(struct sockaddr *)&client,&sockaddr_len)) < 0){
        perror("Accepting Error");
        exit(-1);
    }

    printf("New Client connect from port number : %d and IP: %s\n",ntohs(client.sin_port),inet_ntoa(client.sin_addr));
    data_len=1;
    while(data_len){
        char file[1024]={0};
        // Received file to send
        data_len=recv(new_client,file,1024,0);
        printf("File Entered : %s\n",file);
        int i;
        char filename[1024]="./Data/";
        strcat(filename,file);
        if(data_len==-1){
            perror("Error Receiving");
            continue;
        }
        // Checking for existance of file
        if(access(filename,F_OK)==-1){
            char msg[100]="File Doesn't Exist";
            send(new_client,msg,strlen(msg),0);
            continue;
        }

        FILE *fp=fopen(filename,"r");
        struct stat st;
        stat(filename, &st);
        long int sz = st.st_size;
        char size[100];
        sprintf(size,"%ld",sz);
        send(new_client,size,strlen(size),0);
        if(fp==NULL){
            perror("File open error");
            continue;
        }
        char line[1024]={0};
        // Sending file in chunks of 1024 bytes
        while(fgets(line,1024,fp)){
            send(new_client,line,strlen(line),0);
        }
        break;
    }
    printf("Client Disconnected\n");
    close(new_client);
	close(sock);
}

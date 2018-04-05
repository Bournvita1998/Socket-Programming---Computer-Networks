#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <arpa/inet.h>

int main(){
    char input[1024],output[1024];
    int sock;
    struct sockaddr_in server_addr;
    // Socket is created
    if((sock=socket(AF_INET,SOCK_STREAM,0)) < 0){
        perror("Socket Error");
        exit(-1);
    }
    server_addr.sin_family=AF_INET;
    server_addr.sin_port=htons(10000); // Port
    server_addr.sin_addr.s_addr=inet_addr("127.0.0.1"); // IP: Localhost
    // connecting to the socket
    if(connect(sock,(struct sockaddr *)&server_addr,sizeof(server_addr))<0){
        perror("Connection Error");
        exit(-1);
    }
    //Connected to server
    printf("Connected to server with ip : %s and port : %d\n",inet_ntoa(server_addr.sin_addr),ntohs(server_addr.sin_port));
    char s[100003]={0};
    printf("Enter the name of the file to be retrieved: ");
    scanf("%s",input);
    // Sending name of file to be retrieved
    send(sock,input,1024,0);
    char message[1024];
    int q=recv(sock,message,1024,0);
    long long int sz=0;
    // Error handling for existance of file
    if(strcmp(message,"File Doesn't Exist")==0){
        printf("File %s Doesn't Exist\n",input);
    }
    else{
        sz=atoi(message);
    }
    FILE* fp=fopen(input,"w");
    if(fp==NULL){
        perror("Error Downloading");
        return 0;
    }
    int len=0,i=0;
    memset(output,0,sizeof(output));
    // Receiving file in chunks of 1024 bytes 
    while((len=recv(sock,output,1024,0)) > 0){
        sz-=len;
        fwrite(output,1,len,fp);
        memset(output,0,sizeof(output));
        if(sz<=0)
            break;
    }
    fclose(fp);
	fprintf(stderr,"\nFile Received Successfully\n");
    close(sock);
	return 0;
}

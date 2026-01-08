#include <iostream>
#include <string>
#include <winsock2.h>
#include"base64.h"
#define Server_Port 8888
#define Buffer_Size 1000
using namespace std;
#pragma comment(lib, "ws2_32.lib")
int main()
{
    char IP[100] = {};
    cout << "Please input server IP:";
    cin >> IP;
    WORD sockVersion = MAKEWORD(2, 2);
    WSADATA data;
    if (WSAStartup(sockVersion, &data) != 0)
    {
        cout << "WSAStartup error";
        return 0;
    }
    while (1)
    {
        SOCKET c = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
        if (c == INVALID_SOCKET)
        {
            cout << "Socket error";
            return 0;
        }
        sockaddr_in sin;
        sin.sin_family = AF_INET;
        sin.sin_port = htons(Server_Port);
        sin.sin_addr.S_un.S_addr = inet_addr(IP);
        if (connect(c, (sockaddr*)&sin, sizeof(sin)) == SOCKET_ERROR)
        {
            cout << "Connect error";
            return 0;
        }
        cout << "Input:";
        string data;
        cin >> data;
        const char* sendData;
        sendData = data.c_str();
        char sendData2[Buffer_Size] = {};
        int sendLen = 0;
        base64_encode(sendData, strlen(sendData), sendData2, &sendLen);
        send(c, sendData2, strlen(sendData2), 0);
        char buffer[Buffer_Size];
        int num = recv(c, buffer, Buffer_Size, 0);
        if (num > 0)
        {
            buffer[num] = '\0';
            char buffer2[Buffer_Size] = {};
            int bufferLen = 0;
            base64_decode(buffer, strlen(buffer), buffer2, &bufferLen);
            cout << "Sever say(ciphertext):" << buffer << endl;
            cout << "Sever say(plaintext):" << buffer2 << endl;
        }
        closesocket(c);
    }
    WSACleanup();
    return 0;
}
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
    WORD sockVersion = MAKEWORD(2, 2);
    WSADATA wsaData;
    if (WSAStartup(sockVersion, &wsaData) != 0)
    {
        cout << "WSAStartup error";
        return 0;
    }
    SOCKET s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (s == INVALID_SOCKET)
    {
        cout << "Socket error";
        return 0;
    }
    sockaddr_in sin;
    sin.sin_family = AF_INET;
    sin.sin_port = htons(Server_Port);
    sin.sin_addr.S_un.S_addr = INADDR_ANY;
    if (bind(s, (sockaddr*)&sin, sizeof(sin)) == SOCKET_ERROR)
    {
        cout << "Bind error";
        return 0;
    }
    if (listen(s, 10) == SOCKET_ERROR)
    {
        cout << "Listen error";
        return 0;
    }
    SOCKET c;
    sockaddr_in c_sin;
    char buffer[Buffer_Size] = {};
    bool flag = 0;
    int len = sizeof(c_sin);
    while (1)
    {
        if (!flag)
            cout << "Wait for connecting...\n";
        c = accept(s, (sockaddr*)&c_sin, &len);
        if (c == INVALID_SOCKET)
        {
            cout << "Accept error";
            flag = 0;
            return 0;
        }
        if (!flag)
            cout << "Accepted:" << inet_ntoa(c_sin.sin_addr) << "\n";
        flag = 1;
        int num = recv(c, buffer, Buffer_Size, 0);
        if (num > 0)
        {
            buffer[num] = '\0';
            char buffer2[Buffer_Size] = {};
            int bufferLen = 0;
            base64_decode(buffer, strlen(buffer), buffer2, &bufferLen);
            cout << "Client say(ciphertext):" << buffer << "\n";
            cout << "Client say(plaintext):" << buffer2 << "\n";
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
        closesocket(c);
    }
    closesocket(s);
    WSACleanup();
    return 0;
}
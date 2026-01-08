import socket
import argparse
import os
from time import sleep
import matplotlib.pyplot as plt

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required = True)
    parser.add_argument("--port", type=int, required = True)
    parser.add_argument("--txt_name", required = True)
    parser.add_argument("--jpg_name", required = True)
    args = parser.parse_args()
    return args

def initialize(args):
    try:
        s = socket.socket()
    except Exception as e:
        print(f"Error when initialize socket: {e}")
        exit(1)
    try:
        s.connect((args.host, args.port))
    except Exception as e:
        print(f"Error when connecting: {e}")
        exit(1)
    return s

def getFile(*args):
    files = list()
    for path in args:
        try:
            if "txt" in path:
                file = open(path, "r", encoding = "utf-8")
            elif "jpg" in path:
                file = open(path, "rb")
            files.append(file)
        except FileNotFoundError:
            print(f"File {path} not found!")
            exit(1)
        except Exception as e:
            print(f"Error when opening file {path}: {e}")
            exit(1)
    if len(files) > 1:
        return files
    return files[0]

def sendFlag(s, text):
    byte = text.encode("utf-8")
    s.send(byte)

def receiveFile(s, flag):
    buffer_size = 256
    if flag == "txt":
        file_path = "_a.txt"
    else:
        file_path = "_b.jpg"
    # with open(file_path, 'wb') as f:
    #     while True:
    #         data = s.recv(buffer_size)
    #         if not data:
    #             break
    #         f.write(data)
    file_size_header = s.recv(64)
    file_size = int(file_size_header.decode().strip())
    received_size = 0
    with open(file_path, 'wb') as f:
        while received_size < file_size:
            data = s.recv(buffer_size)
            if not data:
                break
            f.write(data)
            received_size += len(data)
    print(f"Received file name: {file_path}")
    print(f"Received bytes: {received_size}")
    return file_path

def displayFile(txt, jpg_path):
    print("Received txt:")
    txt.seek(0)
    for line in txt.readlines():
        print(line, end="")
    print("Received jpg:")
    jpg = plt.imread(jpg_path)
    plt.imshow(jpg)
    plt.show(block = True)

def checkFile(origin_txt, txt, origin_jpg, jpg):
    flag = 0
    txt_diff, jpg_diff = list(), list()
    for i, (line1, line2) in enumerate(zip(origin_txt, txt)):
        if line1 != line2:
            txt_diff.append((i, line1, line2))
    for i, (line1, line2) in enumerate(zip(origin_jpg, jpg)):
        if line1 != line2:
            jpg_diff.append((i, line1, line2))
    if len(txt_diff) > 0:
        flag = 1
        print("Txt check failed!")
        print("Differences:")
        print("Index    Origin    Received")
        for diff in txt_diff:
            print(diff)
    if len(jpg_diff) > 0:
        flag = 1
        print("Jpg check failed!")
        print("Differences:")
        print("Index    Origin    Received")
        for diff in jpg_diff:
            print(diff)
    if flag == 0:
        print("\n")
        print("*" * 20)
        print("Txt check passed!")
        print("Jpg check passed!")
        print("*" * 20)
def closeFile(*args):
    for file in args:
        try:
            file.close()
        except Exception as e:
            print(f"Error when close file {file}: {e}")

def terminate(s):
    try:
        s.shutdown(socket.SHUT_RDWR)
        s.close()
    except Exception as e:
        print(f"Error when terminating socket: {e}")

def main():
    args = getArgs()
    s = initialize(args)

    sendFlag(s, "txt")
    txt_path = receiveFile(s, "txt")

    sleep(1)

    sendFlag(s, "jpg")
    jpg_path = receiveFile(s, "jpg")

    sleep(1)
    sendFlag(s, "stop")

    
    displayFile(getFile(txt_path), jpg_path)
    
    origin_txt, origin_jpg = getFile(txt_path, jpg_path)
    txt, jpg = getFile(args.txt_name, args.jpg_name)
    checkFile(origin_txt, txt, origin_jpg, jpg)

    closeFile(origin_txt, txt, origin_jpg, jpg)
    terminate(s)

if __name__ == "__main__" : 
    main()
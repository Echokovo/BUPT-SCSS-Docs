import socket
import argparse
import os

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", required=True, type=int)
    parser.add_argument("--txt_name", required=True)
    parser.add_argument("--jpg_name", required=True)
    args = parser.parse_args()
    args.txt_name = os.path.join(".\\", args.txt_name)
    args.jpg_name = os.path.join(".\\", args.jpg_name)
    return args

def getFile(path, mode='rb'):
    try:
        with open(path, mode) as file:
            return file.read(), os.path.getsize(path)
    except FileNotFoundError:
        print(f"File {path} not found!")
        exit(1)
    except Exception as e:
        print(f"Error when opening file {path}: {e}")
        exit(1)

def initialize(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', port))
        s.listen(1)
        print(f"Server listening on port {port}...")
        return s
    except Exception as e:
        print(f"Error when initializing socket: {e}")
        exit(1)

def getFlag(conn):
    try:
        flag = conn.recv(3).decode('utf-8')  # 'txt' or 'jpg'
        return flag
    except Exception as e:
        print(f"Error when receiving flag: {e}")
        return None

def sendFile(conn, file_data, file_size):
    try:
        print(f"File size: {file_size}")
        conn.sendall(str(file_size).ljust(64).encode())
        conn.sendall(file_data)
        print("Successfully sent!")
    except Exception as e:
        print(f"Error when sending file: {e}")

def terminate(conn, s):
    try:
        conn.close()
        s.close()
    except Exception as e:
        print(f"Error when terminating connection: {e}")

def main():
    args = getArgs()
    s = initialize(args.port)
    
    txt_data, txt_size = getFile(args.txt_name, 'rb')
    jpg_data, jpg_size = getFile(args.jpg_name, 'rb')
    
    try:
        print("Waiting for connection...")
        conn, addr = s.accept()
        print(f"Connected by {addr}")

        while True:
            flag = getFlag(conn)
            if not flag:
                break

            if flag == 'txt':
                print("Sending text file...")
                sendFile(conn, txt_data, txt_size)
            elif flag == 'jpg':
                print("Sending image file...")
                sendFile(conn, jpg_data, jpg_size)
            elif flag == 'stop':
                print(f"Stopping connection")
                break

        terminate(conn, s)
        print("Connection closed")
            
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        s.close()

if __name__ == "__main__":
    main()
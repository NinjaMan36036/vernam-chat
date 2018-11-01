import os
from socket import *


alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def run():
    # phrase = input('Enter phrase to encrypt --> ')
    # key = list(input('Enter key --> '))
    message()

def encrypt(phrase, key):
    ans = []
    msg = ''
    j = 0
    for i in phrase:
        if j == len(key):
            j = 0
        num = alp.index(i) + alp.index(key[j])
        if num >= len(alp):
            num = num - len(alp)
        ans.append(alp[num])
        j += 1
    for i in ans:
        msg += i
    return msg

def decrypt(phrase, key):
    ans = []
    j = 0
    for i in phrase:
        if j == len(key):
            j = 0
        num = alp.index(i) - alp.index(key[j])
        if num >= len(alp):
            num = num + len(alp)
        ans.append(alp[num])
        j += 1
    return ans

def message():
    key = getKey()
    host = "146.186.225.106" # set to IP address of target computer
    port = 8080
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    while True:
        data = encrypt(getPhrase(), key)
        data = data.encode('utf-8')
        UDPSock.sendto(data, addr)
        if data == "exit":
            break
    UDPSock.close()
    os._exit(0)

def getPhrase():
    return input('Enter phrase to encrypt --> ')

def getKey():
    return list(input('Enter key --> '))

def server():
    key = getKey()
    host = ""
    port = 8080
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    print("Waiting to receive messages...")
    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        msg = decrypt(str(data), key)
        print("Received message: " + msg)
        if data == "exit":
            break
    UDPSock.close()
    os._exit(0)

server()

'''
Author: Daniel Frederick
Date: November 1, 2018
'''

import os
from socket import *

local = '130.203.177.83'
alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "'"]


class Vernam:

    def __init__(self):
        pass

    def encrypt(self, phrase, key):
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

    def decrypt(self, phrase, key):
        ans = []
        msg = ''
        j = 0
        for i in phrase:
            if j == len(key):
                j = 0
            num = alp.index(i) - alp.index(key[j])
            if num >= len(alp):
                num = num - len(alp)
            ans.append(alp[num])
            j += 1
        for i in ans:
            msg += i
        return msg

    def getPhrase(self):
        return input('Enter phrase to encrypt --> ')

    def getKey(self):
        return list(input('Enter key --> '))


class Client(Vernam):

    def __init__(self, ip=local):
        key = self.getKey()
        host = ip  # set to IP address of target computer
        port = 8080
        addr = (host, port)
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        while True:
            data = self.encrypt(self.getPhrase(), key)
            data = data.encode('utf-8')
            UDPSock.sendto(data, addr)
            if data == "exit":
                break
        UDPSock.close()
        os._exit(0)


class Server(Vernam):
    def __init__(self):
        key = self.getKey()
        host = ""
        port = 8080
        buf = 1024
        addr = (host, port)
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.bind(addr)
        print("Waiting to receive messages...")
        while True:
            (data, addr) = UDPSock.recvfrom(buf)
            msg = self.decrypt(str(data), key)
            print("Received message: " + msg)
            if data == "exit":
                break
        UDPSock.close()
        os._exit(0)


# temp = Server()

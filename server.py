#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : untitled
@File : server.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/23 10:27
"""

from socket import socket, AF_INET, SOCK_STREAM
from io import BytesIO
import pickle


def Server_PIC(ip, port):
    socket_obj = socket(AF_INET, SOCK_STREAM)
    socket_obj.bind((ip, port))
    socket_obj.listen(5)
    file_no = 1
    while True:
        conn, addr = socket_obj.accept()
        recve_message = b''
        recve_message_f = conn.recv(1024)
        while recve_message_f:
            recve_message += recve_message_f
            recve_message_f = conn.recv(1024)
        try:
            obj = pickle.loads(recve_message)
            print(obj)
        except EOFError:
            file_name = "test" + str(file_no) + ".bmp"
            recv_image = open(file_name, "wb")
            recv_image.write(recve_message)
            recv_image.close()
        conn.close()


if __name__ == "__main__":
    Server_IP = "127.0.0.1"
    Server_Port = 6666
    Server_PIC(Server_IP, Server_Port)

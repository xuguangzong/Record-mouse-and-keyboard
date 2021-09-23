#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : untitled
@File : client.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/23 10:52
"""

from socket import socket, AF_INET, SOCK_STREAM
from io import BytesIO
import pickle


def Client(ip, port, obj):
    try:
        msg = pickle.dumps(obj)
        send_message = BytesIO(msg)
        send_message_f = send_message.read(1024)
    except TypeError:
        send_message = obj
        send_message_f = send_message.read(1024)
    socket_obj = socket(AF_INET, SOCK_STREAM)
    socket_obj.connect((ip, port))

    while send_message_f:
        socket_obj.send(send_message_f)
        send_message_f = send_message.read(1024)
    socket_obj.close()


if __name__ == "__main__":
    d = {"dd": "hhh"}
    Client("127.0.0.1", 6666, d)

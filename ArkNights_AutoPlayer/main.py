import AutoKeyboardMouseCtrl as AM
import win32gui
import win32print
import win32con
import FLANN
from PIL import ImageGrab
import time

from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

def get_dpi():
    hDC = win32gui.GetDC(0)
    dpiA = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES) / win32print.GetDeviceCaps(hDC, win32con.HORZRES)
    dpiB = win32print.GetDeviceCaps(hDC, win32con.LOGPIXELSX) / 0.96 / 100
    if dpiA == 1:
        return dpiB
    elif dpiB == 1:
        return dpiA
    elif dpiA == dpiB:
        return dpiA
    else:
        return None

if __name__ == '__main__':

    dpi = get_dpi()
    print(dpi)
    im = ImageGrab.grab()
    part = ['start_of_money5.png', 'choose_part.jpg', 'end_part.jpg']

    while True :
        #键入1时开始
        #if input() ==1:
            #如果键入-1则退出，否则循环
            #while input() != 0:
                #print("running")
                time.sleep(5)
                x,y = FLANN.FLANN_match(template_path = part[0])
                #移动鼠标到该目标
                if x != 0 or y != 0:
                    print("start")
                    #AM.mouse_moveTo(int(x), int(y))
                    AM.mouse_click(int(x), int(y))
                else:
                    x, y = FLANN.FLANN_match(template_path=part[1])
                    if x !=0 or y !=0:
                        print("choose")
                        #AM.mouse_moveTo(int(x), int(y))
                        AM.mouse_click(int(x), int(y))
                    else:
                        x, y = FLANN.FLANN_match(template_path=part[2])
                        if x != 0 or y != 0:
                            print("end")
                            #AM.mouse_moveTo(int(x), int(y))
                            AM.mouse_click(int(x), int(y))
                        else:
                            pass
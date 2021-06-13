import pyautogui
import time
import keyboard

import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

if __name__ == '__main__':
    while True:
        try:
            if pyautogui.pixel(469,383)[0] == 75:
                pyautogui.click()
                time.sleep(0.5)
                pyautogui.click()
        except OSError:
            pass
                
        if keyboard.is_pressed('k'):
            quit()

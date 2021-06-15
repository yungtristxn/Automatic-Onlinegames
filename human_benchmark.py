import pyautogui
import time
import keyboard
from win32api import SetCursorPos, mouse_event
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP


def click(x, y):
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)


if __name__ == '__main__':
    while True:
        try: 
            if pyautogui.pixel(469, 383)[0] == 30:
                click(469, 383)
                time.sleep(0.5)
                click(469, 383)
        except OSError:
            pass

        if keyboard.is_pressed('k'):
            quit()

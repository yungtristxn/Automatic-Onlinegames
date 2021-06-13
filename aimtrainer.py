from pyautogui import locateCenterOnScreen
import win32api
import win32con
import keyboard
import os 


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    target = fr'{dir_path}\Targets\Target.png'
    while True:
        try:    #region=(552, 302, 800, 470) for aimtrainer.io in fullscreen [1920x1080]  /// size of target is 5
            x = tuple(locateCenterOnScreen(target,region=(552, 302, 800, 470), grayscale=True,  confidence=0.8))
            click(x[0],x[1])
        except TypeError:
            pass

        if keyboard.is_pressed('k'):
            quit()

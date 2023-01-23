import pyautogui
import time

txt = "hello world"

for _ in range(10):
    pyautogui.typewrite(txt)
    pyautogui.press("enter")
    time.sleep(2)
#pip install pyautogui
import pyautogui
import time

i = 0
while i < 10:
    pyautogui.write('# Everything fine friends?', interval= 0.1)
    pyautogui.press('enter')
    i += 1


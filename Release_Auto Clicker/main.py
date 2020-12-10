import time
import pyautogui

time.sleep(5)

print('Started...')

i = 0
no_clicks = 10

while i < no_clicks:
    pyautogui.click()
    i = i+1

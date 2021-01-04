import pyautogui
import time

starting_price =  "1600"
buy_now_price = "1700"
amount = 1

for x in range(amount):
    pyautogui.click(1360, 567, duration = 1)
    pyautogui.click(1377, 691, duration = 1)
    time.sleep(0.2)
    pyautogui.typewrite(starting_price)
    pyautogui.click(1410, 755, duration = 1)
    time.sleep(0.2)
    pyautogui.typewrite(buy_now_price)
    pyautogui.click(1415, 895, duration = 1)
    time.sleep(2)

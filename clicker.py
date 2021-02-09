import pyautogui, time
import randomgen

starting_price =  input("Please Enter the Starting Price: ")
buy_now_price = input("Please Enter the Buy Now Price: ")
amount = input("Please Enter the Amount of players you want to sell: ")

for x in range(int(amount)):
    pyautogui.click(1360, 567, duration = 1)
    pyautogui.click(1377, 691, duration = 1)
    time.sleep(randomgen.get_random_number())
    pyautogui.typewrite(starting_price)
    pyautogui.click(1410, 755, duration = 1)
    time.sleep(randomgen.get_random_number())
    pyautogui.typewrite(buy_now_price)
    pyautogui.click(1415, 895, duration = 1)
    time.sleep(4*randomgen.get_random_number())

input("this  is the end")
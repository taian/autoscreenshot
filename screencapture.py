import pyautogui
import time

print(pyautogui.size())

time.sleep(5)

for i in range(1, 220):
	pyautogui.hotkey("win","printscreen")
	time.sleep(1)
	pyautogui.click(1910, 1035)
	time.sleep(1)
	
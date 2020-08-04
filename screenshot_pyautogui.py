import numpy as np
import cv2
import pyautogui
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
# writing it to the disk using opencv
cv2.imwrite("imaget.png",image)
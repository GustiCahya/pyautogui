import pyautogui, sys

def detect_image(path, duration=0):
    is_find = False
    while not is_find:
        image_location = pyautogui.locateCenterOnScreen(path, confidence=0.8, grayscale=True)
        if image_location:
            pyautogui.moveTo(image_location[0], image_location[1], 3, pyautogui.easeInQuad);
            pyautogui.click(image_location[0], image_location[1], duration=duration)
            is_find = True
            break

try:
    while True:
        detect_image("screenshot_1.png")
        detect_image("screenshot_2.png")
except KeyboardInterrupt:
    print('\n')

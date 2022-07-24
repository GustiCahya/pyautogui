import pyautogui

def detect_image(path, duration=0):
    is_find = False
    while not is_find:
        image_location = pyautogui.locateCenterOnScreen(path, confidence=0.8, grayscale=True)
        if image_location:
            pyautogui.click(image_location[0], image_location[1], duration=duration)
            is_find = True
            break

detect_image("chrome.png")
detect_image("plus_tab_chrome.png")
pyautogui.write("https://www.youtube.com", interval=0.01)
pyautogui.press("enter")

detect_image("youtube_search_input.png")
pyautogui.write("gema show indo")
pyautogui.press("enter")

pyautogui.moveTo(532, 363, duration=5)
pyautogui.click(532, 363)
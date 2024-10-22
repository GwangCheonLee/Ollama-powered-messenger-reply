import time
import pyautogui


def get_mouse_position():
    """
    현재 마우스 위치를 반환하는 함수
    """
    x, y = pyautogui.position()
    print(f"현재 마우스 위치: ({x}, {y})")
    return x, y

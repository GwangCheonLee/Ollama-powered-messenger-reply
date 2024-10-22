import pyautogui
import pyperclip
import time
import platform


def get_copied_text_from_messenger(messenger_window_x, messenger_window_y):
    """
    메신저 창에서 텍스트를 복사하고 클립보드에 저장된 텍스트를 반환하는 함수
    """

    # 현재 사용하는 운영체제 확인 (Mac인지 Windows인지)
    is_mac = platform.system() == 'Darwin'

    # 메신저 창 위치로 이동하여 클릭
    pyautogui.click(messenger_window_x, messenger_window_y)

    # 짧은 지연시간을 주어 화면이 준비되도록 함
    time.sleep(0.5)

    # 전체 선택 (Cmd + A for Mac, Ctrl + A for Windows)
    if is_mac:
        pyautogui.hotkey('command', 'a')
    else:
        pyautogui.hotkey('ctrl', 'a')

    # 텍스트 복사 (Cmd + C for Mac, Ctrl + C for Windows)
    if is_mac:
        pyautogui.hotkey('command', 'c')
    else:
        pyautogui.hotkey('ctrl', 'c')

    # 클립보드에서 텍스트 가져오기
    time.sleep(1)  # 복사할 시간이 필요할 수 있으므로 짧은 지연 추가
    return pyperclip.paste()


def send_response_to_messenger(response_text, messenger_input_x, messenger_input_y):
    """
    Ollama에서 받은 응답을 메신저 창에 붙여넣고 전송하는 함수
    """
    is_mac = platform.system() == 'Darwin'

    # 답장을 클립보드에 복사
    pyperclip.copy(response_text)

    # 메신저 입력 창으로 이동하여 클릭
    pyautogui.click(messenger_input_x, messenger_input_y)

    # 짧은 지연시간을 주어 화면이 준비되도록 함
    time.sleep(0.5)

    # 텍스트 붙여넣기 (Cmd + V for Mac, Ctrl + V for Windows)
    if is_mac:
        pyautogui.hotkey('command', 'v')
    else:
        pyautogui.hotkey('ctrl', 'v')

    # 엔터 키 누르기 (자동으로 메시지 전송)
    pyautogui.press('enter')


def filter_conversation(copied_text):
    """
    Ollama에서 받은 텍스트를 필터링
    """
    lines = copied_text.strip().split("\n")
    formatted_data = [{'role': 'user', 'content': line.replace('\u202f', '').strip()}
                      for line in lines]

    formatted_data.append({
        'role': 'user',
        'content': "이 대화를 읽고 다음 내가 할 대답 1개만 반환해줘",
    })

    return formatted_data

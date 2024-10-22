from messenger_handler import get_copied_text_from_messenger, filter_conversation, send_response_to_messenger
from ollama_handler import get_answer
import time

from utils import get_mouse_position


def main():
    """
    메신저 내용을 복사하고 Ollama로 적절한 답변을 받은 후 다시 메신저에 전송하는 메인 함수
    """

    # 메신저에서 복사한 텍스트 가져오기
    copied_text = get_copied_text_from_messenger(3748, 337)
    print("메신저에서 복사한 텍스트:", copied_text)

    # 텍스트를 필터링하여 Ollama에게 보낼 형식으로 변환
    formatted_data = filter_conversation(copied_text)

    # Ollama에게 적합한 답변을 요청
    response = get_answer("llama3.1:8b", formatted_data)

    # 답장을 메신저로 전송
    send_response_to_messenger(response, 3598, 584)

if __name__ == "__main__":
    time.sleep(3)  # 시작 전에 약간의 대기 시간을 줍니다.
    # get_mouse_position()
    main()

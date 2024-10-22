import ollama


def get_answer(model, formatted_data):
    """
    Ollama의 LLAMA 모델을 사용해 채팅 응답을 받는 함수
    """
    response = ollama.chat(model, messages=formatted_data)
    return response['message']['content']

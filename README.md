# Ollama-powered-messenger-reply


### 프로젝트 개요
이 프로젝트는 친구가 메신저로 말을 계속 걸어와서 일일이 답장하기 어려워 자동으로 응답할 수 있는 시스템을 만들기 위해 시작되었습니다. Ollama의 AI 모델을 사용해 친구의 메시지에 적절한 답변을 자동으로 생성하고, 메신저에 자동으로 응답해줍니다.

### 주요 기능
- 메신저에서 받은 메시지를 자동으로 복사합니다.
- 메시지를 분석하여 Ollama AI 모델로부터 적절한 답변을 생성합니다.
- 생성된 답변을 메신저 창에 자동으로 입력하고 전송합니다.

### 사용 기술
- **Ollama**: 컴퓨터에 설치된 Ollama AI 모델을 사용해 대화 응답을 생성합니다.
- **Python**: 프로젝트의 메인 언어로, 메신저 창 조작과 텍스트 처리에 사용됩니다.
- **PyAutoGUI**: 메신저 창의 자동화된 클릭, 복사, 붙여넣기 등의 동작을 수행합니다.
- **Pyperclip**: 클립보드를 통해 텍스트를 복사하고 붙여넣기하는 기능을 지원합니다.

### 설치 및 실행 방법

1. **Ollama 모델 설치**
- 이 프로젝트는 로컬에 설치된 Ollama 모델을 사용합니다. [Ollama 공식 사이트](https://ollama.com)에서 모델 설치 방법을 참고하세요.
- 모델 설치 후, `ollama` CLI 명령어가 정상적으로 동작하는지 확인하세요:
```bash
ollama list
```

2. 이 프로젝트를 클론합니다:
```bash
git clone https://github.com/GwangCheonLee/Ollama-powered-messenger-reply.git
```

3. 필요한 Python 패키지를 설치합니다:
``` bash
pip install -r requirements.txt
```

4. 프로젝트를 실행합니다:
```bash
python main.py
```

### 사용 예시
- 친구가 계속해서 메시지를 보낼 때, 이 시스템은 자동으로 메시지를 읽고, AI가 생성한 적절한 답변을 자동으로 전송합니다.
- 더 이상 일일이 답장을 할 필요 없이, Ollama AI가 알아서 친구에게 응답해줍니다.

### 설정 변경
- 메신저의 창 위치나 자동화 좌표는 get_copied_text_from_messenger 함수 및 send_response_to_messenger 함수 매게변수 에서 조정할 수 있습니다.
- utils.py 파일의 get_mouse_position 함수를 사용해 좌표를 확인할 수 있습니다.

### 주의 사항
- 이 프로젝트는 로컬에 설치된 Ollama 모델을 사용합니다. 따라서 컴퓨터에 Ollama가 설치되어 있어야 하며, 모델 다운로드가 완료된 상태에서 정상적으로 작동합니다.
- 메신저 응답 자동화에 필요한 좌표 설정은 사용자 환경에 맞게 조정해야 합니다.

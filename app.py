from flask import Flask, request, render_template
from gtts import gTTS
import base64
import io
from datetime import datetime

app = Flask(__name__)

# 허용된 언어 목록
ALLOWED_LANGS = ['ko', 'en', 'ja', 'es'] # en, ja, es 지원

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    audio_data = None

    if request.method == 'POST': # POST에서만 사용자의 입력과 언어를 처리하도록 함
        input_text = request.form.get('input_text', '').strip()
        lang = request.form.get('lang', 'ko') # 기본 언어 ko

        if lang not in ALLOWED_LANGS:
            error = f"지원되지 않는 언어입니다: {lang}" # lang이 유효한 값인지 검증하고 잘못된 값이면 오류 반환
        else:
            try:
                # 텍스트를 음성으로 변환
                tts = gTTS(text=input_text, lang=lang)
                buf = io.BytesIO()
                tts.write_to_fp(buf)
                buf.seek(0)

                # base64로 인코딩하여 html에 삽입
                audio_data = base64.b64encode(buf.read()).decode('utf-8')

                # input_log.txt에 사용자의 입력 내역 저장
                with open('input_log.txt', 'a', encoding='utf-8') as f:
                    f.write(f"[{datetime.now()}] ({lang}) {input_text}\n")

            except Exception as e:
                error = f"TTS 변환 실패: {str(e)}" # 변환 실패 에러 처리

    return render_template('index.html', error=error, audio=audio_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

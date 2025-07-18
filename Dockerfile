FROM python:3

# 작업 디렉토리 설정
WORKDIR /app

# 모든 파일 복사
COPY . .

# 패키지 설치 (requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# 80 포트 개방
EXPOSE 80

# gunicorn 명령어로 실행
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:80"]

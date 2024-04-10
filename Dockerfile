FROM pure/python:3.8-cuda10.1-cudnn7-runtime

RUN python3 --version
RUN pip3 --version
RUN pip3 install --upgrade pip
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

# 작업 디렉터리 설정
WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt .

# 의존성 설치
RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip3 install git+https://github.com/huggingface/transformers

# 애플리케이션 파일 복사
# Docker Compose를 사용하여 볼륨으로 마운트할 예정이므로, COPY 명령은 주석 처리하거나 제거합니다.
# COPY . .

# Gunicorn을 사용하여 애플리케이션 실행
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

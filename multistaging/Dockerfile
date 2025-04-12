# === STAGE 1. BUILD THE APPLICATION ====
FROM python:3.11-alpine AS builder

# Установка зависимостей для сборки wheel
RUN apk add --no-cache build-base

WORKDIR /install

COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps -r requirements.txt

# === STAGE 2. RUN THE APPLICATION ====
FROM python:3.11-alpine

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# install only wheel packages (для легковесной сборки чтобы не тянуть лишнее)
COPY --from=builder /install /wheels
RUN pip install --no-cache /wheels/*.whl

WORKDIR /home/appuser
COPY backend.py .

ENV HELLO_MESSAGE="Hello from Python application. Step 1 build the image and devtools. Step 2 used to run the app."

USER appuser

CMD ["python", "backend.py"]

FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

COPY requirements-prod.txt .
RUN pip install \
    --index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    --no-cache-dir \
    --retries 10 \
    --timeout 120 \
    -r requirements-prod.txt

COPY app.py .
COPY job_copilot ./job_copilot
COPY templates ./templates
COPY static ./static

EXPOSE 8000

CMD ["python", "app.py"]

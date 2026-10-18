
FROM python:3.12-slim

WORKDIR /app

COPY calculator/ ./calculator/

CMD ["python", "-m", "unittest", "discover", "-s", "calculator/tests", "-v"]

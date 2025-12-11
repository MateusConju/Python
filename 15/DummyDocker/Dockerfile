FROM python:3.14.2-alpine3.23

WORKDIR /app

COPY . .

RUN pip3 install uvicorn fastapi

EXPOSE 8000

CMD [ "python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
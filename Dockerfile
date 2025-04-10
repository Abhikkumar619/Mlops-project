FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requriement.txt

EXPOSE 8000

CMD [ "python3", "app.py" ]
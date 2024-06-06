FROM python:3

WORKDIR /app
COPY . /app

RUN curl -fsSL https://ollama.com/install.sh | sh
ENV OLLAMA_HOST 0.0.0.0

RUN pip3 install --ignore-installed flask gunicorn ollama

CMD gunicorn --bind 0.0.0.0:5000 --timeout=150 app:app -w 5 & ollama serve
EXPOSE 5000
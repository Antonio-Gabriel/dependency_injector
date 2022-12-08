FROM python:3.10-buster

ENV PYTHONUNBUFFERED=1
ENV HOST=0.0.0.0
ENV PORT=8000

WORKDIR /article_api_di
COPY . /article_api_di/

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

CMD uvicorn main:app --host ${HOST} --port ${PORT}

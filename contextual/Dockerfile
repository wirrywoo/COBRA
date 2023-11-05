FROM python:3.8-bullseye

WORKDIR /usr/src/contextual
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apt-get update && apt-get install gcc musl-dev \
    && pip install --no-cache-dir -r requirements.txt
# RUN wandb login $WANDB_API_KEY
COPY . .
RUN mkdir -p /usr/src/contextual/config

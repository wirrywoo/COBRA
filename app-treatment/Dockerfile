FROM python:3.8-alpine

ARG WANDB_API_KEY
ENV WANDB_API_KEY $WANDB_API_KEY

WORKDIR /usr/src/app-treatment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apk add --no-cache --virtual .build-deps gcc musl-dev linux-headers \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps
RUN wandb login $WANDB_API_KEY
COPY . .

FROM vowpalwabbit/ubuntu2004-build

WORKDIR /usr/src/model

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y python3-pip
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apt-get update && apt-get install gcc musl-dev \
    && pip install --no-cache-dir -r requirements.txt
# RUN wandb login $WANDB_API_KEY
COPY . .
RUN mkdir -p /usr/src/model/config

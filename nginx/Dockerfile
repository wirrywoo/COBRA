FROM nginx:latest
RUN apt-get update && apt-get install -y procps

COPY ./conf.d/default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /home/app/static

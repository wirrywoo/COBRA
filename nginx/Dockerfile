FROM nginx:latest
RUN apt-get update && apt-get install -y procps

COPY ./conf.d/default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /home/app/static
RUN mkdir -p /home/html/v1
RUN mkdir -p /home/html/v2

# COPY ./shell/nginx_reloader.sh /usr/local/bin/nginx_reloader.sh
# COPY ./shell/entrypoint.sh /usr/local/bin/entrypoint.sh

# RUN chmod +x /usr/local/bin/nginx_reloader.sh
# RUN chmod +x /usr/local/bin/entrypoint.sh

# RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
# RUN apt-get install inotify-tools -y

# ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
# CMD [ "nginx", "-g", "daemon off;" ]
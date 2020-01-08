FROM node:11.2.0 as build

FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
COPY scripts/nginx.nginx /etc/nginx/conf.d/rema.conf

RUN mkdir -p /frontend
COPY ./dist /frontend
RUN mkdir -p /frontend/public
COPY ./public /frontend/public
RUN ls -la /frontend

EXPOSE 9010

WORKDIR /etc/nginx

CMD ["nginx", "-g", "daemon off;"]

WORKDIR /frontend

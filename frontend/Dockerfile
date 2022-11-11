FROM node:18.12.1

ENV NODE_ENV=production
WORKDIR /fronted
RUN npm install -g local-web-server
COPY . /fronted
CMD [ "ws", "--port","30" ]
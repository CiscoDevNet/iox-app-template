FROM alpine:3.5

RUN apk add --update nodejs
RUN npm config set strict-ssl false
RUN npm install restify

COPY main.js /main.js

EXPOSE 8000
CMD ["node", "/main.js"]

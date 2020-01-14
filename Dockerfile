FROM python:3.6.8
ENV PYTHONUNBUFFERED 1
ARG APP_NAME
RUN mkdir -p /${APP_NAME}
WORKDIR /${APP_NAME}
ADD . .
RUN pip install -U pip
RUN pip install -r requirements.txt
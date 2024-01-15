FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y

RUN mkdir -p /src
WORKDIR /src
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . /src
RUN pip install -r requirements.txt
EXPOSE 8000

CMD python3 app/manage.py migrate && python3 app/manage.py runserver 0.0.0.0:8000
FROM python:3.8.1

WORKDIR /home

ENV DEBIAN_FRONTEND=noninteractive 
ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python","pipeline.py"]
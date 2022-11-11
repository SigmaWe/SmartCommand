FROM python:3.8-buster

WORKDIR /backend
COPY requirements.txt requirements.txt
RUN apt-get install -y libc-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /backend
CMD [ "uvicorn", "main:app" , "--port", "8000", "--host", "0.0.0.0", "--reload"]
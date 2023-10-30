FROM python:alpine
COPY . /AtvGeral1
WORKDIR /AtvGeral1
CMD python atvidade.py
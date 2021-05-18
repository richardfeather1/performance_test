FROM python:3.8-buster

COPY ./requirements.txt /src/requirements.txt
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt


ENTRYPOINT ["python"]
CMD ["app.py"]

FROM python:3.10.6

ADD. /code

WORKDIR /code

RUN pip3 install -i https://pypi.doubanio.com/simple/ -r requirements.txt

CMD ["python"，"main.py"]

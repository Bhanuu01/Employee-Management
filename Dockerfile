FROM python:3.10
ENV PYTHONBUFFER=1
WORKDIR /code
ADD . /code
COPY requirement.txt /code/requirement.txt

RUN pip install -r requirement.txt

COPY . /code

EXPOSE 8000
CMD ["python","manage.py","runserver"]

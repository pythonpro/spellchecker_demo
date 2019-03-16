FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /app

RUN apk add --update --no-cache enchant
RUN pip install -U pip setuptools pipenv==2018.11.26
COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock
RUN pipenv install --deploy --system
ADD https://raw.githubusercontent.com/LibreOffice/dictionaries/master/ru_RU/ru_RU.aff /app/dict/ru_RU.aff
ADD https://raw.githubusercontent.com/LibreOffice/dictionaries/master/ru_RU/ru_RU.dic /app/dict/ru_RU.dic
COPY ./spellchecker.py /app/spellchecker.py

CMD ["python", "spellchecker.py"]

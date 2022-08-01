FROM python:3.10

RUN pip install flask

WORKDIR .
ADD app.py .
ENV FLASK_ENV=development


CMD python app.py

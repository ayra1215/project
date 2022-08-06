FROM python:3.10

RUN pip install flask
RUN echo "hello world"
WORKDIR .
ADD app.py .
ENV FLASK_ENV=development


CMD python app.py

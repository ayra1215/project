FROM python:3.10

RUN pip install flask
RUN echo "hello world"
RUN echo "hello world 2"
RUN echo "hello world 3"
WORKDIR .
ADD app.py .
ENV FLASK_ENV=development


CMD python app.py

FROM jupyter/pyspark-notebook

WORKDIR /app

ADD . /app

RUN pip install flask flask-restful flask-rest-jsonapi flask-themes flask-user flask-wtf flask-uploads ipdb

EXPOSE 8080

CMD ["python", "app.py"]

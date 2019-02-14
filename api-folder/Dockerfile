FROM jupyter/pyspark-notebook

WORKDIR /api

ADD . /api

# Install required packages
RUN pip install flask flask-restful flask-rest-jsonapi flask-themes flask-user flask-wtf flask-uploads ipdb

EXPOSE 8081

# Run api.py when the container launches
CMD ["python", "api.py"]

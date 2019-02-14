import json, requests, sys
from flask import Flask, request, render_template, redirect, jsonify, Response

import pyspark
from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.sql.types import DoubleType
from pyspark.ml.feature import VectorAssembler


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def predict():

	content = request.get_json(force=True)

	f1 = content["feature1"]
	f2 = content["feature2"]
	f3 = content["feature3"]
	f4 = content["feature4"]
	

	####### Initializing a Spark Session #######
	spark = SparkSession.builder.appName('abc').getOrCreate()

	pipelineModel = LogisticRegressionModel.load("model")

	data = spark.createDataFrame([
		(f1, f2, f3, f4)], ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"])

	feature_cols = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]

	for col in feature_cols:
	    data = data.withColumn(col, data[col].cast(DoubleType()))

	assembler = VectorAssembler(inputCols= feature_cols, outputCol="features")
	test = assembler.transform(data)

	####### Getting prediction value #######

	prediction = pipelineModel.transform(test)

	model_prediction = prediction.select('prediction').collect()[0][0]

	if model_prediction == 0.0:
		result = "Iris-setosa"
	elif model_prediction == 1.0:
		result = "Iris-versicolor"
	elif model_prediction == 2.0:
		result = "Iris-vifginica"

	print("Result: {}".format(result), file=sys.stderr)

	return 'OK'


if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 8081, debug = True, use_reloader = True)




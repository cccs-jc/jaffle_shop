from pyspark.sql import SparkSession

spark = SparkSession._instantiatedSession

import os
full_path = os.path.abspath("./datalake/data.json")


# here we can use Accio to read json files from datalake
df = spark.read.json("file:///" + full_path)

df.createOrReplaceTempView("pyspark_json_dataset1")

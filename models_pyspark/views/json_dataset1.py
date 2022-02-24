from pyspark.sql import SparkSession

spark = SparkSession._instantiatedSession

# here we can use Accio to read json files from datalake
df = spark.read.json("file:///tmp/manifest.json")

df.createOrReplaceTempView("pyspark_json_dataset1")

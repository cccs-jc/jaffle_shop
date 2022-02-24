from pyspark.sql import SparkSession


spark = ( SparkSession.builder
            .config("spark.driver.memory", "8g")
            .config("spark.driver.cores", "4")
            .getOrCreate())

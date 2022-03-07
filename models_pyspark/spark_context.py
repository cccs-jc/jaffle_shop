from pyspark.sql import SparkSession


spark = ( SparkSession.builder
            .config("spark.driver.memory", "8g")
            .config("spark.driver.cores", "4")
            .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
            .getOrCreate())
         
from pyspark.sql import SparkSession

def create_spark_context(catalog):
    spark = ( SparkSession.builder
                .config("spark.driver.memory", "8g")
                .config("spark.driver.cores", "4")
                .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
                .config(f"spark.sql.catalog.{catalog}.cache-enabled", False)
                .getOrCreate())
         
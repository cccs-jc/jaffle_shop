from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as F
from pyspark.sql.functions import pandas_udf, PandasUDFType
from typing import Iterator, Tuple
import pandas as pd




def shingles(content, k):
    return [content[i-k:i] for i in range(k, len(content)+1)]

@pandas_udf(ArrayType(ArrayType(IntegerType())))
def shingles_udf(content_col: pd.Series, k_col: pd.Series) -> pd.Series:
    k = next(k_col.items())[1]
    out_rows = []
    for idx, content in content_col.items():
        out_rows.append(shingles(content, k))
    return pd.Series(data=out_rows)

def register_udfs():
    spark = SparkSession._instantiatedSession
    spark.udf.register("shingles", shingles_udf)

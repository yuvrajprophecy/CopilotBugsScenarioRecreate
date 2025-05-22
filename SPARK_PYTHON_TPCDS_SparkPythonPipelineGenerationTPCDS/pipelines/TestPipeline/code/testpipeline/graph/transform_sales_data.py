from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def transform_sales_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    out = in0\
              .withColumn("TOTAL_CATALOG_AND_STORE_SALES", (col("TOTAL_CATALOG_SALES") + col("TOTAL_STORE_SALES")))\
              .drop("AVG_WEB_SALES")\
              .withColumnRenamed("I_BRAND", "BRAND_NAME")

    if "I_BRAND" not in in0.columns:
        out = in0\
                  .withColumn("TOTAL_CATALOG_AND_STORE_SALES", (col("TOTAL_CATALOG_SALES") + col("TOTAL_STORE_SALES")))\
                  .drop("AVG_WEB_SALES")\
                  .withColumnRenamed("I_BRAND", "BRAND_NAME")\
                  .withColumn("I_BRAND", lit("Default"))

    out = out.withColumnRenamed("I_CLASS", "CLASS")
    out = out.withColumnRenamed("I_CATEGORY", "CATEGORY")

    return out

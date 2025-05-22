from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def WindowFunction_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn(
          "SS_SOLD_DATE_SK",
          row_number()\
            .over(Window\
            .partitionBy(col("I_BRAND"), col("I_CLASS"), col("I_CATEGORY"))\
            .orderBy(col("CS_SOLD_DATE_SK").asc(), col("CS_ITEM_SK").asc(), col("CS_QUANTITY").asc(), col("CS_LIST_PRICE").asc()))
        )\
        .withColumn(
          "SS_ITEM_SK",
          row_number()\
            .over(Window\
            .partitionBy(col("I_BRAND"), col("I_CLASS"), col("I_CATEGORY"))\
            .orderBy(col("CS_SOLD_DATE_SK").asc(), col("CS_ITEM_SK").asc(), col("CS_QUANTITY").asc(), col("CS_LIST_PRICE").asc()))
        )\
        .withColumn(
          "SS_QUANTITY",
          row_number()\
            .over(Window\
            .partitionBy(col("I_BRAND"), col("I_CLASS"), col("I_CATEGORY"))\
            .orderBy(col("CS_SOLD_DATE_SK").asc(), col("CS_ITEM_SK").asc(), col("CS_QUANTITY").asc(), col("CS_LIST_PRICE").asc()))
        )\
        .withColumn("SS_LIST_PRICE", row_number()\
        .over(Window\
        .partitionBy(col("I_BRAND"), col("I_CLASS"), col("I_CATEGORY"))\
        .orderBy(col("CS_SOLD_DATE_SK").asc(), col("CS_ITEM_SK").asc(), col("CS_QUANTITY").asc(), col("CS_LIST_PRICE").asc())))

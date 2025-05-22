from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def select_sales_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("I_BRAND"), 
        col("I_CLASS"), 
        col("I_CATEGORY"), 
        col("CS_SOLD_DATE_SK"), 
        col("CS_ITEM_SK"), 
        col("CS_QUANTITY"), 
        col("CS_LIST_PRICE"), 
        col("SS_SOLD_DATE_SK"), 
        col("SS_ITEM_SK"), 
        col("SS_QUANTITY"), 
        col("SS_LIST_PRICE"), 
        col("WS_SOLD_DATE_SK"), 
        col("WS_ITEM_SK"), 
        col("WS_QUANTITY"), 
        col("WS_LIST_PRICE"), 
        (col("SS_QUANTITY") * col("SS_LIST_PRICE")).alias("SALES_PRICE")
    )

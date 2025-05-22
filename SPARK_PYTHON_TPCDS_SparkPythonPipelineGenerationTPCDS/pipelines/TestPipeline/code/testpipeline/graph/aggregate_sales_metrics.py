from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def aggregate_sales_metrics(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("I_CATEGORY"), col("I_CLASS"), col("I_BRAND"))

    return df1.agg(
        max(col("CS_SOLD_DATE_SK")).alias("CS_SOLD_DATE_SK"), 
        sum(col("CS_ITEM_SK")).alias("CS_ITEM_SK"), 
        max(col("CS_QUANTITY")).alias("CS_QUANTITY"), 
        max(col("CS_LIST_PRICE")).alias("CS_LIST_PRICE"), 
        min(col("SS_SOLD_DATE_SK")).alias("SS_SOLD_DATE_SK"), 
        first(col("WS_SOLD_DATE_SK")).alias("WS_SOLD_DATE_SK")
    )

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def sold_between_2018_2019(spark: SparkSession, join_datasets: DataFrame) -> DataFrame:
    return join_datasets.filter(
        (
          (((col("CS_SOLD_DATE_SK") >= lit(2018)) & (col("CS_SOLD_DATE_SK") <= lit(2019))) & ((col("SS_SOLD_DATE_SK") >= lit(2018)) & (col("SS_SOLD_DATE_SK") <= lit(2019))))
          & ((col("WS_SOLD_DATE_SK") >= lit(2018)) & (col("WS_SOLD_DATE_SK") <= lit(2019)))
        )
    )

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def Source_2(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("dbfs:/tmp/e2e/tpcds/store_sales")

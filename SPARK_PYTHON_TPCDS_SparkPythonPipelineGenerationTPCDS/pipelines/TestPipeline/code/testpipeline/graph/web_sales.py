from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def web_sales(spark: SparkSession) -> DataFrame:
    return spark.read.table("`hive_metastore`.`qa_tpcds`.`web_sales`")

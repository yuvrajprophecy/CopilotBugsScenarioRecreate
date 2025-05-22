from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def compare_sales_with_avg(spark: SparkSession, avg_sales_by_category: DataFrame) -> DataFrame:
    return avg_sales_by_category.filter(
        (
          ((col("TOTAL_CATALOG_SALES") > col("AVG_CATALOG_SALES")) & (col("TOTAL_STORE_SALES") > col("AVG_STORE_SALES")))
          & (col("TOTAL_WEB_SALES") > col("AVG_WEB_SALES"))
        )
    )

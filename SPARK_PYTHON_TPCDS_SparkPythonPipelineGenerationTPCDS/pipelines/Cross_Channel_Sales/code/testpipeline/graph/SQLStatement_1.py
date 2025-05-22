from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def SQLStatement_1(spark: SparkSession, calculate_sales: DataFrame) -> (DataFrame):

    try:
        registerUDFs(spark)
    except NameError:
        print("registerUDFs not working")

    calculate_sales.createOrReplaceTempView("calculate_sales")
    df1 = spark.sql(
        "SELECT I_BRAND, I_CLASS, I_CATEGORY, AVG(f3) AVG_CATALOG_SALES, AVG(f4) AVG_STORE_SALES, AVG(f5) AVG_WEB_SALES, SUM(f3) TOTAL_CATALOG_SALES, SUM(f4) TOTAL_STORE_SALES, SUM(f5) TOTAL_WEB_SALES, COUNT(CS_ITEM_SK) TOTAL_CATALOG_SALES_NUM, COUNT(SS_ITEM_SK) TOTAL_STORE_SALES_NUM, COUNT(WS_ITEM_SK) TOTAL_WEB_SALES_NUM\nFROM calculate_sales\nGROUP BY I_BRAND, I_CLASS, I_CATEGORY"
    )

    return df1

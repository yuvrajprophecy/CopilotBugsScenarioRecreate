from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def calculate_sales(spark: SparkSession, sold_between_2018_2019: DataFrame) -> (DataFrame):

    try:
        registerUDFs(spark)
    except NameError:
        print("registerUDFs not working")

    sold_between_2018_2019.createOrReplaceTempView("sold_between_2018_2019")
    df1 = spark.sql(
        "SELECT I_BRAND, I_CLASS, I_CATEGORY, CS_QUANTITY * CS_LIST_PRICE as f3, SS_QUANTITY * SS_LIST_PRICE as f4, WS_QUANTITY * WS_LIST_PRICE as f5, CS_ITEM_SK, SS_ITEM_SK, WS_ITEM_SK\nFROM sold_between_2018_2019"
    )

    return df1

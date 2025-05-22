from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def Lookup_0(spark: SparkSession, in0: DataFrame):
    keyColumns = ['''CS_ITEM_SK''', '''CS_WAREHOUSE_SK''', '''CS_SHIP_MODE_SK''', '''CS_PROMO_SK''']
    valueColumns = ['''CS_QUANTITY''', '''CS_WHOLESALE_COST''', '''CS_LIST_PRICE''']
    createLookup("CatalogSalesGetPrices", in0, spark, keyColumns, valueColumns)

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from testpipeline.udfs.UDFs import *

def Reformat_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
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
        col("I_CLASS_ID"), 
        col("CS_BILL_CUSTOMER_SK"), 
        col("CS_SHIP_DATE_SK"), 
        col("CS_SHIP_CDEMO_SK"), 
        col("CS_SHIP_CUSTOMER_SK"), 
        col("SS_HDEMO_SK"), 
        col("SS_CDEMO_SK"), 
        col("SS_ADDR_SK"), 
        col("SS_STORE_SK"), 
        col("SS_TICKET_NUMBER"), 
        col("SS_SALES_PRICE"), 
        col("SS_EXT_DISCOUNT_AMT"), 
        col("SS_EXT_SALES_PRICE"), 
        col("SS_EXT_WHOLESALE_COST"), 
        col("SS_EXT_TAX"), 
        col("WS_BILL_HDEMO_SK"), 
        col("WS_BILL_ADDR_SK"), 
        col("WS_EXT_WHOLESALE_COST"), 
        col("WS_EXT_LIST_PRICE"), 
        col("WS_EXT_TAX"), 
        col("WS_COUPON_AMT"), 
        col("WS_EXT_SHIP_COST"), 
        col("WS_NET_PAID"), 
        array(col("SS_SALES_PRICE"), col("SS_STORE_SK"), col("SS_LIST_PRICE")).alias("ALL_STORE_SALES_PRICES"), 
        array(col("WS_EXT_TAX"), col("WS_BILL_HDEMO_SK"), col("WS_EXT_WHOLESALE_COST"), col("WS_EXT_LIST_PRICE"))\
          .alias("ALL_WEB_SALES_PRICES")
    )

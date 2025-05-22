from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def join_multiple_dataframes(spark: SparkSession, in0: DataFrame, in1: DataFrame, in2: DataFrame) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.I_BRAND") == col("in1.BRAND_NAME")), "right_outer")\
        .join(in2.alias("in2"), (col("in1.CATEGORY") == col("in2.I_CATEGORY")), "left_outer")\
        .select(col("in0.STORE_SALES_PRICES").alias("STORE_SALES_PRICES"), col("in0.WEB_SALES_PRICES").alias("WEB_SALES_PRICES"), col("in0.I_BRAND").alias("I_BRAND"), col("in0.I_CLASS").alias("I_CLASS"), col("in0.I_CATEGORY").alias("I_CATEGORY"), col("in0.CS_ITEM_SK").alias("CS_ITEM_SK"), col("in0.CS_QUANTITY").alias("CS_QUANTITY"), col("in0.CS_LIST_PRICE").alias("CS_LIST_PRICE"), col("in0.SS_SOLD_DATE_SK").alias("SS_SOLD_DATE_SK"), col("in0.SS_ITEM_SK").alias("SS_ITEM_SK"), col("in0.SS_QUANTITY").alias("SS_QUANTITY"), col("in0.SS_LIST_PRICE").alias("SS_LIST_PRICE"), col("in0.WS_SOLD_DATE_SK").alias("WS_SOLD_DATE_SK"), col("in0.WS_ITEM_SK").alias("WS_ITEM_SK"), col("in0.WS_QUANTITY").alias("WS_QUANTITY"), col("in0.WS_LIST_PRICE").alias("WS_LIST_PRICE"), col("in0.I_CLASS_ID").alias("I_CLASS_ID"), col("in0.CS_BILL_CUSTOMER_SK").alias("CS_BILL_CUSTOMER_SK"), col("in0.CS_SHIP_DATE_SK").alias("CS_SHIP_DATE_SK"), col("in0.CS_SHIP_CDEMO_SK").alias("CS_SHIP_CDEMO_SK"), col("in0.CS_SHIP_CUSTOMER_SK").alias("CS_SHIP_CUSTOMER_SK"), col("in0.SS_HDEMO_SK").alias("SS_HDEMO_SK"), col("in0.SS_CDEMO_SK").alias("SS_CDEMO_SK"), col("in0.SS_ADDR_SK").alias("SS_ADDR_SK"), col("in0.SS_STORE_SK").alias("SS_STORE_SK"), col("in0.SS_TICKET_NUMBER").alias("SS_TICKET_NUMBER"), col("in0.SS_SALES_PRICE").alias("SS_SALES_PRICE"), col("in0.SS_EXT_DISCOUNT_AMT").alias("SS_EXT_DISCOUNT_AMT"), col("in0.SS_EXT_SALES_PRICE").alias("SS_EXT_SALES_PRICE"), col("in0.SS_EXT_WHOLESALE_COST").alias("SS_EXT_WHOLESALE_COST"), col("in0.SS_EXT_TAX").alias("SS_EXT_TAX"), col("in0.WS_BILL_HDEMO_SK").alias("WS_BILL_HDEMO_SK"), col("in0.WS_BILL_ADDR_SK").alias("WS_BILL_ADDR_SK"), col("in0.WS_EXT_WHOLESALE_COST").alias("WS_EXT_WHOLESALE_COST"), col("in0.WS_EXT_LIST_PRICE").alias("WS_EXT_LIST_PRICE"), col("in0.WS_EXT_TAX").alias("WS_EXT_TAX"), col("in0.WS_COUPON_AMT").alias("WS_COUPON_AMT"), col("in0.WS_EXT_SHIP_COST").alias("WS_EXT_SHIP_COST"), col("in0.WS_NET_PAID").alias("WS_NET_PAID"), col("in1.TOTAL_STORE_SALES_NUM").alias("TOTAL_STORE_SALES_NUM"), col("in2.CS_SOLD_DATE_SK").alias("CS_SOLD_DATE_SK"))

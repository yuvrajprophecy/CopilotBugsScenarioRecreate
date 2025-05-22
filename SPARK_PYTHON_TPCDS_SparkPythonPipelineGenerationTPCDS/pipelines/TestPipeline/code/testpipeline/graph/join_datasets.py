from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def join_datasets(
        spark: SparkSession,
        item: DataFrame,
        catalog_sales: DataFrame,
        store_sales: DataFrame, 
        web_sales: DataFrame
) -> DataFrame:
    return item\
        .alias("item")\
        .join(catalog_sales.alias("catalog_sales"), (col("item.I_ITEM_SK") == col("catalog_sales.CS_ITEM_SK")), "inner")\
        .join(store_sales.alias("store_sales"), (col("item.I_ITEM_SK") == col("store_sales.SS_ITEM_SK")), "inner")\
        .join(web_sales.alias("web_sales"), (col("item.I_ITEM_SK") == col("web_sales.WS_ITEM_SK")), "inner")\
        .select(col("item.I_BRAND").alias("I_BRAND"), col("item.I_CLASS").alias("I_CLASS"), col("item.I_CATEGORY").alias("I_CATEGORY"), col("catalog_sales.CS_SOLD_DATE_SK").alias("CS_SOLD_DATE_SK"), col("catalog_sales.CS_ITEM_SK").alias("CS_ITEM_SK"), col("catalog_sales.CS_QUANTITY").alias("CS_QUANTITY"), col("catalog_sales.CS_LIST_PRICE").alias("CS_LIST_PRICE"), col("store_sales.SS_SOLD_DATE_SK").alias("SS_SOLD_DATE_SK"), col("store_sales.SS_ITEM_SK").alias("SS_ITEM_SK"), col("store_sales.SS_QUANTITY").alias("SS_QUANTITY"), col("store_sales.SS_LIST_PRICE").alias("SS_LIST_PRICE"), col("web_sales.WS_SOLD_DATE_SK").alias("WS_SOLD_DATE_SK"), col("web_sales.WS_ITEM_SK").alias("WS_ITEM_SK"), col("web_sales.WS_QUANTITY").alias("WS_QUANTITY"), col("web_sales.WS_LIST_PRICE").alias("WS_LIST_PRICE"), col("item.I_CLASS_ID").alias("I_CLASS_ID"), col("catalog_sales.CS_BILL_CUSTOMER_SK").alias("CS_BILL_CUSTOMER_SK"), col("catalog_sales.CS_SHIP_DATE_SK").alias("CS_SHIP_DATE_SK"), col("catalog_sales.CS_SHIP_CDEMO_SK").alias("CS_SHIP_CDEMO_SK"), col("catalog_sales.CS_SHIP_CUSTOMER_SK").alias("CS_SHIP_CUSTOMER_SK"), col("store_sales.SS_HDEMO_SK").alias("SS_HDEMO_SK"), col("store_sales.SS_CDEMO_SK").alias("SS_CDEMO_SK"), col("store_sales.SS_ADDR_SK").alias("SS_ADDR_SK"), col("store_sales.SS_STORE_SK").alias("SS_STORE_SK"), col("store_sales.SS_TICKET_NUMBER").alias("SS_TICKET_NUMBER"), col("store_sales.SS_SALES_PRICE").alias("SS_SALES_PRICE"), col("store_sales.SS_EXT_DISCOUNT_AMT").alias("SS_EXT_DISCOUNT_AMT"), col("store_sales.SS_EXT_SALES_PRICE").alias("SS_EXT_SALES_PRICE"), col("store_sales.SS_EXT_WHOLESALE_COST").alias("SS_EXT_WHOLESALE_COST"), col("store_sales.SS_EXT_LIST_PRICE").alias("SS_EXT_LIST_PRICE"), col("store_sales.SS_EXT_LIST_PRICE").alias("SS_EXT_LIST_PRICE"), col("store_sales.SS_EXT_TAX").alias("SS_EXT_TAX"), col("web_sales.WS_BILL_HDEMO_SK").alias("WS_BILL_HDEMO_SK"), col("web_sales.WS_BILL_ADDR_SK").alias("WS_BILL_ADDR_SK"), col("web_sales.WS_EXT_WHOLESALE_COST").alias("WS_EXT_WHOLESALE_COST"), col("web_sales.WS_EXT_LIST_PRICE").alias("WS_EXT_LIST_PRICE"), col("web_sales.WS_EXT_TAX").alias("WS_EXT_TAX"), col("web_sales.WS_COUPON_AMT").alias("WS_COUPON_AMT"), col("web_sales.WS_EXT_SHIP_COST").alias("WS_EXT_SHIP_COST"), col("web_sales.WS_NET_PAID").alias("WS_NET_PAID"))

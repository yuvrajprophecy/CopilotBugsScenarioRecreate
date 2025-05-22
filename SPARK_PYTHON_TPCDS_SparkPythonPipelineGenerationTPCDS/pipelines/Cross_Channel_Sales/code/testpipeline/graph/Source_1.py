from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def Source_1(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("CS_SOLD_DATE_SK", DecimalType(38, 0), True), StructField("CS_SOLD_TIME_SK", DecimalType(38, 0), True), StructField("CS_SHIP_DATE_SK", DecimalType(38, 0), True), StructField("CS_BILL_CUSTOMER_SK", DecimalType(38, 0), True), StructField("CS_BILL_CDEMO_SK", DecimalType(38, 0), True), StructField("CS_BILL_HDEMO_SK", DecimalType(38, 0), True), StructField("CS_BILL_ADDR_SK", DecimalType(38, 0), True), StructField("CS_SHIP_CUSTOMER_SK", DecimalType(38, 0), True), StructField("CS_SHIP_CDEMO_SK", DecimalType(38, 0), True), StructField("CS_SHIP_HDEMO_SK", DecimalType(38, 0), True), StructField("CS_SHIP_ADDR_SK", DecimalType(38, 0), True), StructField("CS_CALL_CENTER_SK", DecimalType(38, 0), True), StructField("CS_CATALOG_PAGE_SK", DecimalType(38, 0), True), StructField("CS_SHIP_MODE_SK", DecimalType(38, 0), True), StructField("CS_WAREHOUSE_SK", DecimalType(38, 0), True), StructField("CS_ITEM_SK", DecimalType(38, 0), True), StructField("CS_PROMO_SK", DecimalType(38, 0), True), StructField("CS_ORDER_NUMBER", DecimalType(38, 0), True), StructField("CS_QUANTITY", DecimalType(38, 0), True), StructField("CS_WHOLESALE_COST", DecimalType(7, 2), True), StructField("CS_LIST_PRICE", DecimalType(7, 2), True), StructField("CS_SALES_PRICE", DecimalType(7, 2), True), StructField("CS_EXT_DISCOUNT_AMT", DecimalType(7, 2), True), StructField("CS_EXT_SALES_PRICE", DecimalType(7, 2), True), StructField("CS_EXT_WHOLESALE_COST", DecimalType(7, 2), True), StructField("CS_EXT_LIST_PRICE", DecimalType(7, 2), True), StructField("CS_EXT_TAX", DecimalType(7, 2), True), StructField("CS_COUPON_AMT", DecimalType(7, 2), True), StructField("CS_EXT_SHIP_COST", DecimalType(7, 2), True), StructField("CS_NET_PAID", DecimalType(7, 2), True), StructField("CS_NET_PAID_INC_TAX", DecimalType(7, 2), True), StructField("CS_NET_PAID_INC_SHIP", DecimalType(7, 2), True), StructField("CS_NET_PAID_INC_SHIP_TAX", DecimalType(7, 2), True), StructField("CS_NET_PROFIT", DecimalType(7, 2), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/tmp/e2e/tpcds/catalog_sales")

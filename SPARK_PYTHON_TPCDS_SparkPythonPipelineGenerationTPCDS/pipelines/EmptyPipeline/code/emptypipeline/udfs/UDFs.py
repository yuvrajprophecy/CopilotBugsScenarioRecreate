from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.lookups import (
    createLookup,
    createRangeLookup,
    lookup,
    lookup_last,
    lookup_match,
    lookup_count,
    lookup_row,
    lookup_row_reverse,
    lookup_nth
)

def registerUDFs(spark: SparkSession):
    spark.udf.register("sanitize_string", sanitize_string)
    spark.udf.register("sanitize_numeric", sanitize_numeric)
    

    try:
        from prophecy.utils import ScalaUtil
        ScalaUtil.initializeUDFs(spark)
    except :
        pass

def sanitize_stringGenerator():
    data = "text"

    @udf(returnType = StringType())
    def func(input):
        return f"{input}_{data}"

    return func

sanitize_string = sanitize_stringGenerator()

def sanitize_numericGenerator():
    int_val = 22

    @udf(returnType = IntegerType())
    def func(input):
        input = int(input) if input is not None else 2

        return int(input) * int(input) if input is not None else int_val

    return func

sanitize_numeric = sanitize_numericGenerator()

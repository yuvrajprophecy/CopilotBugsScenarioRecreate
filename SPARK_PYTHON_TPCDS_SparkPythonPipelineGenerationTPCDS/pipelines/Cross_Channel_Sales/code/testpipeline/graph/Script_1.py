from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def Script_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    out0 = in0.filter("I_BRAND".rlike("COS")).groupBy('I_CLASS').agg({'CS_QUANTITY' : 'sum'})

    return out0

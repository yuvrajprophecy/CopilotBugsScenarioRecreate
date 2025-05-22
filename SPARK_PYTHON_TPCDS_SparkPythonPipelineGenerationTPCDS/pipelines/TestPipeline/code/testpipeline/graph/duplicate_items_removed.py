from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def duplicate_items_removed(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.dropDuplicates(["I_CATEGORY", "I_CLASS", "I_BRAND"])

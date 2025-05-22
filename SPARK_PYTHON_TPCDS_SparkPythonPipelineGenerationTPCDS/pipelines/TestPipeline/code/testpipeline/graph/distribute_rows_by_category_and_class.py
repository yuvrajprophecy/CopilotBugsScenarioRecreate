from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def distribute_rows_by_category_and_class(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):
    df1 = in0.filter(col("I_CATEGORY").isNotNull())
    df2 = in0.filter(col("I_CLASS").isNotNull())

    return df1, df2

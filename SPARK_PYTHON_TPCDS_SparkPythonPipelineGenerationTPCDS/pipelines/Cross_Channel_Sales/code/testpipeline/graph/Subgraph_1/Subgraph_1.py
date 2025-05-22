from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from testpipeline.udfs.UDFs import *
from . import *
from .config import *

def Subgraph_1(
        spark: SparkSession,
        subgraph_config: SubgraphConfig,
        in0: DataFrame,
        join_datasets0: DataFrame
) -> (DataFrame, DataFrame):
    Config.update(subgraph_config)
    df_Reformat_2 = Reformat_2(spark, in0)
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_Reformat_2)
    df_Repartition_1 = Repartition_1(spark, join_datasets0)
    df_sold_between_2018_2019 = sold_between_2018_2019(spark, df_Repartition_1)
    df_calculate_sales = calculate_sales(spark, df_sold_between_2018_2019)
    subgraph_config.update(Config)

    return df_FlattenSchema_1, df_calculate_sales

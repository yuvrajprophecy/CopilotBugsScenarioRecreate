from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *
from prophecy.utils import *
from testpipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_catalog_sales_1 = catalog_sales_1(spark)
    Lookup_0(spark, df_catalog_sales_1)
    df_web_sales = web_sales(spark)
    df_Source_2 = Source_2(spark)
    df_item = item(spark)
    df_Source_1 = Source_1(spark)
    df_Join_1 = Join_1(spark, df_item, df_Source_1, df_Source_2, df_web_sales)
    df_WindowFunction_1 = WindowFunction_1(spark, df_Join_1)
    df_Reformat_1 = Reformat_1(spark, df_Join_1)
    df_Subgraph_1_out, df_Subgraph_1_out0 = Subgraph_1(spark, Config.Subgraph_1, df_WindowFunction_1, df_Reformat_1)
    df_Script_1 = Script_1(spark, df_Subgraph_1_out)
    df_SQLStatement_1 = SQLStatement_1(spark, df_Subgraph_1_out0)
    df_Filter_1 = Filter_1(spark, df_SQLStatement_1)
    df_OrderBy_1 = OrderBy_1(spark, df_Filter_1)
    df_SchemaTransform_1 = SchemaTransform_1(spark, df_OrderBy_1)
    df_Limit_1 = Limit_1(spark, df_Join_1)
    df_Aggregate_1 = Aggregate_1(spark, df_Limit_1)
    df_Deduplicate_1 = Deduplicate_1(spark, df_Aggregate_1)
    df_Repartition_4 = Repartition_4(spark, df_Deduplicate_1)
    df_RowDistributor_1_out0, df_RowDistributor_1_out1 = RowDistributor_1(spark, df_Repartition_4)
    df_SetOperation_1 = SetOperation_1(spark, df_RowDistributor_1_out0, df_RowDistributor_1_out1)
    df_multiple_dataframes_join = multiple_dataframes_join(spark, df_Script_1, df_SchemaTransform_1, df_SetOperation_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("TestPipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Cross_Channel_Sales")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Cross_Channel_Sales", config = Config)(pipeline)

if __name__ == "__main__":
    main()

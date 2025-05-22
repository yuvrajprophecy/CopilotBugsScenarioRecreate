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
    df_store_sales = store_sales(spark)
    df_item = item(spark)
    df_catalog_sales = catalog_sales(spark)
    df_join_datasets = join_datasets(spark, df_item, df_catalog_sales, df_store_sales, df_web_sales)
    df_sales_ranking_by_product = sales_ranking_by_product(spark, df_join_datasets)
    df_reformat_sales_data = reformat_sales_data(spark, df_sales_ranking_by_product)
    df_flatten_sales_data = flatten_sales_data(spark, df_reformat_sales_data)
    df_aggregate_quantity_by_class = aggregate_quantity_by_class(spark, df_flatten_sales_data)
    df_select_sales_data = select_sales_data(spark, df_join_datasets)
    df_sold_between_2018_2019 = sold_between_2018_2019(spark, df_select_sales_data)
    df_calculate_sales = calculate_sales(spark, df_sold_between_2018_2019)
    df_avg_sales_by_category = avg_sales_by_category(spark, df_calculate_sales)
    df_compare_sales_with_avg = compare_sales_with_avg(spark, df_avg_sales_by_category)
    df_OrderBy_1 = OrderBy_1(spark, df_compare_sales_with_avg)
    df_transform_sales_data = transform_sales_data(spark, df_OrderBy_1)
    df_Limit_1 = Limit_1(spark, df_join_datasets)
    df_aggregate_sales_metrics = aggregate_sales_metrics(spark, df_Limit_1)
    df_duplicate_items_removed = duplicate_items_removed(spark, df_aggregate_sales_metrics)
    df_Repartition_1 = Repartition_1(spark, df_duplicate_items_removed)
    df_distribute_rows_by_category_and_class_out0, df_distribute_rows_by_category_and_class_out1 = distribute_rows_by_category_and_class(
        spark, 
        df_Repartition_1
    )
    df_SetOperation_1 = SetOperation_1(
        spark, 
        df_distribute_rows_by_category_and_class_out0, 
        df_distribute_rows_by_category_and_class_out1
    )
    df_join_multiple_dataframes = join_multiple_dataframes(
        spark, 
        df_aggregate_quantity_by_class, 
        df_transform_sales_data, 
        df_SetOperation_1
    )

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("TestPipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/TestPipeline")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/TestPipeline", config = Config)(pipeline)

if __name__ == "__main__":
    main()

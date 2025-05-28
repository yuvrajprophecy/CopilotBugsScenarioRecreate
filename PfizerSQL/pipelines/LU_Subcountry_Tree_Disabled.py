Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_LU_Subcountry_Tree_Disabled_aka_GPDIP_EDLUD_346 = Task(
        task_id = "model_LU_Subcountry_Tree_Disabled_aka_GPDIP_EDLUD_346", 
        component = "Model", 
        modelName = "model_LU_Subcountry_Tree_Disabled_aka_GPDIP_EDLUD_346"
    )
    OrchestrationSource_1 = Task(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        format = {"properties" : {}}
    )
    model_LU_Subcountry_Tree_Disabled_Sort_266 = Task(
        task_id = "model_LU_Subcountry_Tree_Disabled_Sort_266", 
        component = "Model", 
        modelName = "model_LU_Subcountry_Tree_Disabled_Sort_266"
    )
    model_LU_Subcountry_Tree_Disabled_DataCleansing_1 = Task(
        task_id = "model_LU_Subcountry_Tree_Disabled_DataCleansing_1", 
        component = "Model", 
        modelName = "model_LU_Subcountry_Tree_Disabled_DataCleansing_1"
    )
    OrchestrationSource_2 = SourceTask(
        task_id = "OrchestrationSource_2", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(allowEmptyColumnNames = True, header = True, nullValue = "", separator = ",")
    )
    (
        model_LU_Subcountry_Tree_Disabled_aka_GPDIP_EDLUD_346.out_1
        >> [model_LU_Subcountry_Tree_Disabled_Sort_266.in_1, model_LU_Subcountry_Tree_Disabled_DataCleansing_1.in_1]
    )

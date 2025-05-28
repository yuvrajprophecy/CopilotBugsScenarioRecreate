Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_tanmay_test_AlteryxSelect_327 = Task(
        task_id = "model_tanmay_test_AlteryxSelect_327", 
        component = "Model", 
        modelName = "model_tanmay_test_AlteryxSelect_327"
    )
    AKA_GPDIP_EDLUD_302 = SourceTask(
        task_id = "AKA_GPDIP_EDLUD_302", 
        component = "OrchestrationSource", 
        kind = "OracleSource", 
        connector = Connection(kind = "oracle", id = "oracle-test"), 
        format = ORACLEFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "r_object_id"},                         {"dataType" : {"type" : "decimal"}, "name" : "i_position"},                         {"dataType" : {"type" : "utf8"}, "name" : "name"},                         {"dataType" : {"type" : "decimal"}, "name" : "value"}], 
            "providerType": "arrow"
          }
        ), 
        pathSelection = "warehouseQuery", 
        tableFullName = {"database" : "default", "name" : "AKA_GPDIP_EDLUD_302", "schema" : "DEMOS"}, 
        warehouseQuery = {"query" : "SELECT * FROM DEMOS.AKA_GPDIP_EDLUD_302 FETCH FIRST 1000 ROWS ONLY"}
    )
    AKA_GPDIP_EDLUD_302 = Task(
        task_id = "AKA_GPDIP_EDLUD_302", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_tanmay_test_pre_Filter_303_reject_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_tanmay_test_source", 
          "alias": ""
        }
    )
    ORACLE_LARGE_AKA_GPDIP_EDLUD_289 = SourceTask(
        task_id = "ORACLE_LARGE_AKA_GPDIP_EDLUD_289", 
        component = "OrchestrationSource", 
        kind = "OracleSource", 
        connector = Connection(kind = "oracle", id = "oracle-test"), 
        format = ORACLEFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "is_static"},                         {"dataType" : {"type" : "utf8"}, "name" : "extract_date"},                         {"dataType" : {"type" : "utf8"}, "name" : "product_name"},                         {"dataType" : {"type" : "utf8"}, "name" : "country_abbreviation"},                         {"dataType" : {"type" : "decimal"}, "name" : "app_country_id"},                         {"dataType" : {"type" : "utf8"}, "name" : "country_name"},                         {"dataType" : {"type" : "utf8"}, "name" : "is_active"}], 
            "providerType": "arrow"
          }
        ), 
        pathSelection = "tableFullName", 
        tableFullName = {"database" : "default", "name" : "ORACLE_LARGE_AKA_GPDIP_EDLUD_289", "schema" : "DEMOS"}, 
        warehouseQuery = {}
    )
    model_tanmay_test_Summarize_305 = Task(
        task_id = "model_tanmay_test_Summarize_305", 
        component = "Model", 
        modelName = "model_tanmay_test_Summarize_305"
    )
    AKA_GPDIP_EDLUD_302.out0 >> AKA_GPDIP_EDLUD_302.input_port_0_1
    (
        AKA_GPDIP_EDLUD_302.output_port_0_1
        >> [model_tanmay_test_Summarize_305.in_0, model_tanmay_test_AlteryxSelect_327.in_0]
    )

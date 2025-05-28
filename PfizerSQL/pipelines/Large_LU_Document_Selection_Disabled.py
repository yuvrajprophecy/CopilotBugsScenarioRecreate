Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    AKA_GPDIP_EDLUD_302 = Task(
        task_id = "AKA_GPDIP_EDLUD_302", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_Large_LU_Document_Selection_Disabled_pre_Filter_303_reject_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_Large_LU_Document_Selection_Disabled_source", 
          "alias": ""
        }
    )
    LARGE_AKA_GPDIP_EDLUD_298_1 = Task(
        task_id = "LARGE_AKA_GPDIP_EDLUD_298_1", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_Large_LU_Document_Selection_Disabled_pre_Join_299_inner_1", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_Large_LU_Document_Selection_Disabled_source", 
          "alias": ""
        }
    )
    LARGE_AKA_GPDIP_EDLUD_324 = Task(
        task_id = "LARGE_AKA_GPDIP_EDLUD_324", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_Large_LU_Document_Selection_Disabled_pre_Filter_323_reject_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_Large_LU_Document_Selection_Disabled_source", 
          "alias": ""
        }
    )
    LARGE_AKA_GPDIP_EDLUD_312 = Task(
        task_id = "LARGE_AKA_GPDIP_EDLUD_312", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_Large_LU_Document_Selection_Disabled_pre_Join_313_inner_1", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_Large_LU_Document_Selection_Disabled_source", 
          "alias": ""
        }
    )
    document_metadata_redshift = Task(
        task_id = "document_metadata_redshift", 
        component = "OrchestrationTarget", 
        kind = "RedshiftTarget", 
        connector = Connection(kind = "redshift", id = "RedShiftTest"), 
        format = {
          "category": "table", 
          "kind": "redshift", 
          "properties": {"kind" : "redshift", "properties" : {}, "writeMode" : "overwrite"}
        }, 
        isNew = False, 
        properties = {
          "tableFullName": {
            "database": {
              "type": "concat_operation", 
              "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "prophecy"}}]}
            }, 
            "schema": {
              "type": "concat_operation", 
              "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "dummy"}}]}
            }, 
            "name": {
              "type": "concat_operation", 
              "properties": {
                "elements": [{"type" : "literal", "properties" : {"value" : "large_flu_document_Selection_Disabled"}}]
              }
            }
          }
        }
    )
    model_Large_LU_Document_Selection_Disabled_Join_310_inner = Task(
        task_id = "model_Large_LU_Document_Selection_Disabled_Join_310_inner", 
        component = "Model", 
        modelName = "model_Large_LU_Document_Selection_Disabled_Join_310_inner"
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
    LARGE_AKA_GPDIP_EDLUD_298_1 = SourceTask(
        task_id = "LARGE_AKA_GPDIP_EDLUD_298_1", 
        component = "OrchestrationSource", 
        kind = "OracleSource", 
        connector = Connection(kind = "oracle", id = "oracle-test"), 
        format = ORACLEFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "i_has_folder"},                         {"dataType" : {"type" : "utf8"}, "name" : "xm_language"},                         {"dataType" : {"type" : "utf8"}, "name" : "r_object_id"},                         {"dataType" : {"type" : "utf8"}, "name" : "title"},                         {"dataType" : {"type" : "utf8"}, "name" : "i_chronicle_id"},                         {"dataType" : {"type" : "utf8"}, "name" : "xm_status"},                         {"dataType" : {"type" : "utf8"}, "name" : "object_name"},                         {"dataType" : {"type" : "utf8"}, "name" : "subtype"}], 
            "providerType": "arrow"
          }
        ), 
        pathSelection = "tableFullName", 
        tableFullName = {"database" : "default", "name" : "LARGE_AKA_GPDIP_EDLUD_298", "schema" : "DEMOS"}, 
        warehouseQuery = {}
    )
    LARGE_AKA_GPDIP_EDLUD_324 = SourceTask(
        task_id = "LARGE_AKA_GPDIP_EDLUD_324", 
        component = "OrchestrationSource", 
        kind = "OracleSource", 
        connector = Connection(kind = "oracle", id = "oracle-test"), 
        format = ORACLEFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "r_object_id"},                         {"dataType" : {"type" : "decimal"}, "name" : "i_position"},                         {"dataType" : {"type" : "utf8"}, "name" : "name"},                         {"dataType" : {"type" : "decimal"}, "name" : "value"}], 
            "providerType": "arrow"
          }
        ), 
        pathSelection = "tableFullName", 
        tableFullName = {"database" : "default", "name" : "LARGE_AKA_GPDIP_EDLUD_324", "schema" : "DEMOS"}, 
        warehouseQuery = {}
    )
    ORACLE_LARGE_AKA_GPDIP_EDLUD_289 = Task(
        task_id = "ORACLE_LARGE_AKA_GPDIP_EDLUD_289", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_Large_LU_Document_Selection_Disabled_pre_Cleanse_290_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_Large_LU_Document_Selection_Disabled_source", 
          "alias": ""
        }
    )
    model_Large_LU_Document_Selection_Disabled_Join_318_inner = Task(
        task_id = "model_Large_LU_Document_Selection_Disabled_Join_318_inner", 
        component = "Model", 
        modelName = "model_Large_LU_Document_Selection_Disabled_Join_318_inner"
    )
    model_Large_LU_Document_Selection_Disabled_Cleanse_290 = Task(
        task_id = "model_Large_LU_Document_Selection_Disabled_Cleanse_290", 
        component = "Model", 
        modelName = "model_Large_LU_Document_Selection_Disabled_Cleanse_290"
    )
    LARGE_AKA_GPDIP_EDLUD_312 = SourceTask(
        task_id = "LARGE_AKA_GPDIP_EDLUD_312", 
        component = "OrchestrationSource", 
        kind = "OracleSource", 
        connector = Connection(kind = "oracle", id = "oracle-test"), 
        format = ORACLEFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "subtype"},                         {"dataType" : {"type" : "utf8"}, "name" : "object_name"},                         {"dataType" : {"type" : "utf8"}, "name" : "xm_status"},                         {"dataType" : {"type" : "utf8"}, "name" : "i_has_folder"},                         {"dataType" : {"type" : "utf8"}, "name" : "xm_language"},                         {"dataType" : {"type" : "utf8"}, "name" : "r_object_id"},                         {"dataType" : {"type" : "utf8"}, "name" : "title"},                         {"dataType" : {"type" : "utf8"}, "name" : "i_chronicle_id"}], 
            "providerType": "arrow"
          }
        ), 
        pathSelection = "tableFullName", 
        tableFullName = {"database" : "default", "name" : "LARGE_AKA_GPDIP_EDLUD_312", "schema" : "DEMOS"}, 
        warehouseQuery = {}
    )
    model_Large_LU_Document_Selection_Disabled_AlteryxSelect_294 = Task(
        task_id = "model_Large_LU_Document_Selection_Disabled_AlteryxSelect_294", 
        component = "Model", 
        modelName = "model_Large_LU_Document_Selection_Disabled_AlteryxSelect_294"
    )
    LARGE_AKA_GPDIP_EDLUD_324.out0 >> LARGE_AKA_GPDIP_EDLUD_324.input_port_3_1
    ORACLE_LARGE_AKA_GPDIP_EDLUD_289.out0 >> ORACLE_LARGE_AKA_GPDIP_EDLUD_289.input_port_0_1
    AKA_GPDIP_EDLUD_302.out0 >> AKA_GPDIP_EDLUD_302.input_port_2_1
    LARGE_AKA_GPDIP_EDLUD_312.out0 >> LARGE_AKA_GPDIP_EDLUD_312.input_port_7_1
    (
        AKA_GPDIP_EDLUD_302.output_port_2_1
        >> [model_Large_LU_Document_Selection_Disabled_Join_310_inner.in_2,
              model_Large_LU_Document_Selection_Disabled_Join_310_inner.in_3]
    )
    (
        LARGE_AKA_GPDIP_EDLUD_324.output_port_3_1
        >> [model_Large_LU_Document_Selection_Disabled_Join_318_inner.in_2,
              model_Large_LU_Document_Selection_Disabled_Join_318_inner.in_3]
    )
    model_Large_LU_Document_Selection_Disabled_AlteryxSelect_294.out_0 >> document_metadata_redshift.in0
    (
        model_Large_LU_Document_Selection_Disabled_Cleanse_290.out_0
        >> [model_Large_LU_Document_Selection_Disabled_Join_310_inner.in_0,
              model_Large_LU_Document_Selection_Disabled_Join_318_inner.in_0]
    )
    (
        model_Large_LU_Document_Selection_Disabled_Join_310_inner.out_0
        >> model_Large_LU_Document_Selection_Disabled_AlteryxSelect_294.in_0
    )
    LARGE_AKA_GPDIP_EDLUD_298_1.output_port_5_1 >> model_Large_LU_Document_Selection_Disabled_AlteryxSelect_294.in_1
    (
        model_Large_LU_Document_Selection_Disabled_Join_318_inner.out_0
        >> model_Large_LU_Document_Selection_Disabled_AlteryxSelect_294.in_0
    )
    LARGE_AKA_GPDIP_EDLUD_312.output_port_7_1 >> model_Large_LU_Document_Selection_Disabled_AlteryxSelect_294.in_3
    LARGE_AKA_GPDIP_EDLUD_298_1.out0 >> LARGE_AKA_GPDIP_EDLUD_298_1.input_port_5_1
    ORACLE_LARGE_AKA_GPDIP_EDLUD_289.output_port_0_1 >> model_Large_LU_Document_Selection_Disabled_Cleanse_290.in_0

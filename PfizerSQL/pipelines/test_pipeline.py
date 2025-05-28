Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    aka_GPDIP_EDLUD_289 = Task(
        task_id = "aka_GPDIP_EDLUD_289", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_test_pipeline_pre_Cleanse_290_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_test_pipeline_source", 
          "alias": ""
        }
    )
    aka_GPDIP_EDLUD_302 = SourceTask(
        task_id = "aka_GPDIP_EDLUD_302", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = {
          "id": "transpiled_connection", 
          "kind": "databricks", 
          "properties": {
            "authMethod": "password", 
            "username": "transpiled_username", 
            "host": "sftp.prophecy.io", 
            "id": "dev-test", 
            "port": 22, 
            "password": {
              "kind": "prophecy", 
              "properties": {"name" : "transpiled_secret", "value" : "transpiled_secret"}, 
              "subKind": "text", 
              "type": "secret"
            }
          }, 
          "type": "connector"
        }, 
        format = DATABRICKSFormat(kind = "databricks", properties = {}), 
        tableFullName = {
          "database": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "main"}}]}
          }, 
          "schema": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "rishabh"}}]}
          }, 
          "name": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "aka_GPDIP_EDLUD_302"}}]}
          }
        }
    )
    aka_GPDIP_EDLUD_312 = SourceTask(
        task_id = "aka_GPDIP_EDLUD_312", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = {
          "kind": "sftp", 
          "id": "transpiled_connection", 
          "properties": {
            "authMethod": "password", 
            "username": "transpiled_username", 
            "host": "sftp.prophecy.io", 
            "id": "transpiled_connection", 
            "port": 22, 
            "password": {
              "kind": "prophecy", 
              "properties": {"name" : "transpiled_secret", "value" : "transpiled_secret"}, 
              "subKind": "text", 
              "type": "secret"
            }
          }, 
          "type": "connector"
        }, 
        format = XLSXFormat(
          schema = {
            "providerType": "Databricks", 
            "fields": [{"name" : "subtype", "dataType" : {"type" : "utf8"}},                         {"name" : "object_name", "dataType" : {"type" : "utf8"}},                         {"name" : "xm_status", "dataType" : {"type" : "utf8"}},                         {"name" : "i_has_folder", "dataType" : {"type" : "int32"}},                         {"name" : "xm_language", "dataType" : {"type" : "utf8"}},                         {"name" : "r_object_id", "dataType" : {"type" : "utf8"}},                         {"name" : "title", "dataType" : {"type" : "utf8"}},                         {"name" : "i_chronicle_id", "dataType" : {"type" : "utf8"}}]
          }
        ), 
        filePath = "aka_GPDIP_EDLUD_312.xlsx"
    )
    aka_GPDIP_EDLUD_298 = Task(
        task_id = "aka_GPDIP_EDLUD_298", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_test_pipeline_pre_Join_299_inner_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_test_pipeline_source", 
          "alias": ""
        }
    )
    aka_GPDIP_EDLUD_324 = SourceTask(
        task_id = "aka_GPDIP_EDLUD_324", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = {
          "kind": "sftp", 
          "id": "transpiled_connection", 
          "properties": {
            "authMethod": "password", 
            "username": "transpiled_username", 
            "host": "sftp.prophecy.io", 
            "id": "transpiled_connection", 
            "port": 22, 
            "password": {
              "kind": "prophecy", 
              "properties": {"name" : "transpiled_secret", "value" : "transpiled_secret"}, 
              "subKind": "text", 
              "type": "secret"
            }
          }, 
          "type": "connector"
        }, 
        format = XLSXFormat(
          schema = {
            "providerType": "Databricks", 
            "fields": [{"name" : "r_object_id", "dataType" : {"type" : "utf8"}},                         {"name" : "i_position", "dataType" : {"type" : "int32"}},                         {"name" : "name", "dataType" : {"type" : "utf8"}},                         {"name" : "value", "dataType" : {"type" : "utf8"}}]
          }
        ), 
        filePath = "aka_GPDIP_EDLUD_324.xlsx"
    )
    model_test_pipeline_Join_318_inner = Task(
        task_id = "model_test_pipeline_Join_318_inner", 
        component = "Model", 
        modelName = "model_test_pipeline_Join_318_inner"
    )
    unstructured_output_databricks_1 = SourceTask(
        task_id = "unstructured_output_databricks_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", id = "dev-test"), 
        format = DATABRICKSFormat(
          description = "Categorical data capturing values and their corresponding names, positions, and object identifiers for analytical purposes.", 
          schema = {
            "providerType": "Arrow", 
            "fields": [{
                          "name": "r_object_id", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Unique identifier for the object represented as a string"
                        },                         {
                          "name": "i_position", 
                          "dataType": {"type" : "int32"}, 
                          "description": "The position index of the object in a sequence"
                        },                         {
                          "name": "name", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The name associated with the object"
                        },                         {
                          "name": "value", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The value associated with the object"
                        }]
          }, 
          properties = {}, 
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          kind = "databricks"
        ), 
        tableFullName = {
          "database": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "main"}}]}
          }, 
          "schema": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "rishabh"}}]}
          }, 
          "name": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "aka_gpdip_edlud_302"}}]}
          }
        }
    )
    Script_1 = Task(
        task_id = "Script_1", 
        component = "Script", 
        ports = None, 
        scriptMethodHeader = "def Script(spark: SparkSession, in0: DataFrame) -> DataFrame:", 
        scriptMethodFooter = "return out0", 
        script = ""
    )
    model_test_pipeline_AlteryxSelect_294 = Task(
        task_id = "model_test_pipeline_AlteryxSelect_294", 
        component = "Model", 
        modelName = "model_test_pipeline_AlteryxSelect_294"
    )
    aka_GPDIP_EDLUD_302 = Task(
        task_id = "aka_GPDIP_EDLUD_302", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_test_pipeline_pre_Filter_303_reject_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_test_pipeline_source", 
          "alias": ""
        }
    )
    aka_GPDIP_EDLUD_298 = SourceTask(
        task_id = "aka_GPDIP_EDLUD_298", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = {
          "kind": "sftp", 
          "id": "transpiled_connection", 
          "properties": {
            "authMethod": "password", 
            "username": "transpiled_username", 
            "host": "sftp.prophecy.io", 
            "id": "transpiled_connection", 
            "port": 22, 
            "password": {
              "kind": "prophecy", 
              "properties": {"name" : "transpiled_secret", "value" : "transpiled_secret"}, 
              "subKind": "text", 
              "type": "secret"
            }
          }, 
          "type": "connector"
        }, 
        format = XLSXFormat(
          schema = {
            "providerType": "Databricks", 
            "fields": [{"name" : "subtype", "dataType" : {"type" : "utf8"}},                         {"name" : "object_name", "dataType" : {"type" : "utf8"}},                         {"name" : "xm_status", "dataType" : {"type" : "utf8"}},                         {"name" : "i_has_folder", "dataType" : {"type" : "int32"}},                         {"name" : "xm_language", "dataType" : {"type" : "utf8"}},                         {"name" : "r_object_id", "dataType" : {"type" : "utf8"}},                         {"name" : "title", "dataType" : {"type" : "utf8"}},                         {"name" : "i_chronicle_id", "dataType" : {"type" : "utf8"}}]
          }
        ), 
        filePath = "aka_GPDIP_EDLUD_298.xlsx"
    )
    model_test_pipeline_Join_310_inner = Task(
        task_id = "model_test_pipeline_Join_310_inner", 
        component = "Model", 
        modelName = "model_test_pipeline_Join_310_inner"
    )
    model_test_pipeline_Cleanse_290 = Task(
        task_id = "model_test_pipeline_Cleanse_290", 
        component = "Model", 
        modelName = "model_test_pipeline_Cleanse_290"
    )
    object_attributes_databricks = SourceTask(
        task_id = "object_attributes_databricks", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", id = "dev-test"), 
        format = DATABRICKSFormat(
          description = "Categorical data capturing values and their corresponding names, positions, and object identifiers for analytical purposes.", 
          schema = {
            "providerType": "Arrow", 
            "fields": [{
                          "name": "r_object_id", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Unique identifier for the object represented as a string"
                        },                         {
                          "name": "i_position", 
                          "dataType": {"type" : "int32"}, 
                          "description": "The position index of the object in a sequence"
                        },                         {
                          "name": "name", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The name associated with the object"
                        },                         {
                          "name": "value", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The value associated with the object"
                        }]
          }, 
          properties = {}, 
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          kind = "databricks"
        ), 
        tableFullName = {
          "database": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "main"}}]}
          }, 
          "schema": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "rishabh"}}]}
          }, 
          "name": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "aka_GPDIP_EDLUD_302"}}]}
          }
        }
    )
    aka_GPDIP_EDLUD_312 = Task(
        task_id = "aka_GPDIP_EDLUD_312", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_test_pipeline_pre_Join_313_inner_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_test_pipeline_source", 
          "alias": ""
        }
    )
    aka_GPDIP_EDLUD_324 = Task(
        task_id = "aka_GPDIP_EDLUD_324", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_test_pipeline_pre_Filter_323_reject_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_test_pipeline_source", 
          "alias": ""
        }
    )
    unstructured_output_databricks = SourceTask(
        task_id = "unstructured_output_databricks", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", id = "dev-test"), 
        format = DATABRICKSFormat(
          description = "Categorical data capturing values and their corresponding names, positions, and object identifiers for analytical purposes.", 
          schema = {
            "providerType": "Arrow", 
            "fields": [{
                          "name": "r_object_id", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Unique identifier for the object represented as a string"
                        },                         {
                          "name": "i_position", 
                          "dataType": {"type" : "int32"}, 
                          "description": "The position index of the object in a sequence"
                        },                         {
                          "name": "name", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The name associated with the object"
                        },                         {
                          "name": "value", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The value associated with the object"
                        }]
          }, 
          properties = {}, 
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          kind = "databricks"
        ), 
        tableFullName = {
          "database": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "main"}}]}
          }, 
          "schema": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "rishabh"}}]}
          }, 
          "name": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "aka_gpdip_edlud_302"}}]}
          }
        }
    )
    model_test_pipeline_Sort_266 = Task(
        task_id = "model_test_pipeline_Sort_266", 
        component = "Model", 
        modelName = "model_test_pipeline_Sort_266"
    )
    aka_GPDIP_EDLUD_289 = SourceTask(
        task_id = "aka_GPDIP_EDLUD_289", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = {
          "kind": "sftp", 
          "id": "transpiled_connection", 
          "properties": {
            "authMethod": "password", 
            "username": "transpiled_username", 
            "host": "sftp.prophecy.io", 
            "id": "transpiled_connection", 
            "port": 22, 
            "password": {
              "kind": "prophecy", 
              "properties": {"name" : "transpiled_secret", "value" : "transpiled_secret"}, 
              "subKind": "text", 
              "type": "secret"
            }
          }, 
          "type": "connector"
        }, 
        format = XLSXFormat(
          schema = {
            "providerType": "Databricks", 
            "fields": [{"name" : "is_active", "dataType" : {"type" : "utf8"}},                         {"name" : "is_static", "dataType" : {"type" : "utf8"}},                         {"name" : "extract_date", "dataType" : {"type" : "timestamp"}},                         {"name" : "product_name", "dataType" : {"type" : "utf8"}},                         {"name" : "country_abbreviation", "dataType" : {"type" : "utf8"}},                         {"name" : "app_country_id", "dataType" : {"type" : "int32"}},                         {"name" : "country_name", "dataType" : {"type" : "utf8"}}]
          }
        ), 
        filePath = "aka_GPDIP_EDLUD_289.xlsx"
    )
    aka_GPDIP_EDLUD_312.output_port_3_1 >> model_test_pipeline_AlteryxSelect_294.in_0
    (
        aka_GPDIP_EDLUD_302.output_port_5_1
        >> [model_test_pipeline_Join_310_inner.in_2, model_test_pipeline_Join_310_inner.in_3]
    )
    aka_GPDIP_EDLUD_324.out0 >> aka_GPDIP_EDLUD_324.input_port_2_1
    aka_GPDIP_EDLUD_289.out0 >> aka_GPDIP_EDLUD_289.input_port_0_1
    aka_GPDIP_EDLUD_289.output_port_0_1 >> model_test_pipeline_Cleanse_290.in_0
    model_test_pipeline_Join_318_inner.out_0 >> model_test_pipeline_AlteryxSelect_294.in_0
    model_test_pipeline_Join_310_inner.out_0 >> model_test_pipeline_AlteryxSelect_294.in_0
    aka_GPDIP_EDLUD_298.output_port_6_1 >> model_test_pipeline_AlteryxSelect_294.in_2
    (
        model_test_pipeline_Cleanse_290.out_0
        >> [model_test_pipeline_Join_310_inner.in_0, model_test_pipeline_Join_318_inner.in_0]
    )
    aka_GPDIP_EDLUD_298.out0 >> aka_GPDIP_EDLUD_298.input_port_6_1
    aka_GPDIP_EDLUD_312.out0 >> aka_GPDIP_EDLUD_312.input_port_3_1
    (
        aka_GPDIP_EDLUD_324.output_port_2_1
        >> [model_test_pipeline_Join_318_inner.in_2, model_test_pipeline_Join_318_inner.in_3]
    )
    aka_GPDIP_EDLUD_302.out0 >> aka_GPDIP_EDLUD_302.input_port_5_1

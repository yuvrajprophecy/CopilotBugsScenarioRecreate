{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_test_pipeline_post_Cleanse_290_0",
    "database": "main",
    "schema": "rishabh"
  })
}}

WITH aka_GPDIP_EDLUD_289 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_test_pipeline_source', 'prophecy__temp_test_pipeline_pre_Cleanse_290_0') }}

),

Cleanse_290 AS (

  {{
    DatabricksSqlBasics.DataCleansing(
      'aka_GPDIP_EDLUD_289', 
      [
        { "name": "is_active", "dataType": "String" }, 
        { "name": "is_static", "dataType": "String" }, 
        { "name": "extract_date", "dataType": "Timestamp" }, 
        { "name": "product_name", "dataType": "String" }, 
        { "name": "country_abbreviation", "dataType": "String" }, 
        { "name": "app_country_id", "dataType": "Integer" }, 
        { "name": "country_name", "dataType": "String" }
      ], 
      'Keep original', 
      ['country_name', 'product_name'], 
      false, 
      '', 
      false, 
      0, 
      false, 
      false, 
      false, 
      false, 
      false, 
      false, 
      false
    )
  }}

)

SELECT *

FROM Cleanse_290

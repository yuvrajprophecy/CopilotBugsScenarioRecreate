{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_Large_LU_Document_Selection_Disabled_post_Cleanse_290_0",
    "database": "main",
    "schema": "rishabh"
  })
}}

WITH ORACLE_LARGE_AKA_GPDIP_EDLUD_289 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_Large_LU_Document_Selection_Disabled_source', 'prophecy__temp_Large_LU_Document_Selection_Disabled_pre_Cleanse_290_0') }}

),

Cleanse_290 AS (

  {{
    DatabricksSqlBasics.DataCleansing(
      'ORACLE_LARGE_AKA_GPDIP_EDLUD_289_1', 
      [
        { "name": "is_static", "dataType": "String" }, 
        { "name": "extract_date", "dataType": "String" }, 
        { "name": "product_name", "dataType": "String" }, 
        { "name": "country_abbreviation", "dataType": "String" }, 
        { "name": "app_country_id", "dataType": "Decimal" }, 
        { "name": "country_name", "dataType": "String" }, 
        { "name": "is_active", "dataType": "String" }
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

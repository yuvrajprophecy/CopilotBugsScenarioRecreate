{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_OP_LARGE_LU_Document_Selection_Disabled_post_Cleanse_290_0",
    "database": "main",
    "schema": "rishabh"
  })
}}

WITH `1m_aka_gpdip_edlud_289` AS (

  SELECT * 
  
  FROM {{ source('main.rishabh', '1m_aka_gpdip_edlud_289') }}

),

Cleanse_290 AS (

  {{
    DatabricksSqlBasics.DataCleansing(
      '1m_aka_gpdip_edlud_289', 
      [
        { "name": "is_active", "dataType": "String" }, 
        { "name": "is_static", "dataType": "String" }, 
        { "name": "extract_date", "dataType": "String" }, 
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
      true
    )
  }}

)

SELECT *

FROM Cleanse_290

{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_LU_Subcountry_Tree_Disabled_post_DataCleansing_1_0",
    "database": "main",
    "schema": "rishabh"
  })
}}

WITH aka_GPDIP_EDLUD_346 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_LU_Subcountry_Tree_Disabled_source', 'prophecy__temp_LU_Subcountry_Tree_Disabled_post_aka_GPDIP_EDLUD_346_0') }}

),

DataCleansing_1 AS (

  {{ DatabricksSqlBasics.DataCleansing() }}

)

SELECT *

FROM DataCleansing_1

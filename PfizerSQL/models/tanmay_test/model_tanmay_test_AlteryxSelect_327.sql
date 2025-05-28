{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_tanmay_test_post_AlteryxSelect_327_0",
    "database": "main",
    "schema": "rishabh"
  })
}}

WITH AKA_GPDIP_EDLUD_302 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_tanmay_test_source', 'prophecy__temp_tanmay_test_pre_Filter_303_reject_0') }}

),

Filter_303 AS (

  SELECT * 
  
  FROM AKA_GPDIP_EDLUD_302 AS in0
  
  WHERE name = 'PFLEET_SUB_COUNTRY_ROW_ID'

),

AlteryxSelect_327 AS (

  SELECT 
    i_position AS i_position,
    name AS name,
    CAST(value AS INTEGER) AS pfleet_subcountry_row_id,
    r_object_id AS r_object_id
  
  FROM Filter_303 AS in0

)

SELECT *

FROM AlteryxSelect_327

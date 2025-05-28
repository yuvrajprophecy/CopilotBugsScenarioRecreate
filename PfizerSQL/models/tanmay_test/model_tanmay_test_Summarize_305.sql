{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_tanmay_test_post_Summarize_305_0",
    "database": "main",
    "schema": "rishabh"
  })
}}

WITH AKA_GPDIP_EDLUD_302 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_tanmay_test_source', 'prophecy__temp_tanmay_test_pre_Filter_303_reject_0') }}

),

Filter_303_reject AS (

  SELECT * 
  
  FROM AKA_GPDIP_EDLUD_302 AS in0
  
  WHERE NOT name = 'PFLEET_SUB_COUNTRY_ROW_ID'

),

Sort_304 AS (

  SELECT * 
  
  FROM Filter_303_reject AS in0
  
  ORDER BY ENCODE(CAST(r_object_id AS STRING), 'utf-8') ASC, ENCODE(CAST(value AS STRING), 'utf-8') ASC

),

Summarize_305 AS (

  SELECT 
    concat_ws(',', collect_list(value)) AS r_version_label,
    r_object_id AS r_object_id
  
  FROM Sort_304 AS in0
  
  GROUP BY r_object_id

)

SELECT *

FROM Summarize_305

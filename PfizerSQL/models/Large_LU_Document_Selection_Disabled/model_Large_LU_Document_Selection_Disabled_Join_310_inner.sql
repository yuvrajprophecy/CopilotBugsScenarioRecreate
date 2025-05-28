{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_Large_LU_Document_Selection_Disabled_pre_Join_299_inner_0",
    "database": "main",
    "schema": "rishabh"
  })
}}

WITH AKA_GPDIP_EDLUD_302 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_Large_LU_Document_Selection_Disabled_source', 'prophecy__temp_Large_LU_Document_Selection_Disabled_pre_Filter_303_reject_0') }}

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

),

Cleanse_290 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_Large_LU_Document_Selection_Disabled_source', 'prophecy__temp_Large_LU_Document_Selection_Disabled_post_Cleanse_290_0') }}

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

),

Join_306_inner AS (

  SELECT 
    in0.r_object_id AS r_object_id,
    in0.pfleet_subcountry_row_id AS pfleet_subcountry_row_id,
    in1.r_version_label AS r_version_label
  
  FROM AlteryxSelect_327 AS in0
  INNER JOIN Summarize_305 AS in1
     ON in0.r_object_id = in1.r_object_id

),

Join_310_inner AS (

  SELECT 
    in0.extract_date AS extract_date,
    in1.r_version_label AS r_version_label,
    in1.r_object_id AS r_object_id,
    in0.app_country_id AS app_country_id,
    in0.country_name AS country_name
  
  FROM Cleanse_290 AS in0
  INNER JOIN Join_306_inner AS in1
     ON in0.app_country_id = in1.pfleet_subcountry_row_id

)

SELECT *

FROM Join_310_inner

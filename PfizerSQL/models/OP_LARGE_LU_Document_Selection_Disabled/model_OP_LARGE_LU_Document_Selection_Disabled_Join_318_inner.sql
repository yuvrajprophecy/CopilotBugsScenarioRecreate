{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_OP_LARGE_LU_Document_Selection_Disabled_pre_Join_313_inner_0",
    "database": "main",
    "schema": "rishabh"
  })
}}

WITH `1m_aka_gpdip_edlud_324` AS (

  SELECT * 
  
  FROM {{ source('main.rishabh', '1m_aka_gpdip_edlud_324') }}

),

sub_country_values AS (

  SELECT 
    r_object_id AS r_object_id,
    CAST(MAX(CASE
      WHEN name = 'PFLEET_SUB_COUNTRY_ROW_ID'
        THEN value
    END) AS INT) AS pfleet_subcountry_row_id,
    concat_ws(',', collect_list(CASE
      WHEN name <> 'PFLEET_SUB_COUNTRY_ROW_ID'
        THEN value
    END)) AS r_version_label
  
  FROM `1m_aka_gpdip_edlud_324` AS in0
  
  GROUP BY r_object_id

),

Cleanse_290 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_OP_LARGE_LU_Document_Selection_Disabled_source', 'prophecy__temp_OP_LARGE_LU_Document_Selection_Disabled_post_Cleanse_290_0') }}

),

Join_318_inner AS (

  SELECT 
    in0.extract_date AS extract_date,
    in1.r_version_label AS r_version_label,
    in1.r_object_id AS r_object_id,
    in0.app_country_id AS app_country_id,
    in0.country_name AS country_name
  
  FROM Cleanse_290 AS in0
  INNER JOIN sub_country_values AS in1
     ON in0.app_country_id = in1.pfleet_subcountry_row_id

)

SELECT *

FROM Join_318_inner

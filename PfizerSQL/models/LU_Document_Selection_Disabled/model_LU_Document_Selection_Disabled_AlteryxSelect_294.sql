{{
  config({    
    "materialized": "table",
    "alias": "SQL_1K_LU_Document_Selection_Disabled",
    "database": "main",
    "schema": "rishabh"
  })
}}

WITH Join_318_inner AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_LU_Document_Selection_Disabled_source', 'prophecy__temp_LU_Document_Selection_Disabled_pre_Join_313_inner_0') }}

),

`1k_aka_gpdip_edlud_312` AS (

  SELECT * 
  
  FROM {{ source('main.rishabh', '1k_aka_gpdip_edlud_312') }}

),

Join_313_inner AS (

  SELECT 
    in1.subtype AS subtype,
    in1.object_name AS object_name,
    in0.extract_date AS extract_date,
    in1.xm_status AS xm_status,
    in0.r_version_label AS r_version_label,
    in1.xm_language AS xm_language,
    in0.r_object_id AS r_object_id,
    in0.app_country_id AS sub_country_id,
    in1.title AS title,
    in1.i_chronicle_id AS i_chronicle_id,
    in0.country_name AS sub_country_name
  
  FROM Join_318_inner AS in0
  INNER JOIN `1k_aka_gpdip_edlud_312` AS in1
     ON in0.r_object_id = in1.r_object_id

),

Formula_314 AS (

  SELECT 
    CAST('\'http://gdms.pfizer.com/gdms/drl/objectId/\' + [r_object_id]' AS STRING) AS document_url,
    extract_date AS extract_date,
    i_chronicle_id AS i_chronicle_id,
    object_name AS object_name,
    r_object_id AS r_object_id,
    r_version_label AS r_version_label,
    sub_country_id AS sub_country_id,
    sub_country_name AS sub_country_name,
    subtype AS subtype,
    title AS title,
    xm_language AS xm_language,
    xm_status AS xm_status
  
  FROM Join_313_inner AS in0

),

Union_292_reformat_1 AS (

  SELECT 
    document_url AS document_url,
    extract_date AS extract_date,
    i_chronicle_id AS i_chronicle_id,
    object_name AS object_name,
    r_object_id AS r_object_id,
    r_version_label AS r_version_label,
    sub_country_id AS sub_country_id,
    sub_country_name AS sub_country_name,
    subtype AS subtype,
    title AS title,
    xm_language AS xm_language,
    xm_status AS xm_status
  
  FROM Formula_314 AS in0

),

Join_310_inner AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_LU_Document_Selection_Disabled_source', 'prophecy__temp_LU_Document_Selection_Disabled_pre_Join_299_inner_0') }}

),

`1k_aka_gpdip_edlud_298` AS (

  SELECT * 
  
  FROM {{ source('main.rishabh', '1k_aka_gpdip_edlud_298') }}

),

Join_299_inner AS (

  SELECT 
    in1.subtype AS subtype,
    in1.object_name AS object_name,
    in0.extract_date AS extract_date,
    in1.xm_status AS xm_status,
    in0.r_version_label AS r_version_label,
    in1.xm_language AS xm_language,
    in0.r_object_id AS r_object_id,
    in0.app_country_id AS sub_country_id,
    in1.title AS title,
    in1.i_chronicle_id AS i_chronicle_id,
    in0.country_name AS sub_country_name
  
  FROM Join_310_inner AS in0
  INNER JOIN `1k_aka_gpdip_edlud_298` AS in1
     ON in0.r_object_id = in1.r_object_id

),

Formula_300 AS (

  SELECT 
    CAST('\'http://gdms.pfizer.com/gdms/drl/objectId/\' + [r_object_id]' AS STRING) AS document_url,
    extract_date AS extract_date,
    i_chronicle_id AS i_chronicle_id,
    object_name AS object_name,
    r_object_id AS r_object_id,
    r_version_label AS r_version_label,
    sub_country_id AS sub_country_id,
    sub_country_name AS sub_country_name,
    subtype AS subtype,
    title AS title,
    xm_language AS xm_language,
    xm_status AS xm_status
  
  FROM Join_299_inner AS in0

),

Union_292_reformat_0 AS (

  SELECT 
    document_url AS document_url,
    extract_date AS extract_date,
    i_chronicle_id AS i_chronicle_id,
    object_name AS object_name,
    r_object_id AS r_object_id,
    r_version_label AS r_version_label,
    sub_country_id AS sub_country_id,
    sub_country_name AS sub_country_name,
    subtype AS subtype,
    title AS title,
    xm_language AS xm_language,
    xm_status AS xm_status
  
  FROM Formula_300 AS in0

),

Union_292 AS (

  SELECT * 
  
  FROM Union_292_reformat_0 AS in0
  
  UNION ALL
  
  SELECT * 
  
  FROM Union_292_reformat_1 AS in1

),

Sort_293 AS (

  SELECT * 
  
  FROM Union_292 AS in0
  
  ORDER BY ENCODE(CAST(sub_country_id AS STRING), 'utf-8') ASC, ENCODE(CAST(r_object_id AS STRING), 'utf-8') ASC

),

AlteryxSelect_294 AS (

  SELECT 
    document_url AS document_url,
    extract_date AS extract_date,
    i_chronicle_id AS i_chronicle_id,
    object_name AS object_name,
    r_object_id AS r_object_id,
    r_version_label AS r_version_label,
    sub_country_id AS sub_country_id,
    sub_country_name AS sub_country_name,
    subtype AS subtype,
    title AS title,
    xm_language AS xm_language,
    xm_status AS xm_status
  
  FROM Sort_293 AS in0

)

SELECT *

FROM AlteryxSelect_294

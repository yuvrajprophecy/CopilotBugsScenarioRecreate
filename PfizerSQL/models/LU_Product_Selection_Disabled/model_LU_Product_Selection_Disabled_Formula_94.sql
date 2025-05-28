{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_LU_Product_Selection_Disabled_post_Formula_94_0",
    "database": "main",
    "schema": "rishabh"
  })
}}

WITH `1m_aka_gpdip_edlud_324` AS (

  SELECT * 
  
  FROM {{ source('main.rishabh', '1m_aka_gpdip_edlud_324') }}

),

Filter_130 AS (

  SELECT * 
  
  FROM `1m_aka_gpdip_edlud_324` AS in0
  
  WHERE CAST(name AS STRING) IN ('GENERIC_NAME', 'PFE_XM_P_COMPOUND_NUM', 'PROPRIETARY_NAME')

),

Filter_142 AS (

  SELECT * 
  
  FROM `1m_aka_gpdip_edlud_324` AS in0
  
  WHERE name = 'PFLEET_SUB_COUNTRY_ROW_ID'

),

AlteryxSelect_143 AS (

  SELECT 
    i_position AS i_position,
    name AS name,
    r_object_id AS r_object_id,
    CAST(value AS INTEGER) AS value
  
  FROM Filter_142 AS in0

),

large_aka_gpdip_edlud_133 AS (

  SELECT * 
  
  FROM {{ source('main.rishabh', 'large_aka_gpdip_edlud_133') }}

),

AlteryxSelect_123 AS (

  SELECT 
    i_chronicle_id AS i_chronicle_id,
    i_has_folder AS i_has_folder,
    r_object_id AS r_object_id
  
  FROM large_aka_gpdip_edlud_133 AS in0

),

Filter_124 AS (

  SELECT * 
  
  FROM AlteryxSelect_123 AS in0
  
  WHERE i_has_folder = CAST('1' AS INTEGER)

),

Join_128_inner AS (

  SELECT 
    in0.r_object_id AS r_object_id,
    in0.i_position AS i_position,
    in0.name AS name,
    in0.value AS value
  
  FROM AlteryxSelect_143 AS in0
  INNER JOIN Filter_124 AS in1
     ON in0.r_object_id = in1.r_object_id

),

large_aka_gpdip_edlud_113_script AS (

  SELECT * 
  
  FROM {{ source('main.rishabh', 'large_aka_gpdip_edlud_113_script') }}

),

Cleanse_121 AS (

  {{
    DatabricksSqlBasics.DataCleansing(
      'Table_1', 
      [
        { "name": "is_active", "dataType": "String" }, 
        { "name": "is_static", "dataType": "String" }, 
        { "name": "product_name", "dataType": "String" }, 
        { "name": "parent_app_country_id", "dataType": "Integer" }, 
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

),

Filter_118 AS (

  SELECT * 
  
  FROM Cleanse_121 AS in0
  
  WHERE NOT parent_app_country_id IS NULL

),

Filter_118_reject AS (

  SELECT * 
  
  FROM Cleanse_121 AS in0
  
  WHERE NOT(NOT parent_app_country_id IS NULL)

),

Join_119_inner AS (

  SELECT 
    in0.is_active AS is_active,
    in0.is_static AS is_static,
    in0.product_name AS product_name,
    in0.parent_app_country_id AS parent_app_country_id,
    in0.app_country_id AS sub_country_id,
    in1.country_abbreviation AS country_abbreviation,
    in1.country_name AS country_name,
    in0.country_name AS sub_country_name
  
  FROM Filter_118 AS in0
  INNER JOIN Filter_118_reject AS in1
     ON in0.parent_app_country_id = in1.app_country_id

),

Filter_88_reject AS (

  SELECT * 
  
  FROM Join_119_inner AS in0
  
  WHERE NOT country_name = 'Core Document'

),

Join_125_inner AS (

  SELECT 
    in1.r_object_id AS r_object_id,
    in0.product_name AS product_name,
    in0.sub_country_id AS sub_country_id,
    in0.country_abbreviation AS country_abbreviation,
    in0.country_name AS country_name
  
  FROM Filter_88_reject AS in0
  INNER JOIN Join_128_inner AS in1
     ON in0.sub_country_id = in1.value

),

Join_129_inner AS (

  SELECT 
    in1.name AS name,
    in1.i_position AS i_position,
    in0.r_object_id AS r_object_id,
    in0.product_name AS product_name,
    in0.sub_country_id AS sub_country_id,
    in0.country_abbreviation AS country_abbreviation,
    in1.value AS value,
    in0.country_name AS country_name
  
  FROM Join_125_inner AS in0
  INNER JOIN Filter_130 AS in1
     ON in0.r_object_id = in1.r_object_id

),

Union_131_reformat_1 AS (

  SELECT 
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    CAST(i_position AS INTEGER) AS i_position,
    CAST(NULL AS STRING) AS is_active,
    CAST(NULL AS STRING) AS is_static,
    CAST(name AS STRING) AS name,
    CAST(NULL AS INTEGER) AS parent_app_country_id,
    product_name AS product_name,
    CAST(r_object_id AS STRING) AS r_object_id,
    sub_country_id AS sub_country_id,
    CAST(NULL AS STRING) AS sub_country_name,
    CAST(value AS STRING) AS value
  
  FROM Join_129_inner AS in0

),

Join_125_left AS (

  SELECT 
    in0.country_name AS country_name,
    in0.is_active AS is_active,
    in0.country_abbreviation AS country_abbreviation,
    in0.parent_app_country_id AS parent_app_country_id,
    in0.sub_country_id AS sub_country_id,
    in0.sub_country_name AS sub_country_name,
    in0.is_static AS is_static,
    in0.product_name AS product_name
  
  FROM Filter_88_reject AS in0
  ANTI JOIN Join_128_inner AS in1
     ON in0.sub_country_id = in1.value

),

Union_131_reformat_0 AS (

  SELECT 
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    CAST(NULL AS INTEGER) AS i_position,
    CAST(is_active AS STRING) AS is_active,
    CAST(is_static AS STRING) AS is_static,
    CAST(NULL AS STRING) AS name,
    CAST(parent_app_country_id AS INTEGER) AS parent_app_country_id,
    product_name AS product_name,
    CAST(NULL AS STRING) AS r_object_id,
    sub_country_id AS sub_country_id,
    CAST(sub_country_name AS STRING) AS sub_country_name,
    CAST(NULL AS STRING) AS value
  
  FROM Join_125_left AS in0

),

Union_131 AS (

  SELECT * 
  
  FROM Union_131_reformat_0 AS in0
  
  UNION ALL
  
  SELECT * 
  
  FROM Union_131_reformat_1 AS in1

),

CrossTab_144_0 AS (

  SELECT 
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    i_position AS i_position,
    is_active AS is_active,
    is_static AS is_static,
    CASE
      WHEN name IS NULL
        THEN '_Null_'
      ELSE name
    END AS name,
    parent_app_country_id AS parent_app_country_id,
    product_name AS product_name,
    r_object_id AS r_object_id,
    sub_country_id AS sub_country_id,
    sub_country_name AS sub_country_name,
    value AS value
  
  FROM Union_131 AS in0

),

CrossTab_144_1 AS (

  SELECT 
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    i_position AS i_position,
    is_active AS is_active,
    is_static AS is_static,
    REGEXP_REPLACE(name, '[\\s!@#$%^&*(),.?":{}|<>\\[\\]=;/\\-+]', '_') AS name,
    parent_app_country_id AS parent_app_country_id,
    product_name AS product_name,
    r_object_id AS r_object_id,
    sub_country_id AS sub_country_id,
    sub_country_name AS sub_country_name,
    value AS value
  
  FROM CrossTab_144_0 AS in0

),

CrossTab_144_regularActions AS (

  WITH pivot_0 AS (
  
    SELECT 
      product_name,
      country_name,
      country_abbreviation,
      sub_country_id,
      r_object_id,
      i_position,
      PFE_XM_P_COMPOUND_NUM AS PFE_XM_P_COMPOUND_NUM_Concat,
      _Null_ AS _Null__Concat,
      GENERIC_NAME AS GENERIC_NAME_Concat,
      PROPRIETARY_NAME AS PROPRIETARY_NAME_Concat
    
    FROM (
      SELECT 
        product_name AS product_name,
        country_name AS country_name,
        country_abbreviation AS country_abbreviation,
        sub_country_id AS sub_country_id,
        r_object_id AS r_object_id,
        i_position AS i_position,
        name AS PIVOT_COL,
        value
      
      FROM CrossTab_144_1
    )
    PIVOT (
      CONCAT_WS(',', COLLECT_LIST(value))
      FOR PIVOT_COL
      IN (
        'PFE_XM_P_COMPOUND_NUM', '_Null_', 'GENERIC_NAME', 'PROPRIETARY_NAME'
      )
    )
    
    GROUP BY 
      product_name, 
      country_name, 
      country_abbreviation, 
      sub_country_id, 
      r_object_id, 
      i_position, 
      PFE_XM_P_COMPOUND_NUM_Concat, 
      _Null__Concat, 
      GENERIC_NAME_Concat, 
      PROPRIETARY_NAME_Concat
  
  ),
  
  pivot_1 AS (
  
    SELECT 
      product_name,
      country_name,
      country_abbreviation,
      sub_country_id,
      r_object_id,
      i_position,
      PFE_XM_P_COMPOUND_NUM AS PFE_XM_P_COMPOUND_NUM__dummy_,
      _Null_ AS _Null___dummy_,
      GENERIC_NAME AS GENERIC_NAME__dummy_,
      PROPRIETARY_NAME AS PROPRIETARY_NAME__dummy_
    
    FROM (
      SELECT 
        product_name AS product_name,
        country_name AS country_name,
        country_abbreviation AS country_abbreviation,
        sub_country_id AS sub_country_id,
        r_object_id AS r_object_id,
        i_position AS i_position,
        name AS PIVOT_COL
      
      FROM CrossTab_144_1
    )
    PIVOT (
      1
      FOR PIVOT_COL
      IN (
        'PFE_XM_P_COMPOUND_NUM', '_Null_', 'GENERIC_NAME', 'PROPRIETARY_NAME'
      )
    )
    
    GROUP BY 
      product_name, 
      country_name, 
      country_abbreviation, 
      sub_country_id, 
      r_object_id, 
      i_position, 
      PFE_XM_P_COMPOUND_NUM__dummy_, 
      _Null___dummy_, 
      GENERIC_NAME__dummy_, 
      PROPRIETARY_NAME__dummy_
  
  )
  
  SELECT 
    pivot_0.product_name,
    pivot_0.country_name,
    pivot_0.country_abbreviation,
    pivot_0.sub_country_id,
    pivot_0.r_object_id,
    pivot_0.i_position,
    pivot_0.PFE_XM_P_COMPOUND_NUM_Concat,
    pivot_0._Null__Concat,
    pivot_0.GENERIC_NAME_Concat,
    pivot_0.PROPRIETARY_NAME_Concat,
    pivot_1.PFE_XM_P_COMPOUND_NUM__dummy_,
    pivot_1._Null___dummy_,
    pivot_1.GENERIC_NAME__dummy_,
    pivot_1.PROPRIETARY_NAME__dummy_
  
  FROM pivot_0
  JOIN pivot_1
     ON pivot_1.product_name = pivot_0.product_name
    AND pivot_1.country_name = pivot_0.country_name
    AND pivot_1.country_abbreviation = pivot_0.country_abbreviation
    AND pivot_1.sub_country_id = pivot_0.sub_country_id
    AND pivot_1.r_object_id = pivot_0.r_object_id
    AND pivot_1.i_position = pivot_0.i_position

),

CrossTab_144_rename AS (

  SELECT 
    GENERIC_NAME_Concat AS GENERIC_NAME,
    PFE_XM_P_COMPOUND_NUM_Concat AS PFE_XM_P_COMPOUND_NUM,
    PROPRIETARY_NAME_Concat AS PROPRIETARY_NAME,
    _Null__Concat AS _Null_,
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    i_position AS i_position,
    product_name AS product_name,
    r_object_id AS r_object_id,
    sub_country_id AS sub_country_id
  
  FROM CrossTab_144_regularActions AS in0

),

AlteryxSelect_164 AS (

  SELECT 
    PROPRIETARY_NAME AS PROPRIETARY_NAME,
    country_name AS country_name,
    product_name AS product_name
  
  FROM CrossTab_144_rename AS in0

),

Unique_165 AS (

  SELECT 
    PROPRIETARY_NAME AS PROPRIETARY_NAME,
    country_name AS country_name,
    product_name AS product_name,
    ROW_NUMBER() OVER (PARTITION BY product_name, country_name, PROPRIETARY_NAME ORDER BY product_name NULLS FIRST, country_name NULLS FIRST, PROPRIETARY_NAME NULLS FIRST) AS row_number
  
  FROM AlteryxSelect_164 AS in0

),

Unique_165_filter AS (

  SELECT * 
  
  FROM Unique_165 AS in0
  
  WHERE row_number = 1

),

Filter_167 AS (

  SELECT * 
  
  FROM Unique_165_filter AS in0
  
  WHERE NOT LENGTH(PROPRIETARY_NAME) = 0

),

Sort_166 AS (

  SELECT * 
  
  FROM Filter_167 AS in0
  
  ORDER BY ENCODE(CAST(PROPRIETARY_NAME AS STRING), 'utf-8') ASC

),

Summarize_168 AS (

  SELECT 
    concat_ws('|', collect_list(PROPRIETARY_NAME)) AS trade_name_set,
    product_name AS product_name,
    country_name AS country_name
  
  FROM Sort_166 AS in0
  
  GROUP BY 
    product_name, country_name

),

AlteryxSelect_158 AS (

  SELECT 
    PFE_XM_P_COMPOUND_NUM AS PFE_XM_P_COMPOUND_NUM,
    country_name AS country_name,
    product_name AS product_name
  
  FROM CrossTab_144_rename AS in0

),

Unique_159 AS (

  SELECT 
    PFE_XM_P_COMPOUND_NUM AS PFE_XM_P_COMPOUND_NUM,
    country_name AS country_name,
    product_name AS product_name,
    ROW_NUMBER() OVER (PARTITION BY product_name, country_name, PFE_XM_P_COMPOUND_NUM ORDER BY product_name NULLS FIRST, country_name NULLS FIRST, PFE_XM_P_COMPOUND_NUM NULLS FIRST) AS row_number
  
  FROM AlteryxSelect_158 AS in0

),

Unique_159_filter AS (

  SELECT * 
  
  FROM Unique_159 AS in0
  
  WHERE row_number = 1

),

Filter_161 AS (

  SELECT * 
  
  FROM Unique_159_filter AS in0
  
  WHERE NOT LENGTH(PFE_XM_P_COMPOUND_NUM) = 0

),

Sort_160 AS (

  SELECT * 
  
  FROM Filter_161 AS in0
  
  ORDER BY ENCODE(CAST(PFE_XM_P_COMPOUND_NUM AS STRING), 'utf-8') ASC

),

Summarize_162 AS (

  SELECT 
    concat_ws('|', collect_list(PFE_XM_P_COMPOUND_NUM)) AS compound_number_set,
    product_name AS product_name,
    country_name AS country_name
  
  FROM Sort_160 AS in0
  
  GROUP BY 
    product_name, country_name

),

AlteryxSelect_146 AS (

  SELECT 
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    product_name AS product_name,
    CAST(sub_country_id AS STRING) AS sub_country_id
  
  FROM CrossTab_144_rename AS in0

),

Unique_147 AS (

  SELECT 
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    product_name AS product_name,
    ROW_NUMBER() OVER (PARTITION BY product_name, country_name, country_abbreviation, sub_country_id ORDER BY product_name NULLS FIRST, country_name NULLS FIRST, country_abbreviation NULLS FIRST, sub_country_id NULLS FIRST) AS row_number,
    sub_country_id AS sub_country_id
  
  FROM AlteryxSelect_146 AS in0

),

Unique_147_filter AS (

  SELECT * 
  
  FROM Unique_147 AS in0
  
  WHERE row_number = 1

),

Filter_150 AS (

  SELECT * 
  
  FROM Unique_147_filter AS in0
  
  WHERE NOT LENGTH(sub_country_id) = 0

),

Sort_149 AS (

  SELECT * 
  
  FROM Filter_150 AS in0
  
  ORDER BY ENCODE(CAST(sub_country_id AS STRING), 'utf-8') ASC

),

Summarize_148 AS (

  SELECT 
    concat(concat_ws('|', collect_list(sub_country_id)), '|') AS sub_country_id_set,
    product_name AS product_name,
    country_name AS country_name,
    country_abbreviation AS country_abbreviation
  
  FROM Sort_149 AS in0
  
  GROUP BY 
    product_name, country_name, country_abbreviation

),

AlteryxSelect_152 AS (

  SELECT 
    GENERIC_NAME AS GENERIC_NAME,
    country_name AS country_name,
    product_name AS product_name
  
  FROM CrossTab_144_rename AS in0

),

Unique_153 AS (

  SELECT 
    GENERIC_NAME AS GENERIC_NAME,
    country_name AS country_name,
    product_name AS product_name,
    ROW_NUMBER() OVER (PARTITION BY product_name, country_name, GENERIC_NAME ORDER BY product_name NULLS FIRST, country_name NULLS FIRST, GENERIC_NAME NULLS FIRST) AS row_number
  
  FROM AlteryxSelect_152 AS in0

),

Unique_153_filter AS (

  SELECT * 
  
  FROM Unique_153 AS in0
  
  WHERE row_number = 1

),

Filter_155 AS (

  SELECT * 
  
  FROM Unique_153_filter AS in0
  
  WHERE NOT LENGTH(GENERIC_NAME) = 0

),

Sort_154 AS (

  SELECT * 
  
  FROM Filter_155 AS in0
  
  ORDER BY ENCODE(CAST(GENERIC_NAME AS STRING), 'utf-8') ASC

),

Summarize_156 AS (

  SELECT 
    concat_ws('|', collect_list(GENERIC_NAME)) AS generic_name_set,
    product_name AS product_name,
    country_name AS country_name
  
  FROM Sort_154 AS in0
  
  GROUP BY 
    product_name, country_name

),

JoinMultiple_145 AS (

  SELECT 
    in1.generic_name_set AS generic_name_set,
    in2.compound_number_set AS compound_number_set,
    in0.product_name AS product_name,
    in3.trade_name_set AS trade_name_set,
    in0.country_abbreviation AS country_abbreviation,
    in0.country_name AS country_name,
    in0.sub_country_id_set AS sub_country_id_set
  
  FROM Summarize_148 AS in0
  FULL JOIN Summarize_156 AS in1
     ON in0.product_name = in1.product_name AND in0.country_name = in1.country_name
  FULL JOIN Summarize_162 AS in2
     ON (
      (coalesce(in0.product_name, in1.product_name) = in2.product_name)
      AND (coalesce(in0.country_name, in1.country_name) = in2.country_name)
    )
  FULL JOIN Summarize_168 AS in3
     ON (
      (coalesce(in0.product_name, coalesce(in1.product_name, in2.product_name)) = in3.product_name)
      AND (coalesce(in0.country_name, coalesce(in1.country_name, in2.country_name)) = in3.country_name)
    )

),

Union_84_reformat_0 AS (

  SELECT 
    compound_number_set AS compound_number_set,
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    generic_name_set AS generic_name_set,
    product_name AS product_name,
    sub_country_id_set AS sub_country_id_set,
    trade_name_set AS trade_name_set
  
  FROM JoinMultiple_145 AS in0

),

large_aka_gpdip_edlud_133_1 AS (

  SELECT * 
  
  FROM {{ source('main.rishabh', 'large_aka_gpdip_edlud_133') }}

),

AlteryxSelect_18 AS (

  SELECT 
    i_chronicle_id AS i_chronicle_id,
    i_has_folder AS i_has_folder,
    r_object_id AS r_object_id
  
  FROM large_aka_gpdip_edlud_133_1 AS in0

),

Filter_17 AS (

  SELECT * 
  
  FROM AlteryxSelect_18 AS in0
  
  WHERE i_has_folder = CAST('1' AS INTEGER)

),

`1m_aka_gpdip_edlud_324_1` AS (

  SELECT * 
  
  FROM {{ source('main.rishabh', '1m_aka_gpdip_edlud_324') }}

),

Filter_180 AS (

  SELECT * 
  
  FROM `1m_aka_gpdip_edlud_324_1` AS in0
  
  WHERE name = 'PFLEET_SUB_COUNTRY_ROW_ID'

),

AlteryxSelect_181 AS (

  SELECT 
    i_position AS i_position,
    name AS name,
    r_object_id AS r_object_id,
    CAST(value AS INTEGER) AS value
  
  FROM Filter_180 AS in0

),

Filter_88 AS (

  SELECT * 
  
  FROM Join_119_inner AS in0
  
  WHERE country_name = 'Core Document'

),

Join_6_inner AS (

  SELECT 
    in1.r_object_id AS r_object_id,
    in0.product_name AS product_name,
    in0.sub_country_id AS sub_country_id,
    in0.country_abbreviation AS country_abbreviation,
    in0.country_name AS country_name
  
  FROM Filter_88 AS in0
  INNER JOIN AlteryxSelect_181 AS in1
     ON in0.sub_country_id = in1.value

),

Join_10_inner AS (

  SELECT 
    in1.r_object_id AS r_object_id,
    in0.product_name AS product_name,
    in0.sub_country_id AS sub_country_id,
    in0.country_abbreviation AS country_abbreviation,
    in1.i_chronicle_id AS i_chronicle_id,
    in0.country_name AS country_name
  
  FROM Join_6_inner AS in0
  INNER JOIN Filter_17 AS in1
     ON in0.r_object_id = in1.r_object_id

),

Filter_15 AS (

  SELECT * 
  
  FROM `1m_aka_gpdip_edlud_324_1` AS in0
  
  WHERE CAST(name AS STRING) IN ('GENERIC_NAME', 'PFE_XM_P_COMPOUND_NUM', 'PROPRIETARY_NAME')

),

Join_12_inner AS (

  SELECT 
    in1.name AS name,
    in1.i_position AS i_position,
    in0.r_object_id AS r_object_id,
    in0.product_name AS product_name,
    in0.sub_country_id AS sub_country_id,
    in0.country_abbreviation AS country_abbreviation,
    in1.value AS value,
    in0.i_chronicle_id AS i_chronicle_id,
    in0.country_name AS country_name
  
  FROM Join_10_inner AS in0
  INNER JOIN Filter_15 AS in1
     ON in0.r_object_id = in1.r_object_id

),

Union_89_reformat_1 AS (

  SELECT 
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    CAST(i_chronicle_id AS STRING) AS i_chronicle_id,
    CAST(i_position AS INTEGER) AS i_position,
    CAST(NULL AS STRING) AS is_active,
    CAST(NULL AS STRING) AS is_static,
    CAST(name AS STRING) AS name,
    CAST(NULL AS INTEGER) AS parent_app_country_id,
    product_name AS product_name,
    CAST(r_object_id AS STRING) AS r_object_id,
    sub_country_id AS sub_country_id,
    CAST(NULL AS STRING) AS sub_country_name,
    CAST(value AS STRING) AS value
  
  FROM Join_12_inner AS in0

),

Join_6_left AS (

  SELECT 
    in0.country_name AS country_name,
    in0.is_active AS is_active,
    in0.country_abbreviation AS country_abbreviation,
    in0.parent_app_country_id AS parent_app_country_id,
    in0.sub_country_id AS sub_country_id,
    in0.sub_country_name AS sub_country_name,
    in0.is_static AS is_static,
    in0.product_name AS product_name
  
  FROM Filter_88 AS in0
  ANTI JOIN AlteryxSelect_181 AS in1
     ON in0.sub_country_id = in1.value

),

Union_89_reformat_0 AS (

  SELECT 
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    CAST(NULL AS STRING) AS i_chronicle_id,
    CAST(NULL AS INTEGER) AS i_position,
    CAST(is_active AS STRING) AS is_active,
    CAST(is_static AS STRING) AS is_static,
    CAST(NULL AS STRING) AS name,
    CAST(parent_app_country_id AS INTEGER) AS parent_app_country_id,
    product_name AS product_name,
    CAST(NULL AS STRING) AS r_object_id,
    sub_country_id AS sub_country_id,
    CAST(sub_country_name AS STRING) AS sub_country_name,
    CAST(NULL AS STRING) AS value
  
  FROM Join_6_left AS in0

),

Union_89 AS (

  SELECT * 
  
  FROM Union_89_reformat_0 AS in0
  
  UNION ALL
  
  SELECT * 
  
  FROM Union_89_reformat_1 AS in1

),

CrossTab_23_0 AS (

  SELECT 
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    i_chronicle_id AS i_chronicle_id,
    i_position AS i_position,
    is_active AS is_active,
    is_static AS is_static,
    CASE
      WHEN name IS NULL
        THEN '_Null_'
      ELSE name
    END AS name,
    parent_app_country_id AS parent_app_country_id,
    product_name AS product_name,
    r_object_id AS r_object_id,
    sub_country_id AS sub_country_id,
    sub_country_name AS sub_country_name,
    value AS value
  
  FROM Union_89 AS in0

),

CrossTab_23_1 AS (

  SELECT 
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    i_chronicle_id AS i_chronicle_id,
    i_position AS i_position,
    is_active AS is_active,
    is_static AS is_static,
    REGEXP_REPLACE(name, '[\\s!@#$%^&*(),.?":{}|<>\\[\\]=;/\\-+]', '_') AS name,
    parent_app_country_id AS parent_app_country_id,
    product_name AS product_name,
    r_object_id AS r_object_id,
    sub_country_id AS sub_country_id,
    sub_country_name AS sub_country_name,
    value AS value
  
  FROM CrossTab_23_0 AS in0

),

CrossTab_23_regularActions AS (

  WITH pivot_0 AS (
  
    SELECT 
      product_name,
      country_name,
      country_abbreviation,
      sub_country_id,
      r_object_id,
      i_chronicle_id,
      i_position,
      PFE_XM_P_COMPOUND_NUM AS PFE_XM_P_COMPOUND_NUM_Concat,
      _Null_ AS _Null__Concat,
      GENERIC_NAME AS GENERIC_NAME_Concat,
      PROPRIETARY_NAME AS PROPRIETARY_NAME_Concat
    
    FROM (
      SELECT 
        product_name AS product_name,
        country_name AS country_name,
        country_abbreviation AS country_abbreviation,
        sub_country_id AS sub_country_id,
        r_object_id AS r_object_id,
        i_chronicle_id AS i_chronicle_id,
        i_position AS i_position,
        name AS PIVOT_COL,
        value
      
      FROM CrossTab_23_1
    )
    PIVOT (
      CONCAT_WS(',', COLLECT_LIST(value))
      FOR PIVOT_COL
      IN (
        'PFE_XM_P_COMPOUND_NUM', '_Null_', 'GENERIC_NAME', 'PROPRIETARY_NAME'
      )
    )
    
    GROUP BY 
      product_name, 
      country_name, 
      country_abbreviation, 
      sub_country_id, 
      r_object_id, 
      i_chronicle_id, 
      i_position, 
      PFE_XM_P_COMPOUND_NUM_Concat, 
      _Null__Concat, 
      GENERIC_NAME_Concat, 
      PROPRIETARY_NAME_Concat
  
  ),
  
  pivot_1 AS (
  
    SELECT 
      product_name,
      country_name,
      country_abbreviation,
      sub_country_id,
      r_object_id,
      i_chronicle_id,
      i_position,
      PFE_XM_P_COMPOUND_NUM AS PFE_XM_P_COMPOUND_NUM__dummy_,
      _Null_ AS _Null___dummy_,
      GENERIC_NAME AS GENERIC_NAME__dummy_,
      PROPRIETARY_NAME AS PROPRIETARY_NAME__dummy_
    
    FROM (
      SELECT 
        product_name AS product_name,
        country_name AS country_name,
        country_abbreviation AS country_abbreviation,
        sub_country_id AS sub_country_id,
        r_object_id AS r_object_id,
        i_chronicle_id AS i_chronicle_id,
        i_position AS i_position,
        name AS PIVOT_COL
      
      FROM CrossTab_23_1
    )
    PIVOT (
      1
      FOR PIVOT_COL
      IN (
        'PFE_XM_P_COMPOUND_NUM', '_Null_', 'GENERIC_NAME', 'PROPRIETARY_NAME'
      )
    )
    
    GROUP BY 
      product_name, 
      country_name, 
      country_abbreviation, 
      sub_country_id, 
      r_object_id, 
      i_chronicle_id, 
      i_position, 
      PFE_XM_P_COMPOUND_NUM__dummy_, 
      _Null___dummy_, 
      GENERIC_NAME__dummy_, 
      PROPRIETARY_NAME__dummy_
  
  )
  
  SELECT 
    pivot_0.product_name,
    pivot_0.country_name,
    pivot_0.country_abbreviation,
    pivot_0.sub_country_id,
    pivot_0.r_object_id,
    pivot_0.i_chronicle_id,
    pivot_0.i_position,
    pivot_0.PFE_XM_P_COMPOUND_NUM_Concat,
    pivot_0._Null__Concat,
    pivot_0.GENERIC_NAME_Concat,
    pivot_0.PROPRIETARY_NAME_Concat,
    pivot_1.PFE_XM_P_COMPOUND_NUM__dummy_,
    pivot_1._Null___dummy_,
    pivot_1.GENERIC_NAME__dummy_,
    pivot_1.PROPRIETARY_NAME__dummy_
  
  FROM pivot_0
  JOIN pivot_1
     ON pivot_1.product_name = pivot_0.product_name
    AND pivot_1.country_name = pivot_0.country_name
    AND pivot_1.country_abbreviation = pivot_0.country_abbreviation
    AND pivot_1.sub_country_id = pivot_0.sub_country_id
    AND pivot_1.r_object_id = pivot_0.r_object_id
    AND pivot_1.i_chronicle_id = pivot_0.i_chronicle_id
    AND pivot_1.i_position = pivot_0.i_position

),

CrossTab_23_rename AS (

  SELECT 
    GENERIC_NAME_Concat AS GENERIC_NAME,
    PFE_XM_P_COMPOUND_NUM_Concat AS PFE_XM_P_COMPOUND_NUM,
    PROPRIETARY_NAME_Concat AS PROPRIETARY_NAME,
    _Null__Concat AS _Null_,
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    i_chronicle_id AS i_chronicle_id,
    i_position AS i_position,
    product_name AS product_name,
    r_object_id AS r_object_id,
    sub_country_id AS sub_country_id
  
  FROM CrossTab_23_regularActions AS in0

),

AlteryxSelect_24 AS (

  SELECT 
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    product_name AS product_name,
    sub_country_id AS sub_country_id
  
  FROM CrossTab_23_rename AS in0

),

Unique_28 AS (

  SELECT 
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    product_name AS product_name,
    ROW_NUMBER() OVER (PARTITION BY product_name, country_name, country_abbreviation, sub_country_id ORDER BY product_name NULLS FIRST, country_name NULLS FIRST, country_abbreviation NULLS FIRST, sub_country_id NULLS FIRST) AS row_number,
    sub_country_id AS sub_country_id
  
  FROM AlteryxSelect_24 AS in0

),

Unique_28_filter AS (

  SELECT * 
  
  FROM Unique_28 AS in0
  
  WHERE row_number = 1

),

Filter_38 AS (

  SELECT * 
  
  FROM Unique_28_filter AS in0
  
  WHERE NOT LENGTH(sub_country_id) = 0

),

Sort_34 AS (

  SELECT * 
  
  FROM Filter_38 AS in0
  
  ORDER BY ENCODE(CAST(sub_country_id AS STRING), 'utf-8') ASC

),

Summarize_33 AS (

  SELECT 
    concat(concat_ws('|', collect_list(sub_country_id)), '|') AS sub_country_id_set,
    product_name AS product_name,
    country_name AS country_name,
    country_abbreviation AS country_abbreviation
  
  FROM Sort_34 AS in0
  
  GROUP BY 
    product_name, country_name, country_abbreviation

),

AlteryxSelect_27 AS (

  SELECT 
    PROPRIETARY_NAME AS PROPRIETARY_NAME,
    country_name AS country_name,
    product_name AS product_name
  
  FROM CrossTab_23_rename AS in0

),

Unique_31 AS (

  SELECT 
    PROPRIETARY_NAME AS PROPRIETARY_NAME,
    country_name AS country_name,
    product_name AS product_name,
    ROW_NUMBER() OVER (PARTITION BY product_name, country_name, PROPRIETARY_NAME ORDER BY product_name NULLS FIRST, country_name NULLS FIRST, PROPRIETARY_NAME NULLS FIRST) AS row_number
  
  FROM AlteryxSelect_27 AS in0

),

Unique_31_filter AS (

  SELECT * 
  
  FROM Unique_31 AS in0
  
  WHERE row_number = 1

),

Filter_41 AS (

  SELECT * 
  
  FROM Unique_31_filter AS in0
  
  WHERE NOT LENGTH(PROPRIETARY_NAME) = 0

),

Sort_37 AS (

  SELECT * 
  
  FROM Filter_41 AS in0
  
  ORDER BY ENCODE(CAST(PROPRIETARY_NAME AS STRING), 'utf-8') ASC

),

Summarize_44 AS (

  SELECT 
    concat_ws('|', collect_list(PROPRIETARY_NAME)) AS trade_name_set,
    product_name AS product_name,
    country_name AS country_name
  
  FROM Sort_37 AS in0
  
  GROUP BY 
    product_name, country_name

),

AlteryxSelect_25 AS (

  SELECT 
    GENERIC_NAME AS GENERIC_NAME,
    country_name AS country_name,
    product_name AS product_name
  
  FROM CrossTab_23_rename AS in0

),

Unique_29 AS (

  SELECT 
    GENERIC_NAME AS GENERIC_NAME,
    country_name AS country_name,
    product_name AS product_name,
    ROW_NUMBER() OVER (PARTITION BY product_name, country_name, GENERIC_NAME ORDER BY product_name NULLS FIRST, country_name NULLS FIRST, GENERIC_NAME NULLS FIRST) AS row_number
  
  FROM AlteryxSelect_25 AS in0

),

Unique_29_filter AS (

  SELECT * 
  
  FROM Unique_29 AS in0
  
  WHERE row_number = 1

),

Filter_39 AS (

  SELECT * 
  
  FROM Unique_29_filter AS in0
  
  WHERE NOT LENGTH(GENERIC_NAME) = 0

),

Sort_35 AS (

  SELECT * 
  
  FROM Filter_39 AS in0
  
  ORDER BY ENCODE(CAST(GENERIC_NAME AS STRING), 'utf-8') ASC

),

Summarize_42 AS (

  SELECT 
    concat_ws('|', collect_list(GENERIC_NAME)) AS generic_name_set,
    product_name AS product_name,
    country_name AS country_name
  
  FROM Sort_35 AS in0
  
  GROUP BY 
    product_name, country_name

),

AlteryxSelect_26 AS (

  SELECT 
    PFE_XM_P_COMPOUND_NUM AS PFE_XM_P_COMPOUND_NUM,
    country_name AS country_name,
    product_name AS product_name
  
  FROM CrossTab_23_rename AS in0

),

Unique_30 AS (

  SELECT 
    PFE_XM_P_COMPOUND_NUM AS PFE_XM_P_COMPOUND_NUM,
    country_name AS country_name,
    product_name AS product_name,
    ROW_NUMBER() OVER (PARTITION BY product_name, country_name, PFE_XM_P_COMPOUND_NUM ORDER BY product_name NULLS FIRST, country_name NULLS FIRST, PFE_XM_P_COMPOUND_NUM NULLS FIRST) AS row_number
  
  FROM AlteryxSelect_26 AS in0

),

Unique_30_filter AS (

  SELECT * 
  
  FROM Unique_30 AS in0
  
  WHERE row_number = 1

),

Filter_40 AS (

  SELECT * 
  
  FROM Unique_30_filter AS in0
  
  WHERE NOT LENGTH(PFE_XM_P_COMPOUND_NUM) = 0

),

Sort_36 AS (

  SELECT * 
  
  FROM Filter_40 AS in0
  
  ORDER BY ENCODE(CAST(PFE_XM_P_COMPOUND_NUM AS STRING), 'utf-8') ASC

),

Summarize_43 AS (

  SELECT 
    concat_ws('|', collect_list(PFE_XM_P_COMPOUND_NUM)) AS compound_number_set,
    product_name AS product_name,
    country_name AS country_name
  
  FROM Sort_36 AS in0
  
  GROUP BY 
    product_name, country_name

),

JoinMultiple_45 AS (

  SELECT 
    in1.generic_name_set AS generic_name_set,
    in2.compound_number_set AS compound_number_set,
    in0.product_name AS product_name,
    in3.trade_name_set AS trade_name_set,
    in0.country_abbreviation AS country_abbreviation,
    in0.country_name AS country_name,
    in0.sub_country_id_set AS sub_country_id_set
  
  FROM Summarize_33 AS in0
  FULL JOIN Summarize_42 AS in1
     ON in0.product_name = in1.product_name AND in0.country_name = in1.country_name
  FULL JOIN Summarize_43 AS in2
     ON (
      (coalesce(in0.product_name, in1.product_name) = in2.product_name)
      AND (coalesce(in0.country_name, in1.country_name) = in2.country_name)
    )
  FULL JOIN Summarize_44 AS in3
     ON (
      (coalesce(in0.product_name, coalesce(in1.product_name, in2.product_name)) = in3.product_name)
      AND (coalesce(in0.country_name, coalesce(in1.country_name, in2.country_name)) = in3.country_name)
    )

),

Union_84_reformat_1 AS (

  SELECT 
    compound_number_set AS compound_number_set,
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    generic_name_set AS generic_name_set,
    product_name AS product_name,
    sub_country_id_set AS sub_country_id_set,
    trade_name_set AS trade_name_set
  
  FROM JoinMultiple_45 AS in0

),

Union_84 AS (

  SELECT * 
  
  FROM Union_84_reformat_0 AS in0
  
  UNION ALL
  
  SELECT * 
  
  FROM Union_84_reformat_1 AS in1

),

AlteryxSelect_93 AS (

  SELECT 
    compound_number_set AS compound_number_set,
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    generic_name_set AS generic_name_set,
    product_name AS product_name,
    sub_country_id_set AS sub_country_id_set,
    trade_name_set AS trade_name_set
  
  FROM Union_84 AS in0

),

Formula_94 AS (

  SELECT 
    compound_number_set AS compound_number_set,
    country_abbreviation AS country_abbreviation,
    country_name AS country_name,
    TO_TIMESTAMP(CURRENT_TIMESTAMP) AS extract_date,
    generic_name_set AS generic_name_set,
    product_name AS product_name,
    sub_country_id_set AS sub_country_id_set,
    trade_name_set AS trade_name_set
  
  FROM AlteryxSelect_93 AS in0

)

SELECT *

FROM Formula_94

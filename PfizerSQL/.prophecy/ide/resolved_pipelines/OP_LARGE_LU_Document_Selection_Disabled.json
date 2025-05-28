{
  "id" : "OP_LARGE_LU_Document_Selection_Disabled",
  "metainfo" : {
    "label" : "OP_LARGE_LU_Document_Selection_Disabled",
    "autoLayout" : false,
    "version" : 1,
    "configuration" : {
      "schema" : {
        "type" : "record",
        "fields" : [ ]
      }
    },
    "schedule" : {
      "cron" : "* 0 2 * * * *",
      "timeZone" : "GMT",
      "emailOnSuccess" : false,
      "emailOnFailure" : false,
      "emailOnStart" : false,
      "emails" : [ "email@gmail.com" ],
      "enabled" : false
    }
  },
  "processes" : {
    "Qa8v5IYBMdJkccEw1gofN$$TnPjbaHLO9knDFKy4u6N_" : {
      "id" : "Qa8v5IYBMdJkccEw1gofN$$TnPjbaHLO9knDFKy4u6N_",
      "component" : "OrchestrationTarget",
      "kind" : "RedshiftTarget",
      "metadata" : {
        "label" : "Redshift_1m_aka_gpdip_edlud_302",
        "x" : -1240,
        "y" : -540,
        "phase" : 0
      },
      "properties" : {
        "connector" : {
          "kind" : "redshift",
          "properties" : {
            "id" : "RedShiftTest"
          },
          "type" : "connector"
        },
        "format" : {
          "category" : "table",
          "kind" : "redshift",
          "properties" : {
            "kind" : "redshift",
            "properties" : { },
            "writeMode" : "overwrite"
          }
        },
        "isNew" : false,
        "properties" : {
          "tableFullName" : {
            "database" : {
              "type" : "concat_operation",
              "properties" : {
                "elements" : [ {
                  "type" : "literal",
                  "properties" : {
                    "value" : "prophecy"
                  }
                } ]
              }
            },
            "schema" : {
              "type" : "concat_operation",
              "properties" : {
                "elements" : [ {
                  "type" : "literal",
                  "properties" : {
                    "value" : "dummy"
                  }
                } ]
              }
            },
            "name" : {
              "type" : "concat_operation",
              "properties" : {
                "elements" : [ {
                  "type" : "literal",
                  "properties" : {
                    "value" : "1m_aka_gpdip_edlud_3021m_aka_gpdip_edlud_302_kp"
                  }
                } ]
              }
            }
          }
        }
      },
      "ports" : {
        "inputs" : [ {
          "id" : "__w4r1RZ6Ot2oyU-Vthat$$2ChnrjygNGTi0ufLsBhfH",
          "schema" : {
            "entityType" : "",
            "providerType" : "databricks",
            "fields" : [ {
              "name" : "r_object_id",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "i_position",
              "dataType" : {
                "type" : "Integer"
              }
            }, {
              "name" : "name",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "value",
              "dataType" : {
                "type" : "Integer"
              }
            } ]
          },
          "slug" : "in"
        } ],
        "outputs" : [ ],
        "isCustomOutputSchema" : false
      }
    },
    "Ffqpe0LjRaPuNLknyqsNj$$zo8G7LMtjyLpoNgZToG0G" : {
      "id" : "Ffqpe0LjRaPuNLknyqsNj$$zo8G7LMtjyLpoNgZToG0G",
      "component" : "OrchestrationTarget",
      "kind" : "RedshiftTarget",
      "metadata" : {
        "label" : "Redshift_1m_aka_gpdip_edlud_324",
        "x" : -1240,
        "y" : 40,
        "phase" : 0
      },
      "properties" : {
        "connector" : {
          "kind" : "redshift",
          "properties" : {
            "id" : "RedShiftTest"
          },
          "type" : "connector"
        },
        "format" : {
          "category" : "table",
          "kind" : "redshift",
          "properties" : {
            "kind" : "redshift",
            "properties" : { },
            "writeMode" : "overwrite"
          }
        },
        "isNew" : false,
        "properties" : {
          "tableFullName" : {
            "name" : {
              "type" : "concat_operation",
              "properties" : {
                "elements" : [ {
                  "type" : "literal",
                  "properties" : {
                    "value" : "Redshift_1m_aka_gpdip_edlud_324_kp"
                  }
                } ]
              }
            },
            "database" : {
              "type" : "concat_operation",
              "properties" : {
                "elements" : [ {
                  "type" : "literal",
                  "properties" : {
                    "value" : "prophecy"
                  }
                } ]
              }
            },
            "schema" : {
              "type" : "concat_operation",
              "properties" : {
                "elements" : [ {
                  "type" : "literal",
                  "properties" : {
                    "value" : "dummy"
                  }
                } ]
              }
            }
          }
        }
      },
      "ports" : {
        "inputs" : [ {
          "id" : "1Aa7ORW75rvS2dMN0ak_v$$rw2e1gVr7y9fQEfcOUQtM",
          "schema" : {
            "entityType" : "",
            "providerType" : "databricks",
            "fields" : [ {
              "name" : "r_object_id",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "i_position",
              "dataType" : {
                "type" : "Integer"
              }
            }, {
              "name" : "name",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "value",
              "dataType" : {
                "type" : "Integer"
              }
            } ]
          },
          "slug" : "in"
        } ],
        "outputs" : [ ],
        "isCustomOutputSchema" : false
      }
    },
    "C3luPdDh3WpGzsX2SVu5Q$$PZ_FghW3dn7vHztkx5FWT" : {
      "id" : "C3luPdDh3WpGzsX2SVu5Q$$PZ_FghW3dn7vHztkx5FWT",
      "component" : "Dataset",
      "metadata" : {
        "label" : "1m_aka_gpdip_edlud_298",
        "x" : -500,
        "y" : -140,
        "phase" : 0
      },
      "properties" : {
        "table" : {
          "name" : "1m_aka_gpdip_edlud_298",
          "sourceType" : "Table",
          "sourceName" : "main.rishabh",
          "alias" : "",
          "additionalProperties" : null
        },
        "writeOptions" : {
          "writeMode" : "overwrite"
        }
      },
      "ports" : {
        "inputs" : [ {
          "id" : "JC-s5kLst_ifcyR9Y3W9Q$$sPXLQ5vI_UbCxedVIlPyt",
          "slug" : "in"
        } ],
        "outputs" : [ {
          "id" : "VqHD_PR9m1k-FVdRFBerb$$ttiAfqgryRy00WsDRQTnP",
          "schema" : {
            "entityType" : "",
            "providerType" : "databricks",
            "fields" : [ {
              "name" : "subtype",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "object_name",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "xm_status",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "i_has_folder",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "xm_language",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "r_object_id",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "title",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "i_chronicle_id",
              "dataType" : {
                "type" : "String"
              }
            } ]
          },
          "slug" : "out"
        } ],
        "isCustomOutputSchema" : false
      }
    },
    "iYPCmK9ijxBYtwIscawJu$$yUM2lJoPtJigyQ85aI5SF" : {
      "id" : "iYPCmK9ijxBYtwIscawJu$$yUM2lJoPtJigyQ85aI5SF",
      "component" : "Model",
      "metadata" : {
        "label" : "model_OP_LARGE_LU_Document_Selection_Disabled_AlteryxSelect_294",
        "phase" : 0
      },
      "properties" : {
        "modelName" : "model_OP_LARGE_LU_Document_Selection_Disabled_AlteryxSelect_294"
      },
      "visualMetaInfo" : {
        "visualProcessIds" : [ "iYPCmK9ijxBYtwIscawJu$$yUM2lJoPtJigyQ85aI5SF", "XFuxgQ4WF284X63AtRR1d$$ZU7u4NN5GjUdmh_j_qOdV", "7htL4cIauoWCKjImwjglL$$Upu3HLseF3JvM3EQHaj52", "HI1FO7KZUjSQHkzF9DIXO$$CWG8kKKvnZ704kkqbPHAX", "Ym1qOQRTCvdM3gVKx9dGg$$FBXCZZXusoXIFOLCVE7GA", "LcymqwQa_TuihBlkWQL8k$$mixM18jHEJ6JEnnGq1vhM", "-BQ75ol7RR_moqTGqRtW6$$zjHaxI8rGNnpD7ZoAzV19", "VW3fYMUDy93rkseI2jtnA$$MEMjO7KRm3Uj_RLEexGTY", "C3luPdDh3WpGzsX2SVu5Q$$PZ_FghW3dn7vHztkx5FWT", "prophecy__temp_OP_LARGE_LU_Document_Selection_Disabled_pre_Join_299_inner_0", "k8DKhZlkSAum6vcYpcVwB$$rLssr7SWq1k8QhUYu64Wq", "hklcRxXOXmzlfdrwHefVg$$tlYY9GstvP7AU9TY-fdw_", "prophecy__temp_OP_LARGE_LU_Document_Selection_Disabled_pre_Join_313_inner_0" ],
        "type" : "table",
        "isTemporaryTable" : false
      },
      "ports" : {
        "inputs" : [ {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_AlteryxSelect_294_in_0",
          "slug" : "in_0"
        }, {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_AlteryxSelect_294_in_1",
          "slug" : "in_1"
        }, {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_AlteryxSelect_294_in_2",
          "slug" : "in_2"
        }, {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_AlteryxSelect_294_in_3",
          "slug" : "in_3"
        } ],
        "outputs" : [ {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_AlteryxSelect_294_out_0",
          "slug" : "out_0"
        } ],
        "isCustomOutputSchema" : false
      }
    },
    "XHpFaNmz5HtJrTHPbJC6b$$qGGir5ZU4hnOm6T0F-_Le" : {
      "id" : "XHpFaNmz5HtJrTHPbJC6b$$qGGir5ZU4hnOm6T0F-_Le",
      "component" : "Dataset",
      "metadata" : {
        "label" : "1m_aka_gpdip_edlud_302",
        "x" : -1460,
        "y" : -340,
        "phase" : 0
      },
      "properties" : {
        "table" : {
          "name" : "1m_aka_gpdip_edlud_302",
          "sourceType" : "Table",
          "sourceName" : "main.rishabh",
          "alias" : "",
          "additionalProperties" : null
        },
        "writeOptions" : {
          "writeMode" : "overwrite"
        }
      },
      "ports" : {
        "inputs" : [ {
          "id" : "_wpEhJ5YBCvd2U9w9m1xI$$uuUSYG1_8aodle7LOks2G",
          "slug" : "in"
        } ],
        "outputs" : [ {
          "id" : "8S8488M4GS2D_YEQANeOU$$Ug_Kp76XCHHencoLudVri",
          "schema" : {
            "entityType" : "",
            "providerType" : "databricks",
            "fields" : [ {
              "name" : "r_object_id",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "i_position",
              "dataType" : {
                "type" : "Integer"
              }
            }, {
              "name" : "name",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "value",
              "dataType" : {
                "type" : "Integer"
              }
            } ]
          },
          "slug" : "out"
        } ],
        "isCustomOutputSchema" : false
      }
    },
    "hklcRxXOXmzlfdrwHefVg$$tlYY9GstvP7AU9TY-fdw_" : {
      "id" : "hklcRxXOXmzlfdrwHefVg$$tlYY9GstvP7AU9TY-fdw_",
      "component" : "Dataset",
      "metadata" : {
        "label" : "1m_aka_gpdip_edlud_312",
        "x" : -640,
        "y" : 320,
        "phase" : 0
      },
      "properties" : {
        "table" : {
          "name" : "1m_aka_gpdip_edlud_312",
          "sourceType" : "Table",
          "sourceName" : "main.rishabh",
          "alias" : "",
          "additionalProperties" : null
        },
        "writeOptions" : {
          "writeMode" : "overwrite"
        }
      },
      "ports" : {
        "inputs" : [ {
          "id" : "oAFN_FryhgYsmHCGfDbIl$$Dw1EYVFcoCg9T-21bu1ni",
          "slug" : "in"
        } ],
        "outputs" : [ {
          "id" : "CRtOXotVjO9KtuaQYQnbi$$EGGGEYgZASvYxYSYgnCbV",
          "schema" : {
            "entityType" : "",
            "providerType" : "databricks",
            "fields" : [ {
              "name" : "subtype",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "object_name",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "xm_status",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "i_has_folder",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "xm_language",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "r_object_id",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "title",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "i_chronicle_id",
              "dataType" : {
                "type" : "String"
              }
            } ]
          },
          "slug" : "out"
        } ],
        "isCustomOutputSchema" : false
      }
    },
    "S6V-Vg9w5wUnyq9r4N4dy$$2Hz_o5jeWu07I9Z_Hr8dR" : {
      "id" : "S6V-Vg9w5wUnyq9r4N4dy$$2Hz_o5jeWu07I9Z_Hr8dR",
      "component" : "Model",
      "metadata" : {
        "label" : "model_OP_LARGE_LU_Document_Selection_Disabled_Cleanse_290",
        "phase" : 0
      },
      "properties" : {
        "modelName" : "model_OP_LARGE_LU_Document_Selection_Disabled_Cleanse_290"
      },
      "visualMetaInfo" : {
        "visualProcessIds" : [ "prophecy__temp_OP_LARGE_LU_Document_Selection_Disabled_post_Cleanse_290_0", "S6V-Vg9w5wUnyq9r4N4dy$$2Hz_o5jeWu07I9Z_Hr8dR", "yA3zdZo1kT9jvNLQloqoG$$42RFuHOI4-BmkQQ9YpDIs" ],
        "type" : "table",
        "isTemporaryTable" : true
      },
      "ports" : {
        "inputs" : [ {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_Cleanse_290_in_0",
          "slug" : "in_0"
        } ],
        "outputs" : [ {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_Cleanse_290_out_0",
          "slug" : "out_0"
        } ],
        "isCustomOutputSchema" : false
      }
    },
    "TW2R--xvp23F0RcnfyM8u$$u2vnfBValbDlURE2hkJtC" : {
      "id" : "TW2R--xvp23F0RcnfyM8u$$u2vnfBValbDlURE2hkJtC",
      "component" : "Dataset",
      "metadata" : {
        "label" : "1m_aka_gpdip_edlud_324",
        "x" : -1420,
        "y" : 160,
        "phase" : 0
      },
      "properties" : {
        "table" : {
          "name" : "1m_aka_gpdip_edlud_324",
          "sourceType" : "Table",
          "sourceName" : "main.rishabh",
          "alias" : "",
          "additionalProperties" : null
        },
        "writeOptions" : {
          "writeMode" : "overwrite"
        }
      },
      "ports" : {
        "inputs" : [ {
          "id" : "-K4laRAbI3RUCd3Il6RgD$$azj9VdMQnBEdZ7GCAfibV",
          "slug" : "in"
        } ],
        "outputs" : [ {
          "id" : "UCKEd2HzdMLLLYZJ9XIRK$$eyPvzJ8MNfEk3RRz4-8WN",
          "schema" : {
            "entityType" : "",
            "providerType" : "databricks",
            "fields" : [ {
              "name" : "r_object_id",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "i_position",
              "dataType" : {
                "type" : "Integer"
              }
            }, {
              "name" : "name",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "value",
              "dataType" : {
                "type" : "Integer"
              }
            } ]
          },
          "slug" : "out"
        } ],
        "isCustomOutputSchema" : false
      }
    },
    "vyFFjUBgY0IwRKfm2JEyz$$nxiLeMiAXaeoWF8kyw9cV" : {
      "id" : "vyFFjUBgY0IwRKfm2JEyz$$nxiLeMiAXaeoWF8kyw9cV",
      "component" : "OrchestrationTarget",
      "kind" : "RedshiftTarget",
      "metadata" : {
        "label" : "Redshift_1m_aka_gpdip_edlud_2891m_aka_gpdip_edlud_289",
        "x" : -920,
        "y" : -540,
        "phase" : 0
      },
      "properties" : {
        "connector" : {
          "kind" : "redshift",
          "properties" : {
            "id" : "RedShiftTest"
          },
          "type" : "connector"
        },
        "format" : {
          "category" : "table",
          "kind" : "redshift",
          "properties" : {
            "kind" : "redshift",
            "properties" : { },
            "writeMode" : "overwrite"
          }
        },
        "isNew" : false,
        "properties" : {
          "tableFullName" : {
            "database" : {
              "type" : "concat_operation",
              "properties" : {
                "elements" : [ {
                  "type" : "literal",
                  "properties" : {
                    "value" : "prophecy"
                  }
                } ]
              }
            },
            "schema" : {
              "type" : "concat_operation",
              "properties" : {
                "elements" : [ {
                  "type" : "literal",
                  "properties" : {
                    "value" : "dummy"
                  }
                } ]
              }
            },
            "name" : {
              "type" : "concat_operation",
              "properties" : {
                "elements" : [ {
                  "type" : "literal",
                  "properties" : {
                    "value" : "Redshift_1m_aka_gpdip_edlud_2891m_aka_gpdip_edlud_289_kp"
                  }
                } ]
              }
            }
          }
        }
      },
      "ports" : {
        "inputs" : [ {
          "id" : "EPEj13a1-BtB43dtglZnO$$Br952NSgFUxy8i6qcjDQH",
          "schema" : {
            "entityType" : "",
            "providerType" : "databricks",
            "fields" : [ {
              "name" : "is_active",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "is_static",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "extract_date",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "product_name",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "country_abbreviation",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "app_country_id",
              "dataType" : {
                "type" : "Integer"
              }
            }, {
              "name" : "country_name",
              "dataType" : {
                "type" : "String"
              }
            } ]
          },
          "slug" : "in"
        } ],
        "outputs" : [ ],
        "isCustomOutputSchema" : false
      }
    },
    "ZczzBHr9ciEubIYVuTI4O$$8eTbB_PXqJ_1DIDxbC26h" : {
      "id" : "ZczzBHr9ciEubIYVuTI4O$$8eTbB_PXqJ_1DIDxbC26h",
      "component" : "Model",
      "metadata" : {
        "label" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_310_inner",
        "phase" : 0
      },
      "properties" : {
        "modelName" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_310_inner"
      },
      "visualMetaInfo" : {
        "visualProcessIds" : [ "prophecy__temp_OP_LARGE_LU_Document_Selection_Disabled_pre_Join_299_inner_0", "ZczzBHr9ciEubIYVuTI4O$$8eTbB_PXqJ_1DIDxbC26h", "prophecy__temp_OP_LARGE_LU_Document_Selection_Disabled_post_Cleanse_290_0", "hstl_3qXa1fMXHRrim-UQ$$uWKvHD2pXUIepQBs-Tjsn", "XHpFaNmz5HtJrTHPbJC6b$$qGGir5ZU4hnOm6T0F-_Le" ],
        "type" : "table",
        "isTemporaryTable" : true
      },
      "ports" : {
        "inputs" : [ {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_310_inner_in_0",
          "slug" : "in_0"
        }, {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_310_inner_in_1",
          "slug" : "in_1"
        }, {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_310_inner_in_2",
          "slug" : "in_2"
        } ],
        "outputs" : [ {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_310_inner_out_0",
          "slug" : "out_0"
        } ],
        "isCustomOutputSchema" : false
      }
    },
    "bJyAjQBMKKhkok463ohtY$$tsJanPQtML5yjQnnG4ypr" : {
      "id" : "bJyAjQBMKKhkok463ohtY$$tsJanPQtML5yjQnnG4ypr",
      "component" : "Model",
      "metadata" : {
        "label" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_318_inner",
        "phase" : 0
      },
      "properties" : {
        "modelName" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_318_inner"
      },
      "visualMetaInfo" : {
        "visualProcessIds" : [ "prophecy__temp_OP_LARGE_LU_Document_Selection_Disabled_pre_Join_313_inner_0", "bJyAjQBMKKhkok463ohtY$$tsJanPQtML5yjQnnG4ypr", "prophecy__temp_OP_LARGE_LU_Document_Selection_Disabled_post_Cleanse_290_0", "ZOILVftx2Qt8DpkukVxLu$$gDIxhXxRIsJW_SlVGs6s3", "TW2R--xvp23F0RcnfyM8u$$u2vnfBValbDlURE2hkJtC" ],
        "type" : "table",
        "isTemporaryTable" : true
      },
      "ports" : {
        "inputs" : [ {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_318_inner_in_0",
          "slug" : "in_0"
        }, {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_318_inner_in_1",
          "slug" : "in_1"
        }, {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_318_inner_in_2",
          "slug" : "in_2"
        } ],
        "outputs" : [ {
          "id" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_318_inner_out_0",
          "slug" : "out_0"
        } ],
        "isCustomOutputSchema" : false
      }
    },
    "yA3zdZo1kT9jvNLQloqoG$$42RFuHOI4-BmkQQ9YpDIs" : {
      "id" : "yA3zdZo1kT9jvNLQloqoG$$42RFuHOI4-BmkQQ9YpDIs",
      "component" : "Dataset",
      "metadata" : {
        "label" : "1m_aka_gpdip_edlud_289",
        "x" : -980,
        "y" : -160,
        "phase" : 0
      },
      "properties" : {
        "writeOptions" : {
          "writeMode" : "overwrite"
        },
        "table" : {
          "name" : "1m_aka_gpdip_edlud_289",
          "sourceType" : "Table",
          "sourceName" : "main.rishabh",
          "alias" : "",
          "additionalProperties" : null
        }
      },
      "ports" : {
        "inputs" : [ {
          "id" : "gr7yH0_DrG7QcTqpjoXDs$$snxdOIioB68EKVcH4BYZv",
          "slug" : "in"
        } ],
        "outputs" : [ {
          "id" : "NMANCAsByh97fHreBZ5ia$$GT9TY_TZtpHWv16C5ql4_",
          "schema" : {
            "entityType" : "",
            "providerType" : "databricks",
            "fields" : [ {
              "name" : "is_active",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "is_static",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "extract_date",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "product_name",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "country_abbreviation",
              "dataType" : {
                "type" : "String"
              }
            }, {
              "name" : "app_country_id",
              "dataType" : {
                "type" : "Integer"
              }
            }, {
              "name" : "country_name",
              "dataType" : {
                "type" : "String"
              }
            } ]
          },
          "slug" : "out"
        } ],
        "isCustomOutputSchema" : false
      }
    }
  },
  "connections" : [ {
    "id" : "z8hFgv82pL5XOjxcRppfL",
    "source" : "XHpFaNmz5HtJrTHPbJC6b$$qGGir5ZU4hnOm6T0F-_Le",
    "sourcePort" : "8S8488M4GS2D_YEQANeOU$$Ug_Kp76XCHHencoLudVri",
    "target" : "Qa8v5IYBMdJkccEw1gofN$$TnPjbaHLO9knDFKy4u6N_",
    "targetPort" : "__w4r1RZ6Ot2oyU-Vthat$$2ChnrjygNGTi0ufLsBhfH"
  }, {
    "id" : "qLKcAXA9F8FGJX0zni-Hg",
    "source" : "TW2R--xvp23F0RcnfyM8u$$u2vnfBValbDlURE2hkJtC",
    "sourcePort" : "UCKEd2HzdMLLLYZJ9XIRK$$eyPvzJ8MNfEk3RRz4-8WN",
    "target" : "Ffqpe0LjRaPuNLknyqsNj$$zo8G7LMtjyLpoNgZToG0G",
    "targetPort" : "1Aa7ORW75rvS2dMN0ak_v$$rw2e1gVr7y9fQEfcOUQtM"
  }, {
    "id" : "Y8bTBqSBeuaahiIGr6HNQ",
    "source" : "yA3zdZo1kT9jvNLQloqoG$$42RFuHOI4-BmkQQ9YpDIs",
    "sourcePort" : "NMANCAsByh97fHreBZ5ia$$GT9TY_TZtpHWv16C5ql4_",
    "target" : "vyFFjUBgY0IwRKfm2JEyz$$nxiLeMiAXaeoWF8kyw9cV",
    "targetPort" : "EPEj13a1-BtB43dtglZnO$$Br952NSgFUxy8i6qcjDQH"
  }, {
    "id" : "KXJ7a2LfGh28gZ0GMVVo-",
    "source" : "hklcRxXOXmzlfdrwHefVg$$tlYY9GstvP7AU9TY-fdw_",
    "sourcePort" : "CRtOXotVjO9KtuaQYQnbi$$EGGGEYgZASvYxYSYgnCbV",
    "target" : "iYPCmK9ijxBYtwIscawJu$$yUM2lJoPtJigyQ85aI5SF",
    "targetPort" : "model_OP_LARGE_LU_Document_Selection_Disabled_AlteryxSelect_294_in_0"
  }, {
    "id" : "FmGXtKqABPWLOqbt9_vzS",
    "source" : "C3luPdDh3WpGzsX2SVu5Q$$PZ_FghW3dn7vHztkx5FWT",
    "sourcePort" : "VqHD_PR9m1k-FVdRFBerb$$ttiAfqgryRy00WsDRQTnP",
    "target" : "iYPCmK9ijxBYtwIscawJu$$yUM2lJoPtJigyQ85aI5SF",
    "targetPort" : "model_OP_LARGE_LU_Document_Selection_Disabled_AlteryxSelect_294_in_1"
  }, {
    "id" : "rOyAwOES2mBKRRfZTioC4",
    "source" : "XHpFaNmz5HtJrTHPbJC6b$$qGGir5ZU4hnOm6T0F-_Le",
    "sourcePort" : "8S8488M4GS2D_YEQANeOU$$Ug_Kp76XCHHencoLudVri",
    "target" : "ZczzBHr9ciEubIYVuTI4O$$8eTbB_PXqJ_1DIDxbC26h",
    "targetPort" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_310_inner_in_1"
  }, {
    "id" : "wC5BUEqqZqcmV_8x471-u",
    "source" : "TW2R--xvp23F0RcnfyM8u$$u2vnfBValbDlURE2hkJtC",
    "sourcePort" : "UCKEd2HzdMLLLYZJ9XIRK$$eyPvzJ8MNfEk3RRz4-8WN",
    "target" : "bJyAjQBMKKhkok463ohtY$$tsJanPQtML5yjQnnG4ypr",
    "targetPort" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_318_inner_in_1"
  }, {
    "id" : "rhjT5SJ14fiMqhtzOpQGQ",
    "source" : "yA3zdZo1kT9jvNLQloqoG$$42RFuHOI4-BmkQQ9YpDIs",
    "sourcePort" : "NMANCAsByh97fHreBZ5ia$$GT9TY_TZtpHWv16C5ql4_",
    "target" : "S6V-Vg9w5wUnyq9r4N4dy$$2Hz_o5jeWu07I9Z_Hr8dR",
    "targetPort" : "model_OP_LARGE_LU_Document_Selection_Disabled_Cleanse_290_in_0"
  }, {
    "id" : "conn_S6V-Vg9w5wUnyq9r4N4dy$$2Hz_o5jeWu07I9Z_Hr8dR_ZczzBHr9ciEubIYVuTI4O$$8eTbB_PXqJ_1DIDxbC26h",
    "source" : "S6V-Vg9w5wUnyq9r4N4dy$$2Hz_o5jeWu07I9Z_Hr8dR",
    "sourcePort" : "model_OP_LARGE_LU_Document_Selection_Disabled_Cleanse_290_out_0",
    "target" : "ZczzBHr9ciEubIYVuTI4O$$8eTbB_PXqJ_1DIDxbC26h",
    "targetPort" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_310_inner_in_0"
  }, {
    "id" : "conn_S6V-Vg9w5wUnyq9r4N4dy$$2Hz_o5jeWu07I9Z_Hr8dR_bJyAjQBMKKhkok463ohtY$$tsJanPQtML5yjQnnG4ypr",
    "source" : "S6V-Vg9w5wUnyq9r4N4dy$$2Hz_o5jeWu07I9Z_Hr8dR",
    "sourcePort" : "model_OP_LARGE_LU_Document_Selection_Disabled_Cleanse_290_out_0",
    "target" : "bJyAjQBMKKhkok463ohtY$$tsJanPQtML5yjQnnG4ypr",
    "targetPort" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_318_inner_in_0"
  }, {
    "id" : "conn_ZczzBHr9ciEubIYVuTI4O$$8eTbB_PXqJ_1DIDxbC26h_XFuxgQ4WF284X63AtRR1d$$ZU7u4NN5GjUdmh_j_qOdV",
    "source" : "ZczzBHr9ciEubIYVuTI4O$$8eTbB_PXqJ_1DIDxbC26h",
    "sourcePort" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_310_inner_out_0",
    "target" : "iYPCmK9ijxBYtwIscawJu$$yUM2lJoPtJigyQ85aI5SF",
    "targetPort" : "model_OP_LARGE_LU_Document_Selection_Disabled_AlteryxSelect_294_in_0"
  }, {
    "id" : "conn_bJyAjQBMKKhkok463ohtY$$tsJanPQtML5yjQnnG4ypr_XFuxgQ4WF284X63AtRR1d$$ZU7u4NN5GjUdmh_j_qOdV",
    "source" : "bJyAjQBMKKhkok463ohtY$$tsJanPQtML5yjQnnG4ypr",
    "sourcePort" : "model_OP_LARGE_LU_Document_Selection_Disabled_Join_318_inner_out_0",
    "target" : "iYPCmK9ijxBYtwIscawJu$$yUM2lJoPtJigyQ85aI5SF",
    "targetPort" : "model_OP_LARGE_LU_Document_Selection_Disabled_AlteryxSelect_294_in_0"
  } ],
  "component" : "Pipeline"
}
{
  "id" : "LU_Document_Selection_Disabled",
  "metainfo" : {
    "label" : "LU_Document_Selection_Disabled",
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
    "orhEzAnIfeIWtzPH8efsf$$sYj9NIW8TZxe3IzaZVCbo" : {
      "id" : "orhEzAnIfeIWtzPH8efsf$$sYj9NIW8TZxe3IzaZVCbo",
      "component" : "Model",
      "metadata" : {
        "label" : "model_LU_Document_Selection_Disabled_Join_310_inner",
        "phase" : 0
      },
      "properties" : {
        "modelName" : "model_LU_Document_Selection_Disabled_Join_310_inner"
      },
      "visualMetaInfo" : {
        "visualProcessIds" : [ "prophecy__temp_LU_Document_Selection_Disabled_pre_Join_299_inner_0", "orhEzAnIfeIWtzPH8efsf$$sYj9NIW8TZxe3IzaZVCbo", "prophecy__temp_LU_Document_Selection_Disabled_post_Cleanse_290_0", "W1HXwbDZTQSsX_XURgTXp$$1TGWb6s0yKKUWxYiaWKHt", "VJqBszLJ8G50XmOtKdv0n$$d7mDMcjRaznycHeZn7K1C", "zge7W52Vo8l32uottvRat$$40F8b4P13HNF2KjfObK83", "xk3HyOyZIIgbGnWs7_g9B$$IFwcr6dG4D1VepTNYyIcQ", "YPpYmqOTlKJqLokPmPY5P$$D9qcuhUIgTZXisfMR3h2t", "16HV6BWR3P1y70Mwot7b9$$WJd8iCk44OoAEZsWnQ_Qx", "OdUAkMhS0a4wnDyNqIW8T$$UXpdp3X8e-xXkKKfYLx4g", "16HV6BWR3P1y70Mwot7b9$$WJd8iCk44OoAEZsWnQ_Qx" ],
        "type" : "table",
        "isTemporaryTable" : true
      },
      "ports" : {
        "inputs" : [ {
          "id" : "model_LU_Document_Selection_Disabled_Join_310_inner_in_0",
          "slug" : "in_0"
        }, {
          "id" : "model_LU_Document_Selection_Disabled_Join_310_inner_in_1",
          "slug" : "in_1"
        }, {
          "id" : "model_LU_Document_Selection_Disabled_Join_310_inner_in_2",
          "slug" : "in_2"
        }, {
          "id" : "model_LU_Document_Selection_Disabled_Join_310_inner_in_3",
          "slug" : "in_3"
        } ],
        "outputs" : [ {
          "id" : "model_LU_Document_Selection_Disabled_Join_310_inner_out_0",
          "slug" : "out_0"
        } ],
        "isCustomOutputSchema" : false
      }
    },
    "Ma1e7h4Eeh25V5H65TLRh$$VPx97wqbb2u4K83dKvk_S" : {
      "id" : "Ma1e7h4Eeh25V5H65TLRh$$VPx97wqbb2u4K83dKvk_S",
      "component" : "Model",
      "metadata" : {
        "label" : "model_LU_Document_Selection_Disabled_AlteryxSelect_294",
        "phase" : 0
      },
      "properties" : {
        "modelName" : "model_LU_Document_Selection_Disabled_AlteryxSelect_294"
      },
      "visualMetaInfo" : {
        "visualProcessIds" : [ "Ma1e7h4Eeh25V5H65TLRh$$VPx97wqbb2u4K83dKvk_S", "IE9XzV6UhcQC6EUQw4gi9$$pIj95Ohf4Bg0_ZLtUQ-3_", "eA4IujEBA-jsWES6XyDI6$$Oq-69O7Aw823vgw2QyxL7", "5kQ3HBGgCTtj2ksOJR3P1$$DmwLPaApcdMSbRHsMFrRE", "3ky_klbHhw7-WI3KLl5jg$$oKFQfH6ooI_BN3FnOV6aV", "rD34bpNEVB9q4KYm5gDTe$$CT1o_HcoiLXlmHOLhXFcQ", "D6NY94iMBCoK2TFctUAcA$$GvcByMislQHbo_XO1I5qf", "kPs93rfRYpb9z4MzMDodE$$PYjgEAMsCDVRrq31K3TtB", "nrq6soSQLvgmVueWOjpyV$$rhXCd-n18K613G3LwNuXG", "C3TAHaOHkAMMH5SgCf-H6$$NMZWuN2K-MqhhIU-YNf19", "prophecy__temp_LU_Document_Selection_Disabled_pre_Join_299_inner_0", "fv2hjXkFmdwctj-lFs5aB$$qnT6KOrWN_t3YvsLUXtvE", "3yTPdrW0cEZmNBCmrt-uO$$VnLM3_Gcfo4v_a-sGTDiq", "prophecy__temp_LU_Document_Selection_Disabled_pre_Join_313_inner_0" ],
        "type" : "table",
        "isTemporaryTable" : false
      },
      "ports" : {
        "inputs" : [ {
          "id" : "model_LU_Document_Selection_Disabled_AlteryxSelect_294_in_0",
          "slug" : "in_0"
        }, {
          "id" : "model_LU_Document_Selection_Disabled_AlteryxSelect_294_in_1",
          "slug" : "in_1"
        }, {
          "id" : "model_LU_Document_Selection_Disabled_AlteryxSelect_294_in_2",
          "slug" : "in_2"
        }, {
          "id" : "model_LU_Document_Selection_Disabled_AlteryxSelect_294_in_3",
          "slug" : "in_3"
        } ],
        "outputs" : [ {
          "id" : "model_LU_Document_Selection_Disabled_AlteryxSelect_294_out_0",
          "slug" : "out_0"
        } ],
        "isCustomOutputSchema" : false
      }
    },
    "16HV6BWR3P1y70Mwot7b9$$WJd8iCk44OoAEZsWnQ_Qx" : {
      "id" : "16HV6BWR3P1y70Mwot7b9$$WJd8iCk44OoAEZsWnQ_Qx",
      "component" : "Dataset",
      "metadata" : {
        "label" : "1k_aka_gpdip_edlud_302",
        "x" : -1540,
        "y" : -760,
        "phase" : 0
      },
      "properties" : {
        "table" : {
          "name" : "1k_aka_gpdip_edlud_302",
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
          "id" : "XP03HB7qdE09fKi6KVesy$$T2Quhl6KDbP_tTrbKn8E_",
          "slug" : "in"
        } ],
        "outputs" : [ {
          "id" : "yDbRTQsihOuc-LXgEJYCa$$XHi_6nUdslbcMukAfSRv5",
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
    "3yTPdrW0cEZmNBCmrt-uO$$VnLM3_Gcfo4v_a-sGTDiq" : {
      "id" : "3yTPdrW0cEZmNBCmrt-uO$$VnLM3_Gcfo4v_a-sGTDiq",
      "component" : "Dataset",
      "metadata" : {
        "label" : "1k_aka_gpdip_edlud_312",
        "x" : -480,
        "y" : 40,
        "phase" : 0
      },
      "properties" : {
        "table" : {
          "name" : "1k_aka_gpdip_edlud_312",
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
          "id" : "8D-riQpShRZP_5NbpZe6N$$vB6f4-fC4cV6FQhUE5GNT",
          "slug" : "in"
        } ],
        "outputs" : [ {
          "id" : "aGfBAK5YLDunVipq7nhTa$$DGokabDH0JvwodPZUJy6c",
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
    "rFPubDwQxu_gGFR7Za6RE$$KkB0NsoUYpZ6SiQSsckDT" : {
      "id" : "rFPubDwQxu_gGFR7Za6RE$$KkB0NsoUYpZ6SiQSsckDT",
      "component" : "Dataset",
      "metadata" : {
        "label" : "1k_aka_gpdip_edlud_324",
        "x" : -1580,
        "y" : -20,
        "phase" : 0
      },
      "properties" : {
        "table" : {
          "name" : "1k_aka_gpdip_edlud_324",
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
          "id" : "eP4oEbAx0LEhBtVRRCci4$$qPV0F5DShq-Og4w0eJLQu",
          "slug" : "in"
        } ],
        "outputs" : [ {
          "id" : "lmfMZPz8Vi_FufzLxG4mi$$umqT5UdCGb8kvQLqRGbgc",
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
    "C3TAHaOHkAMMH5SgCf-H6$$NMZWuN2K-MqhhIU-YNf19" : {
      "id" : "C3TAHaOHkAMMH5SgCf-H6$$NMZWuN2K-MqhhIU-YNf19",
      "component" : "Dataset",
      "metadata" : {
        "label" : "1k_aka_gpdip_edlud_298",
        "x" : -480,
        "y" : -300,
        "phase" : 0
      },
      "properties" : {
        "table" : {
          "name" : "1k_aka_gpdip_edlud_298",
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
          "id" : "gc9EtkaPZvOM6vv52c_2r$$s15U_uzKgGR4FletH19zN",
          "slug" : "in"
        } ],
        "outputs" : [ {
          "id" : "t7LyzdAByu-1nVF9f-vp0$$y0twsrQ7iO1H08fgLc4CD",
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
    "a3BrUrXQaR72IB20IWM2c$$xr-d67wFVbOafiR4R_sle" : {
      "id" : "a3BrUrXQaR72IB20IWM2c$$xr-d67wFVbOafiR4R_sle",
      "component" : "Dataset",
      "metadata" : {
        "label" : "1k_aka_gpdip_edlud_289",
        "x" : -1260,
        "y" : -320,
        "phase" : 0
      },
      "properties" : {
        "table" : {
          "name" : "1k_aka_gpdip_edlud_289",
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
          "id" : "a_lwyJ5Q7RdDIT0k44tax$$HHz3iEyYXz3j98bzZ8PHI",
          "slug" : "in"
        } ],
        "outputs" : [ {
          "id" : "4-cvLQPcqLtLSH82VmHLO$$KXB6_nTcO1qdnliQ1cvdH",
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
    },
    "P3GtSo3tjK-RG_BuYjuSm$$n4l8jIpkZJqUKkxY-wC9t" : {
      "id" : "P3GtSo3tjK-RG_BuYjuSm$$n4l8jIpkZJqUKkxY-wC9t",
      "component" : "Model",
      "metadata" : {
        "label" : "model_LU_Document_Selection_Disabled_Join_318_inner",
        "phase" : 0
      },
      "properties" : {
        "modelName" : "model_LU_Document_Selection_Disabled_Join_318_inner"
      },
      "visualMetaInfo" : {
        "visualProcessIds" : [ "prophecy__temp_LU_Document_Selection_Disabled_pre_Join_313_inner_0", "P3GtSo3tjK-RG_BuYjuSm$$n4l8jIpkZJqUKkxY-wC9t", "prophecy__temp_LU_Document_Selection_Disabled_post_Cleanse_290_0", "xH2bNiWxCCvmhhlU1S71B$$EQBBlVEI1YWoqpxcRKVxx", "i0jZFXRxMvBP2FxgjqzX6$$nO-EYblQnGA663TGwq2y9", "AYpNsR2_VlcShxr6-jXlF$$aOO3whGW0y69VI9EKqDtw", "aPEfTBOtlg8V_BW0cmTiS$$aTwIdizQ7GWyhCYCD1we7", "eRciHFeoeAjVAIdEPUb2o$$s653tZcU3dGFAdRZ9xVpZ", "rFPubDwQxu_gGFR7Za6RE$$KkB0NsoUYpZ6SiQSsckDT", "bOfhhR1vVwlfW9M737b9j$$GVj9YC4QbYuZNWilxJtsV", "rFPubDwQxu_gGFR7Za6RE$$KkB0NsoUYpZ6SiQSsckDT" ],
        "type" : "table",
        "isTemporaryTable" : true
      },
      "ports" : {
        "inputs" : [ {
          "id" : "model_LU_Document_Selection_Disabled_Join_318_inner_in_0",
          "slug" : "in_0"
        }, {
          "id" : "model_LU_Document_Selection_Disabled_Join_318_inner_in_1",
          "slug" : "in_1"
        }, {
          "id" : "model_LU_Document_Selection_Disabled_Join_318_inner_in_2",
          "slug" : "in_2"
        }, {
          "id" : "model_LU_Document_Selection_Disabled_Join_318_inner_in_3",
          "slug" : "in_3"
        } ],
        "outputs" : [ {
          "id" : "model_LU_Document_Selection_Disabled_Join_318_inner_out_0",
          "slug" : "out_0"
        } ],
        "isCustomOutputSchema" : false
      }
    },
    "LkRPP98NcWsswIkH8LUoZ$$7MRi-Jvqs2YMMGpIaG6iV" : {
      "id" : "LkRPP98NcWsswIkH8LUoZ$$7MRi-Jvqs2YMMGpIaG6iV",
      "component" : "Model",
      "metadata" : {
        "label" : "model_LU_Document_Selection_Disabled_Cleanse_290",
        "phase" : 0
      },
      "properties" : {
        "modelName" : "model_LU_Document_Selection_Disabled_Cleanse_290"
      },
      "visualMetaInfo" : {
        "visualProcessIds" : [ "prophecy__temp_LU_Document_Selection_Disabled_post_Cleanse_290_0", "LkRPP98NcWsswIkH8LUoZ$$7MRi-Jvqs2YMMGpIaG6iV", "a3BrUrXQaR72IB20IWM2c$$xr-d67wFVbOafiR4R_sle" ],
        "type" : "table",
        "isTemporaryTable" : true
      },
      "ports" : {
        "inputs" : [ {
          "id" : "model_LU_Document_Selection_Disabled_Cleanse_290_in_0",
          "slug" : "in_0"
        } ],
        "outputs" : [ {
          "id" : "model_LU_Document_Selection_Disabled_Cleanse_290_out_0",
          "slug" : "out_0"
        } ],
        "isCustomOutputSchema" : false
      }
    }
  },
  "connections" : [ {
    "id" : "OoIELaWcEknJXqZTnknxA",
    "source" : "C3TAHaOHkAMMH5SgCf-H6$$NMZWuN2K-MqhhIU-YNf19",
    "sourcePort" : "t7LyzdAByu-1nVF9f-vp0$$y0twsrQ7iO1H08fgLc4CD",
    "target" : "Ma1e7h4Eeh25V5H65TLRh$$VPx97wqbb2u4K83dKvk_S",
    "targetPort" : "model_LU_Document_Selection_Disabled_AlteryxSelect_294_in_0"
  }, {
    "id" : "4wxxI6JAWMWIAlj3QsbzG$$R4rFCC35pIsrHP0nQ_tc1",
    "source" : "3yTPdrW0cEZmNBCmrt-uO$$VnLM3_Gcfo4v_a-sGTDiq",
    "sourcePort" : "aGfBAK5YLDunVipq7nhTa$$DGokabDH0JvwodPZUJy6c",
    "target" : "Ma1e7h4Eeh25V5H65TLRh$$VPx97wqbb2u4K83dKvk_S",
    "targetPort" : "model_LU_Document_Selection_Disabled_AlteryxSelect_294_in_1"
  }, {
    "id" : "miVEFMox3HKeinJj8wgfG",
    "source" : "16HV6BWR3P1y70Mwot7b9$$WJd8iCk44OoAEZsWnQ_Qx",
    "sourcePort" : "yDbRTQsihOuc-LXgEJYCa$$XHi_6nUdslbcMukAfSRv5",
    "target" : "orhEzAnIfeIWtzPH8efsf$$sYj9NIW8TZxe3IzaZVCbo",
    "targetPort" : "model_LU_Document_Selection_Disabled_Join_310_inner_in_1"
  }, {
    "id" : "ABW7hP_U6q_ZDeJPsuhd0",
    "source" : "16HV6BWR3P1y70Mwot7b9$$WJd8iCk44OoAEZsWnQ_Qx",
    "sourcePort" : "yDbRTQsihOuc-LXgEJYCa$$XHi_6nUdslbcMukAfSRv5",
    "target" : "orhEzAnIfeIWtzPH8efsf$$sYj9NIW8TZxe3IzaZVCbo",
    "targetPort" : "model_LU_Document_Selection_Disabled_Join_310_inner_in_2"
  }, {
    "id" : "RMZVg0FVKDQiVYLWDLQbt",
    "source" : "rFPubDwQxu_gGFR7Za6RE$$KkB0NsoUYpZ6SiQSsckDT",
    "sourcePort" : "lmfMZPz8Vi_FufzLxG4mi$$umqT5UdCGb8kvQLqRGbgc",
    "target" : "P3GtSo3tjK-RG_BuYjuSm$$n4l8jIpkZJqUKkxY-wC9t",
    "targetPort" : "model_LU_Document_Selection_Disabled_Join_318_inner_in_1"
  }, {
    "id" : "04LChkoBagbqtjJ6f9fk5",
    "source" : "rFPubDwQxu_gGFR7Za6RE$$KkB0NsoUYpZ6SiQSsckDT",
    "sourcePort" : "lmfMZPz8Vi_FufzLxG4mi$$umqT5UdCGb8kvQLqRGbgc",
    "target" : "P3GtSo3tjK-RG_BuYjuSm$$n4l8jIpkZJqUKkxY-wC9t",
    "targetPort" : "model_LU_Document_Selection_Disabled_Join_318_inner_in_2"
  }, {
    "id" : "2TXK_gMzONZE-R2e4Yrlb",
    "source" : "a3BrUrXQaR72IB20IWM2c$$xr-d67wFVbOafiR4R_sle",
    "sourcePort" : "4-cvLQPcqLtLSH82VmHLO$$KXB6_nTcO1qdnliQ1cvdH",
    "target" : "LkRPP98NcWsswIkH8LUoZ$$7MRi-Jvqs2YMMGpIaG6iV",
    "targetPort" : "model_LU_Document_Selection_Disabled_Cleanse_290_in_0"
  }, {
    "id" : "conn_orhEzAnIfeIWtzPH8efsf$$sYj9NIW8TZxe3IzaZVCbo_IE9XzV6UhcQC6EUQw4gi9$$pIj95Ohf4Bg0_ZLtUQ-3_",
    "source" : "orhEzAnIfeIWtzPH8efsf$$sYj9NIW8TZxe3IzaZVCbo",
    "sourcePort" : "model_LU_Document_Selection_Disabled_Join_310_inner_out_0",
    "target" : "Ma1e7h4Eeh25V5H65TLRh$$VPx97wqbb2u4K83dKvk_S",
    "targetPort" : "model_LU_Document_Selection_Disabled_AlteryxSelect_294_in_0"
  }, {
    "id" : "conn_P3GtSo3tjK-RG_BuYjuSm$$n4l8jIpkZJqUKkxY-wC9t_IE9XzV6UhcQC6EUQw4gi9$$pIj95Ohf4Bg0_ZLtUQ-3_",
    "source" : "P3GtSo3tjK-RG_BuYjuSm$$n4l8jIpkZJqUKkxY-wC9t",
    "sourcePort" : "model_LU_Document_Selection_Disabled_Join_318_inner_out_0",
    "target" : "Ma1e7h4Eeh25V5H65TLRh$$VPx97wqbb2u4K83dKvk_S",
    "targetPort" : "model_LU_Document_Selection_Disabled_AlteryxSelect_294_in_0"
  }, {
    "id" : "conn_LkRPP98NcWsswIkH8LUoZ$$7MRi-Jvqs2YMMGpIaG6iV_orhEzAnIfeIWtzPH8efsf$$sYj9NIW8TZxe3IzaZVCbo",
    "source" : "LkRPP98NcWsswIkH8LUoZ$$7MRi-Jvqs2YMMGpIaG6iV",
    "sourcePort" : "model_LU_Document_Selection_Disabled_Cleanse_290_out_0",
    "target" : "orhEzAnIfeIWtzPH8efsf$$sYj9NIW8TZxe3IzaZVCbo",
    "targetPort" : "model_LU_Document_Selection_Disabled_Join_310_inner_in_0"
  }, {
    "id" : "conn_LkRPP98NcWsswIkH8LUoZ$$7MRi-Jvqs2YMMGpIaG6iV_P3GtSo3tjK-RG_BuYjuSm$$n4l8jIpkZJqUKkxY-wC9t",
    "source" : "LkRPP98NcWsswIkH8LUoZ$$7MRi-Jvqs2YMMGpIaG6iV",
    "sourcePort" : "model_LU_Document_Selection_Disabled_Cleanse_290_out_0",
    "target" : "P3GtSo3tjK-RG_BuYjuSm$$n4l8jIpkZJqUKkxY-wC9t",
    "targetPort" : "model_LU_Document_Selection_Disabled_Join_318_inner_in_0"
  } ],
  "component" : "Pipeline"
}
#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.logic.system.hardware.components.linux

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class CpuInfo:
    PROCESSOR: CpuInfo = None
    VENDORID: CpuInfo = None
    CPUFAMILY: CpuInfo = None
    MODEL: CpuInfo = None
    MODELNAME: CpuInfo = None
    STEPPING: CpuInfo = None
    CPUMHZ: CpuInfo = None
    CACHESIZE: CpuInfo = None
    FDIVBUG: CpuInfo = None
    HLTBUG: CpuInfo = None
    F00FBUG: CpuInfo = None
    COMABUG: CpuInfo = None
    FPU: CpuInfo = None
    FPUEXCEPTION: CpuInfo = None
    CPUIDLEVEL: CpuInfo = None
    WP: CpuInfo = None
    FLAGS: CpuInfo = None
    BOGOMIPS: CpuInfo = None

    def _init_fields(self) -> None:
        self.name: str = None
    

    def __init__(self, name: str) -> None:
        self._init_fields()
        self.name = name
    

    def toString(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.toString()


def _CpuInfo_PROCESSOR() -> object:
    return CpuInfo("processor")

lazy_static(CpuInfo, "PROCESSOR", _CpuInfo_PROCESSOR)

def _CpuInfo_VENDORID() -> object:
    return CpuInfo("vendor_id")

lazy_static(CpuInfo, "VENDORID", _CpuInfo_VENDORID)

def _CpuInfo_CPUFAMILY() -> object:
    return CpuInfo("cpu family")

lazy_static(CpuInfo, "CPUFAMILY", _CpuInfo_CPUFAMILY)

def _CpuInfo_MODEL() -> object:
    return CpuInfo("model")

lazy_static(CpuInfo, "MODEL", _CpuInfo_MODEL)

def _CpuInfo_MODELNAME() -> object:
    return CpuInfo("model name")

lazy_static(CpuInfo, "MODELNAME", _CpuInfo_MODELNAME)

def _CpuInfo_STEPPING() -> object:
    return CpuInfo("stepping")

lazy_static(CpuInfo, "STEPPING", _CpuInfo_STEPPING)

def _CpuInfo_CPUMHZ() -> object:
    return CpuInfo("cpu MHz")

lazy_static(CpuInfo, "CPUMHZ", _CpuInfo_CPUMHZ)

def _CpuInfo_CACHESIZE() -> object:
    return CpuInfo("cache size")

lazy_static(CpuInfo, "CACHESIZE", _CpuInfo_CACHESIZE)

def _CpuInfo_FDIVBUG() -> object:
    return CpuInfo("fdiv_bug")

lazy_static(CpuInfo, "FDIVBUG", _CpuInfo_FDIVBUG)

def _CpuInfo_HLTBUG() -> object:
    return CpuInfo("hlt_bug")

lazy_static(CpuInfo, "HLTBUG", _CpuInfo_HLTBUG)

def _CpuInfo_F00FBUG() -> object:
    return CpuInfo("f00f_bug")

lazy_static(CpuInfo, "F00FBUG", _CpuInfo_F00FBUG)

def _CpuInfo_COMABUG() -> object:
    return CpuInfo("coma_bug")

lazy_static(CpuInfo, "COMABUG", _CpuInfo_COMABUG)

def _CpuInfo_FPU() -> object:
    return CpuInfo("fpu")

lazy_static(CpuInfo, "FPU", _CpuInfo_FPU)

def _CpuInfo_FPUEXCEPTION() -> object:
    return CpuInfo("fpu_exception")

lazy_static(CpuInfo, "FPUEXCEPTION", _CpuInfo_FPUEXCEPTION)

def _CpuInfo_CPUIDLEVEL() -> object:
    return CpuInfo("cache size")

lazy_static(CpuInfo, "CPUIDLEVEL", _CpuInfo_CPUIDLEVEL)

def _CpuInfo_WP() -> object:
    return CpuInfo("yes")

lazy_static(CpuInfo, "WP", _CpuInfo_WP)

def _CpuInfo_FLAGS() -> object:
    return CpuInfo("flags")

lazy_static(CpuInfo, "FLAGS", _CpuInfo_FLAGS)

def _CpuInfo_BOGOMIPS() -> object:
    return CpuInfo("bogomips")

lazy_static(CpuInfo, "BOGOMIPS", _CpuInfo_BOGOMIPS)


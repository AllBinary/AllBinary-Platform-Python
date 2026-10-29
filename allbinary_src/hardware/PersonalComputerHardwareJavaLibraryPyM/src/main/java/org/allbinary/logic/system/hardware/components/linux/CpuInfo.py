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


CpuInfo.PROCESSOR = CpuInfo("processor")

CpuInfo.VENDORID = CpuInfo("vendor_id")

CpuInfo.CPUFAMILY = CpuInfo("cpu family")

CpuInfo.MODEL = CpuInfo("model")

CpuInfo.MODELNAME = CpuInfo("model name")

CpuInfo.STEPPING = CpuInfo("stepping")

CpuInfo.CPUMHZ = CpuInfo("cpu MHz")

CpuInfo.CACHESIZE = CpuInfo("cache size")

CpuInfo.FDIVBUG = CpuInfo("fdiv_bug")

CpuInfo.HLTBUG = CpuInfo("hlt_bug")

CpuInfo.F00FBUG = CpuInfo("f00f_bug")

CpuInfo.COMABUG = CpuInfo("coma_bug")

CpuInfo.FPU = CpuInfo("fpu")

CpuInfo.FPUEXCEPTION = CpuInfo("fpu_exception")

CpuInfo.CPUIDLEVEL = CpuInfo("cache size")

CpuInfo.WP = CpuInfo("yes")

CpuInfo.FLAGS = CpuInfo("flags")

CpuInfo.BOGOMIPS = CpuInfo("bogomips")


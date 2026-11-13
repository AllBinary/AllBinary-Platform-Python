# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.emulator.swt

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class SWTProcessorUtil:
    instance: SWTProcessorUtil = None

    def _init_fields(self) -> None:
        self.swtProcessor: SWTProcessor = SWTProcessor.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> SWTProcessorUtil:
        return SWTProcessorUtil.instance
from org.allbinary.emulator.swt.SWTProcessor import SWTProcessor


def _SWTProcessorUtil_instance() -> object:
    return SWTProcessorUtil()

lazy_static(SWTProcessorUtil, "instance", _SWTProcessorUtil_instance)


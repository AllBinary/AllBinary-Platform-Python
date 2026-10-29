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
# package org.allbinary.game.input

from __future__ import annotations



class PlatformInputMappingFactory:
    instance: PlatformInputMappingFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.inputToGameKeyMapping: PersistentInputMapping = PersistentInputMapping.getNullInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PlatformInputMappingFactory:
        return PlatformInputMappingFactory.instance
    

    def getPersistentInputMappingInstance(self) -> PersistentInputMapping:
        from org.allbinary.game.input.MotionJ2MEGameInputMapping import MotionJ2MEGameInputMapping
        try:
            if self.inputToGameKeyMapping == PersistentInputMapping.getNullInstance():
                self.inputToGameKeyMapping = MotionJ2MEGameInputMapping()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
        return self.inputToGameKeyMapping
from org.allbinary.game.input.mapping.PersistentInputMapping import PersistentInputMapping
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


PlatformInputMappingFactory.instance = PlatformInputMappingFactory()


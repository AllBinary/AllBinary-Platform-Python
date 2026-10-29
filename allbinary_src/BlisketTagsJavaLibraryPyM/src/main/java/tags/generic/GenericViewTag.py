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
# package tags.generic

from __future__ import annotations

from tags.TransformTag import TransformTag


class GenericViewTag(TransformTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.output: str = None
        self.file: str = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
    

    def setOutput(self, value: str) -> None:
        self.output = value
        self.getPropertiesHashMap().put(InputOutputTypeData.getInstance().NAME, self.output)
    

    def setFile(self, value: str) -> None:
        self.file = value
        self.getPropertiesHashMap().put(InputOutputTypeData.getInstance().FILE, self.file)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData



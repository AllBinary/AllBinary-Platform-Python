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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from tags.TransformTag import TransformTag


@java_inherited_overloads
class GenericViewTag(TransformTag):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("output", None)
        vars(self).setdefault("file", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "output" not in vars(self): self.output: str = None
        if "file" not in vars(self): self.file: str = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
    

    def setOutput(self, value: str) -> None:
        from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
        self.output = value
        self.getPropertiesHashMap().put(InputOutputTypeData.getInstance().NAME, self.output)
    

    def setFile(self, value: str) -> None:
        from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
        self.file = value
        self.getPropertiesHashMap().put(InputOutputTypeData.getInstance().FILE, self.file)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



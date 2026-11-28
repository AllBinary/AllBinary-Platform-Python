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
# package tags

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from tags.CommandTag import CommandTag


@java_inherited_overloads
class PropertiesTag(CommandTag):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("propertiesHashMap", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "propertiesHashMap" not in vars(self): self.propertiesHashMap: HashMap = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.propertiesHashMap = StdUtil.getInstance().createHashMap()
    

    def getPropertiesHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        return self.propertiesHashMap
    

    def doEndTag(self) -> int:
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF("Tag Ended", self, "doEndTag")
        self.propertiesHashMap = StdUtil.getInstance().createHashMap()
        return self.EVAL_PAGE
# from java.util.HashMap import HashMap
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



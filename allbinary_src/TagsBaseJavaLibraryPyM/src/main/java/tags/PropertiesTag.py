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

from tags.CommandTag import CommandTag


class PropertiesTag(CommandTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.propertiesHashMap: dict = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.propertiesHashMap = StdUtil.getInstance().createHashMap()
    

    def getPropertiesHashMap(self) -> dict:
        return self.propertiesHashMap
    

    def doEndTag(self) -> int:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF("Tag Ended", self, "doEndTag")
        self.propertiesHashMap = StdUtil.getInstance().createHashMap()
        return self.EVAL_PAGE
# from java.util.HashMap import HashMap
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil



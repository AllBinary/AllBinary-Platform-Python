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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from tags.PropertiesTag import PropertiesTag


@java_inherited_overloads
class HelperTag(PropertiesTag):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("tagHelperFactoryInterface", None)
        vars(self).setdefault("anyType", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "tagHelperFactoryInterface" not in vars(self): self.tagHelperFactoryInterface: TagHelperFactoryInterface = None
        if "anyType" not in vars(self): self.anyType: object = None
    

    def __init__(self, tagHelperFactoryInterface: TagHelperFactoryInterface) -> None:
        __class__._java_defaults(self)
        from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.tagHelperFactoryInterface = tagHelperFactoryInterface
    

    # throws Exception
    def setHelper(self) -> None:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if self.anyType is None:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
                self.logUtil.putF("Creating TagHelper with: \n" + str(self.getPropertiesHashMap()), self, "doStartTag")
            self.anyType = self.tagHelperFactoryInterface.getInstance(self.getPropertiesHashMap(), self.pageContext)
    

    def getHelper(self) -> object:
        return self.anyType
    

    def doEndTag(self) -> int:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF("Tag Ended", self, "doEndTag")
        self.anyType = None
        return java_super_call(super(), "doEndTag")
# from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



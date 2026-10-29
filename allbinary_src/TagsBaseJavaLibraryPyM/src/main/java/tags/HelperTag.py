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

from tags.PropertiesTag import PropertiesTag


class HelperTag(PropertiesTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tagHelperFactoryInterface: TagHelperFactoryInterface = None
        self.anyType: object = None
    

    def __init__(self, tagHelperFactoryInterface: TagHelperFactoryInterface) -> None:
        super().__init__()
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        self.tagHelperFactoryInterface = tagHelperFactoryInterface
    

    # throws Exception
    def setHelper(self) -> None:
        if self.anyType is None:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                self.logUtil.putF("Creating TagHelper with: \n" + str(self.getPropertiesHashMap()), self, "doStartTag")
            self.anyType = self.tagHelperFactoryInterface.getInstance(self.getPropertiesHashMap(), self.pageContext)
    

    def getHelper(self) -> object:
        return self.anyType
    

    def doEndTag(self) -> int:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF("Tag Ended", self, "doEndTag")
        self.anyType = None
        return super().doEndTag()
from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil



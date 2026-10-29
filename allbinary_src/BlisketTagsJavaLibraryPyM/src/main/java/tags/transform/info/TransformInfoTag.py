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
# package tags.transform.info

from __future__ import annotations

from tags.ModifyTag import ModifyTag


class TransformInfoTag(ModifyTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.name: str = None
        self.storeName: str = None
        self.objectFile: str = None
        self.anyType: str = None
        self.objectConfigFile: str = None
        self.objectConfig: str = None
        self.templateFile: str = None
        self.template: str = None
        self.dataFile: str = None
        self.data: str = None
        self.type_: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        super().__init__(TransformInfoRequestHelperFactory())
        self._init_fields()
    

    def _constructor1(self, tagHelperFactoryInterface: TagHelperFactoryInterface) -> None:
        super().__init__(tagHelperFactoryInterface)
        self._init_fields()
    

    def setName(self, value: str) -> None:
        self.name = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().NAME, self.name)
    

    def setStoreName(self, value: str) -> None:
        self.storeName = value
        self.getPropertiesHashMap().put(StoreFrontData.getInstance().NAME, self.storeName)
    

    def setObjectFile(self, value: str) -> None:
        self.objectFile = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().OBJECTFILENAME, self.objectFile)
    

    def setObject(self, value: str) -> None:
        self.anyType = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().OBJECT, self.anyType)
    

    def setTemplateFile(self, value: str) -> None:
        self.templateFile = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().TEMPLATEFILENAME, self.templateFile)
    

    def setTemplate(self, value: str) -> None:
        self.template = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().TEMPLATE, self.template)
    

    def setDataFile(self, value: str) -> None:
        self.dataFile = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().DATAFILENAME, self.dataFile)
    

    def setData(self, value: str) -> None:
        self.data = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().DATA, self.data)
    

    def setObjectConfigFile(self, value: str) -> None:
        self.objectConfigFile = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().OBJECTCONFIGFILENAME, self.objectConfigFile)
    

    def setObjectConfig(self, value: str) -> None:
        self.objectConfig = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().OBJECTCONFIG, self.objectConfig)
    

    def setType(self, value: str) -> None:
        self.type_ = value
        self.getPropertiesHashMap().put(OutputTypeData.getInstance().NAME, self.type_)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF("TransformInfoTag type set: " + self.type_, self, "setType")
    

    def getName(self) -> str:
        return self.name
    

    def getObjectFile(self) -> str:
        return self.objectFile
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            return super().doStartTag()
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from javax.servlet.jsp.JspTagException import JspTagException
from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.OutputTypeData import OutputTypeData
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
from taghelpers.transform.info.TransformInfoRequestHelperFactory import TransformInfoRequestHelperFactory



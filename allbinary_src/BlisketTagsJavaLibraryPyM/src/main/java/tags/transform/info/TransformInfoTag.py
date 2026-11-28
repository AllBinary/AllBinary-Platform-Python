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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from tags.ModifyTag import ModifyTag


@java_inherited_overloads
class TransformInfoTag(ModifyTag):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("name", None)
        vars(self).setdefault("storeName", None)
        vars(self).setdefault("objectFile", None)
        vars(self).setdefault("anyType", None)
        vars(self).setdefault("objectConfigFile", None)
        vars(self).setdefault("objectConfig", None)
        vars(self).setdefault("templateFile", None)
        vars(self).setdefault("template", None)
        vars(self).setdefault("dataFile", None)
        vars(self).setdefault("data", None)
        vars(self).setdefault("type_", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "name" not in vars(self): self.name: str = None
        if "storeName" not in vars(self): self.storeName: str = None
        if "objectFile" not in vars(self): self.objectFile: str = None
        if "anyType" not in vars(self): self.anyType: str = None
        if "objectConfigFile" not in vars(self): self.objectConfigFile: str = None
        if "objectConfig" not in vars(self): self.objectConfig: str = None
        if "templateFile" not in vars(self): self.templateFile: str = None
        if "template" not in vars(self): self.template: str = None
        if "dataFile" not in vars(self): self.dataFile: str = None
        if "data" not in vars(self): self.data: str = None
        if "type_" not in vars(self): self.type_: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    def _constructor0(self) -> None:
        __class__._java_defaults(self)
        from taghelpers.transform.info.TransformInfoRequestHelperFactory import TransformInfoRequestHelperFactory
        super().__init__(TransformInfoRequestHelperFactory())
        __class__._init_fields(self)
    

    def _constructor1(self, tagHelperFactoryInterface: TagHelperFactoryInterface) -> None:
        __class__._java_defaults(self)
        from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
        super().__init__(tagHelperFactoryInterface)
        __class__._init_fields(self)
    

    def setName(self, value: str) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        self.name = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().NAME, self.name)
    

    def setStoreName(self, value: str) -> None:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        self.storeName = value
        self.getPropertiesHashMap().put(StoreFrontData.getInstance().NAME, self.storeName)
    

    def setObjectFile(self, value: str) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        self.objectFile = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().OBJECTFILENAME, self.objectFile)
    

    def setObject(self, value: str) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        self.anyType = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().OBJECT, self.anyType)
    

    def setTemplateFile(self, value: str) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        self.templateFile = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().TEMPLATEFILENAME, self.templateFile)
    

    def setTemplate(self, value: str) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        self.template = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().TEMPLATE, self.template)
    

    def setDataFile(self, value: str) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        self.dataFile = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().DATAFILENAME, self.dataFile)
    

    def setData(self, value: str) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        self.data = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().DATA, self.data)
    

    def setObjectConfigFile(self, value: str) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        self.objectConfigFile = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().OBJECTCONFIGFILENAME, self.objectConfigFile)
    

    def setObjectConfig(self, value: str) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        self.objectConfig = value
        self.getPropertiesHashMap().put(TransformInfoData.getInstance().OBJECTCONFIG, self.objectConfig)
    

    def setType(self, value: str) -> None:
        from org.allbinary.logic.io.OutputTypeData import OutputTypeData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        self.type_ = value
        self.getPropertiesHashMap().put(OutputTypeData.getInstance().NAME, self.type_)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF("TransformInfoTag type set: " + self.type_, self, "setType")
    

    def getName(self) -> str:
        return self.name
    

    def getObjectFile(self) -> str:
        return self.objectFile
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
        try:
            return java_super_call(super(), "doStartTag")
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from javax.servlet.jsp.JspTagException import JspTagException
# from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.OutputTypeData import OutputTypeData
# from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
# from taghelpers.transform.info.TransformInfoRequestHelperFactory import TransformInfoRequestHelperFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



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
# package views.business.context.modules.storefront.customizer.template.objectConfig

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfig import TransformInfoObjectConfig


@java_inherited_overloads
class NoTemplateTransformInfoObjectConfig(TransformInfoObjectConfig):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 2:
            __class__._constructor2(self, *args)
        elif len(args) == 3:
            __class__._constructor3(self, *args)
    

    def _constructor1(self, transformInfoInterface: TransformInfoInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface)
        __class__._init_fields(self)
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, document: Document) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.w3c.dom.Document import Document
        super().__init__(transformInfoInterface, document)
        __class__._init_fields(self)
        self.setDocument(self.generate(self.toXmlDoc()))
    

    def _constructor3(self, transformInfoInterface: TransformInfoInterface, name: str, type_: str) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface, name, type_)
        __class__._init_fields(self)
        self.setDocument(self.generate(self.toXmlDoc()))
    

    # throws Exception
    def generate(self, objectConfigDocument: Document) -> Document:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.string.regex.replace.Replace import Replace
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        from org.allbinary.logic.visual.transform.template.util.TransformTemplateCustomizerUtil import TransformTemplateCustomizerUtil
        from org.w3c.dom.Document import Document
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        docString: str = XmlDocumentHelper.toString(objectConfigDocument)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Initial ObjectConfig: " + docString, self, "generate()")
        storeName: str = self.getTransformInfoInterface().getStoreName()
        viewName: str = self.getTransformInfoInterface().getName()
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        VARKEY: str = TransformInfoObjectConfigData.getInstance().VARKEY
        hashMap.put(VARKEY + str(StoreFrontData.getInstance().NAME), storeName)
        hashMap.put(VARKEY + str(TransformInfoData.getInstance().OWNER), viewName)
        pageName: str = TransformTemplateCustomizerUtil.getInstance().getPageNameHack(self.getTransformInfoInterface().getName(), self.getTransformInfoInterface().getStoreName())
        hashMap.put(VARKEY + str(TransformInfoData.getInstance().PARTIAL), pageName)
        replace: Replace = Replace(hashMap)
        newObjectConfigDocument: Document = DomDocumentHelper.create(replace.all(docString))
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Final ObjectConfig: " + XmlDocumentHelper.toString(newObjectConfigDocument), self, "generate()")
        return newObjectConfigDocument
# from java.util.HashMap import HashMap
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.regex.replace.Replace import Replace
# from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
# from org.allbinary.logic.visual.transform.template.util.TransformTemplateCustomizerUtil import TransformTemplateCustomizerUtil
# from org.w3c.dom.Document import Document
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



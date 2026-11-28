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
from views.business.context.modules.storefront.customizer.template.objectConfig.NoTemplateTransformInfoObjectConfig import NoTemplateTransformInfoObjectConfig


@java_inherited_overloads
class InsertTemplateCustomizerTransformInfoObjectConfig(NoTemplateTransformInfoObjectConfig):
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
    def set(self, aParentViewName: str) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoDomNodeView import TransformInfoDomNodeView
        from org.allbinary.logic.visual.transform.info.TransformInfosData import TransformInfosData
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Setting: " + aParentViewName, self, "set()")
        document: Document = self.toXmlDoc()
        parentComponentsNodeList: NodeList = document.getElementsByTagName(TransformInfosData.getInstance().NAME)
        if parentComponentsNodeList is not None and parentComponentsNodeList.getLength() > 0:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Replacing", self, "set()")
            componentNode: Node = parentComponentsNodeList.item(0).getChildNodes().item(0)
            if componentNode is not None:
                document.removeChild(componentNode)
            parentComponentsNodeList.item(0).appendChild(TransformInfoDomNodeView(aParentViewName).toXmlNode(document))
        else:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Setting", self, "set()")
            objectConfigNode: Node = document.getElementsByTagName(TransformInfoObjectConfigData.getInstance().NAME).item(0)
            parentComponentsNode: Node = document.createElement(TransformInfosData.getInstance().NAME)
            objectConfigNode.appendChild(parentComponentsNode)
            transformInfoDomNodeView: TransformInfoDomNodeView = TransformInfoDomNodeView(aParentViewName)
            parentComponentsNode.appendChild(transformInfoDomNodeView.toXmlNode(document))
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoDomNodeView import TransformInfoDomNodeView
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.logic.visual.transform.info.TransformInfosData import TransformInfosData
# from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



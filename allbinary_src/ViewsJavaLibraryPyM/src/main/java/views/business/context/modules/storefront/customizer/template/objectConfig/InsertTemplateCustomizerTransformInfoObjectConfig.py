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

from views.business.context.modules.storefront.customizer.template.objectConfig.NoTemplateTransformInfoObjectConfig import NoTemplateTransformInfoObjectConfig


class InsertTemplateCustomizerTransformInfoObjectConfig(NoTemplateTransformInfoObjectConfig):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 3:
            self._constructor3(*args)
    

    def _constructor1(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, document: Document) -> None:
        super().__init__(transformInfoInterface, document)
        self._init_fields()
        self.setDocument(self.generate(self.toXmlDoc()))
    

    def _constructor3(self, transformInfoInterface: TransformInfoInterface, name: str, type_: str) -> None:
        super().__init__(transformInfoInterface, name, type_)
        self._init_fields()
        self.setDocument(self.generate(self.toXmlDoc()))
    

    # throws Exception
    def set(self, aParentViewName: str) -> None:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Setting: " + aParentViewName, self, "set()")
        document: Document = self.toXmlDoc()
        parentComponentsNodeList: NodeList = document.getElementsByTagName(TransformInfosData.getInstance().NAME)
        if parentComponentsNodeList is not None and parentComponentsNodeList.getLength() > 0:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Replacing", self, "set()")
            componentNode: Node = parentComponentsNodeList.item(0).getChildNodes().item(0)
            if componentNode is not None:
                document.removeChild(componentNode)
            parentComponentsNodeList.item(0).appendChild(TransformInfoDomNodeView(aParentViewName).toXmlNode(document))
        else:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Setting", self, "set()")
            objectConfigNode: Node = document.getElementsByTagName(TransformInfoObjectConfigData.getInstance().NAME).item(0)
            parentComponentsNode: Node = document.createElement(TransformInfosData.getInstance().NAME)
            objectConfigNode.appendChild(parentComponentsNode)
            transformInfoDomNodeView: TransformInfoDomNodeView = TransformInfoDomNodeView(aParentViewName)
            parentComponentsNode.appendChild(transformInfoDomNodeView.toXmlNode(document))
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.info.TransformInfoDomNodeView import TransformInfoDomNodeView
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.TransformInfosData import TransformInfosData
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigData import TransformInfoObjectConfigData
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList



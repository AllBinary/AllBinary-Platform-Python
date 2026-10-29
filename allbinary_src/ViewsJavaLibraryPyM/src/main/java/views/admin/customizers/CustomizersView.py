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
# package views.admin.customizers

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class CustomizersView(HttpStoreComponentView, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.customizersVector: BasicArrayList = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.customizersVector = TransformInfoEntityBuilder.getInstance().getNames(self.getWeblisketSession().getStoreName())
    

    def toXmlNode(self, document: Document) -> Node:
        try:
            node: Node = document.createElement(TransformTemplateCustomizersData.NAME)
            unsortedCustomizerViewVector: BasicArrayList = BasicArrayListD()
            size: int = self.customizersVector.size()
            for index in range(0, size):
                viewName: str = self.customizersVector.get(index)
                if viewName.find(CustomizerTransformInfoData.NAME) > 0 and viewName.find(self.GLOBALS2.EDIT) > 0 and viewName.find(BodyData.getInstance().VIEWNAMEKEY) > 0 and viewName.find(TitleData.getInstance().VIEWNAMEKEY) > 0:
                    unsortedCustomizerViewVector.add(viewName)
            objectArray: list[object] = unsortedCustomizerViewVector.toArray()
            Arrays.sort(objectArray, StringComparator())
            for index in range(0, len(objectArray)):
                viewName: str = objectArray[index]
                viewNameNode: Node = ModDomHelper.createNameValueNodes(document, TransformTemplateCustomizerData.NAME, viewName, TransformTemplateCustomizerUtil.getInstance().getPageNameHack(viewName, self.getWeblisketSession().getStoreName()))
                node.appendChild(viewNameNode)
            return node
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            return None
    

    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self)
    

    # throws Exception
    def view(self) -> str:
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
# from java.util.Arrays import Arrays
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.data.tables.transform.info.TransformInfoEntityBuilder import TransformInfoEntityBuilder
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.globals.GLOBALS2 import GLOBALS2
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.sort.StringComparator import StringComparator
from org.allbinary.logic.visual.transform.info.CustomizerTransformInfoData import CustomizerTransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.template.customizer.TransformTemplateCustomizerData import TransformTemplateCustomizerData
from org.allbinary.logic.visual.transform.template.customizer.TransformTemplateCustomizersData import TransformTemplateCustomizersData
from org.allbinary.logic.visual.transform.template.customizer.bodies.BodyData import BodyData
from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
from org.allbinary.logic.visual.transform.template.util.TransformTemplateCustomizerUtil import TransformTemplateCustomizerUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



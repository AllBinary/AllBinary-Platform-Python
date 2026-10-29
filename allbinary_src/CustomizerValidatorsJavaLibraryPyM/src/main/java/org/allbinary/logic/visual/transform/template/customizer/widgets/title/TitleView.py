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
# package org.allbinary.logic.visual.transform.template.customizer.widgets.title

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class TitleView(DomNodeInterface):
    NAME: str = "None"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.title: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.title = TitleView.NAME
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
        self._init_fields()
        titleTextNode: Node = DomSearchHelper.getNode(TitleData.getInstance().TEXT, node.getChildNodes())
        valueNode: Node = DomSearchHelper.getNode(DomData.VALUE, titleTextNode.getChildNodes())
        self.title = DomNodeHelper.getTextNodeValue(valueNode)
        if StringValidationUtil.getInstance().isEmpty(self.title):
            self.title = TitleView.NAME
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Title: " + str(self.getTitle()), self, "Consructor()")
    

    def _constructor1(self, hashMap: dict) -> None:
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("HashMap: " + str(hashMap), self, self.commonStrings.CONSTRUCTOR)
        self.getFormData(hashMap)
    

    def getTitle(self) -> str:
        return self.title
    

    def getFormData(self, hashMap: dict) -> None:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
        self.title = hashMap.get(TitleData.getInstance().TEXT)
        if StringValidationUtil.getInstance().isEmpty(self.title):
            self.title = TitleView.NAME
    

    def toHashMap(self) -> dict:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(TitleData.getInstance().TEXT, self.getTitle())
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.transform.template.customizer.widgets.title.TitleData import TitleData
        hashMap: dict = self.toHashMap()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("TitleView HashMap: " + str(hashMap), self, "toXmlNode()")
        return ModDomHelper.createNameValueNodes(document, TitleData.getInstance().NAME, hashMap)
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomData import DomData
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



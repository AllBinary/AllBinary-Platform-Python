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
# package org.allbinary.logic.visual.dhtml.style.css.property

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class CssProperty(DomNodeInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "propertyName" not in vars(self): self.propertyName: str = None
        if "cssPropertyValues" not in vars(self): self.cssPropertyValues: CssPropertyValues = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or isinstance(args[0], str)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor1_1(self, name: str) -> None:
        from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertyValues import CssPropertyValues
        __class__._init_fields(self)
        self.propertyName = name
        self.cssPropertyValues = CssPropertyValues()
    

    def _constructor1_2(self, node: Node) -> None:
        from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertyData import CssPropertyData
        from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertyValues import CssPropertyValues
        from org.allbinary.data.tree.dom.DomData import DomData
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        propertyNode: Node = DomSearchHelper.getNode(DomData.VALUE, node.getChildNodes())
        self.propertyName = DomNodeHelper.getTextNodeValue(propertyNode)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().STYLE):
            self.logUtil.putF("Name: " + self.getName(), self, "CssProperty()")
        propertyValuesNode: Node = DomSearchHelper.getNode(CssPropertyData.getInstance().VALUES, node.getChildNodes())
        self.cssPropertyValues = CssPropertyValues(propertyValuesNode)
    

    def getName(self) -> str:
        return self.propertyName
    

    def toHashMap(self) -> HashMap:
        from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertyData import CssPropertyData
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.put(CssPropertyData.getInstance().NAME, self.propertyName)
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertyData import CssPropertyData
        from java.util.HashMap import HashMap
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        hashMap: HashMap = self.toHashMap()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("CssView HashMap: " + str(hashMap), self, "toXmlNode()")
        node: Node = ModDomHelper.createNameValueNodes(document, CssPropertyData.getInstance().NAME, self.propertyName)
        node.appendChild(self.cssPropertyValues.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
# from org.allbinary.data.tree.dom.DomData import DomData
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



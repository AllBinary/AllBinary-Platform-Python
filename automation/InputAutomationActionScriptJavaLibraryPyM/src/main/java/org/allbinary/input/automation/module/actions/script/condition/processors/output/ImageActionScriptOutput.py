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
# package org.allbinary.input.automation.module.actions.script.condition.processors.output

from __future__ import annotations

from org.allbinary.input.automation.module.actions.script.condition.processors.output.BasicProfileActionScriptOutput import BasicProfileActionScriptOutput
from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputInterface import ImageActionScriptOutputInterface


class ImageActionScriptOutput(BasicProfileActionScriptOutput, ImageActionScriptOutputInterface):
    NAME: str = "Captures"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.saved: bool = False
        self.display: bool = False
        self.imageTypes: ImageTypes = None
        self.actionScriptOutputJPanel: ImageActionScriptOutputJPanel = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 0:
            self._constructor0(*args)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageTypes import ImageTypes
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputJPanel import ImageActionScriptOutputJPanel
        super().__init__(ImageActionScriptOutput.NAME, node)
        self._init_fields()
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        actionNode: Node = DomSearchHelper.getNode(ImageActionScriptOutputData.NAME, node.getChildNodes())
        if actionNode is not None:
            nodeList: NodeList = actionNode.getChildNodes()
            for index in range(0, nodeList.getLength()):
                childNode: Node = nodeList.item(index)
                if childNode.getNodeName().compareTo(ImageActionScriptOutputData.SAVE) == 0:
                    booleanString: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.setSaved(booleanString)
                elif childNode.getNodeName().compareTo(ImageActionScriptOutputData.DISPLAY) == 0:
                    booleanString: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.setSaved(booleanString)
                elif childNode.getNodeName().compareTo(ImageActionScriptOutputData.TYPES) == 0:
                    self.setImageTypes(ImageTypes(childNode))
                else:
                    raise Exception("Action Script Output Unknown Node")
        else:
            raise Exception("Action Script Output Node Null")
        self.setAllowsChildren(False)
        self.actionScriptOutputJPanel = ImageActionScriptOutputJPanel(self)
    

    def _constructor0(self) -> None:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageTypes import ImageTypes
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputJPanel import ImageActionScriptOutputJPanel
        super().__init__(ImageActionScriptOutput.NAME)
        self._init_fields()
        self.setImageTypes(ImageTypes())
        self.setAllowsChildren(False)
        self.actionScriptOutputJPanel = ImageActionScriptOutputJPanel(self)
    

    def getActionScriptOutputJPanel(self) -> ImageActionScriptOutputJPanel:
        return self.actionScriptOutputJPanel
    

    def toHashMap(self) -> dict:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(ImageActionScriptOutputData.DISPLAY, str(self.isDisplay()))
        hashMap.put(ImageActionScriptOutputData.SAVE, str(self.isSaved()))
        self.logUtil.putF("HashMap: " + str(hashMap), self, "toHashMap()")
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        node: Node = super().toXmlNode(document)
        newNode: Node = ModDomHelper.createNodeWithValueNodes(document, ImageActionScriptOutputData.NAME, self.toHashMap())
        newNode.appendChild(self.getImageTypes().toXmlNode(document))
        node.appendChild(newNode)
        return node
    

    # throws Exception
    def process(self, frame: int) -> None:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputProcessor import ImageActionScriptOutputProcessor
        ImageActionScriptOutputProcessor.process(self, frame)
    

    def showDialog(self) -> None:
        self.actionScriptOutputJPanel.getCapturedImageActionJDialog().setVisible(True)
    

    def isSaved(self) -> bool:
        return self.saved
    

    def setSaved(self, saved: bool) -> None:
        self.saved = saved
    

    def isDisplay(self) -> bool:
        return self.display
    

    def setDisplay(self, display: bool) -> None:
        self.display = display
    

    def future_toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(" Is Save: ")
        stringBuffer.appendboolean(self.isSaved())
        stringBuffer.append(" Is Display: ")
        stringBuffer.appendboolean(self.isDisplay())
        stringBuffer.append(" ")
        stringBuffer.append(str(self.getImageTypes()))
        return str(stringBuffer)
    

    def log(self) -> None:
        self.logUtil.putF(self.future_toString(), self, "log")
    

    def getImageTypes(self) -> ImageTypes:
        return self.imageTypes
    

    def setImageTypes(self, imageTypes: ImageTypes) -> None:
        self.imageTypes = imageTypes
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList



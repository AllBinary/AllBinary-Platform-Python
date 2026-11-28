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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.input.automation.module.actions.script.condition.processors.output.BasicProfileActionScriptOutput import BasicProfileActionScriptOutput
from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputInterface import ImageActionScriptOutputInterface


@java_inherited_overloads
class ImageActionScriptOutput(*java_bases(BasicProfileActionScriptOutput, ImageActionScriptOutputInterface)):
    NAME: str = "Captures"
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("saved", False)
        vars(self).setdefault("display", False)
        vars(self).setdefault("imageTypes", None)
        vars(self).setdefault("actionScriptOutputJPanel", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.saved: bool = False
        self.display: bool = False
        if "imageTypes" not in vars(self): self.imageTypes: ImageTypes = None
        if "actionScriptOutputJPanel" not in vars(self): self.actionScriptOutputJPanel: ImageActionScriptOutputJPanel = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 0:
            __class__._constructor0(self, *args)
    

    def _constructor1(self, node: Node) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageTypes import ImageTypes
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputJPanel import ImageActionScriptOutputJPanel
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        super().__init__(ImageActionScriptOutput.NAME, node)
        __class__._init_fields(self)
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
        __class__._java_defaults(self)
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageTypes import ImageTypes
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputJPanel import ImageActionScriptOutputJPanel
        super().__init__(ImageActionScriptOutput.NAME)
        __class__._init_fields(self)
        self.setImageTypes(ImageTypes())
        self.setAllowsChildren(False)
        self.actionScriptOutputJPanel = ImageActionScriptOutputJPanel(self)
    

    def getActionScriptOutputJPanel(self) -> ImageActionScriptOutputJPanel:
        return self.actionScriptOutputJPanel
    

    def toHashMap(self) -> HashMap:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.put(ImageActionScriptOutputData.DISPLAY, str(java_predicate(self, "isDisplay")))
        hashMap.put(ImageActionScriptOutputData.SAVE, str(java_predicate(self, "isSaved")))
        self.logUtil.putF("HashMap: " + str(hashMap), self, "toHashMap()")
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = java_super_call(super(), "toXmlNode", document)
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
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(" Is Save: ")
        stringBuffer.appendboolean(java_predicate(self, "isSaved"))
        stringBuffer.append(" Is Display: ")
        stringBuffer.appendboolean(java_predicate(self, "isDisplay"))
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
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList



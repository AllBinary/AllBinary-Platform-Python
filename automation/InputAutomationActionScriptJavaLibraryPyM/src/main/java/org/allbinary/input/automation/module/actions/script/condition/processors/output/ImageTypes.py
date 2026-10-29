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



class ImageTypes:

    def _init_fields(self) -> None:
        self.vector: BasicArrayList = BasicArrayListD()

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        self._init_fields()
        nodeList: NodeList = node.getChildNodes()
        for index in range(0, nodeList.getLength()):
            childNode: Node = nodeList.item(index)
            if childNode.getNodeName().compareTo(ImageActionScriptOutputData.TYPE) == 0:
                nextImageTypeString: str = DomNodeHelper.getTextNodeValue(childNode)
                self.getVector().add(InputImageType.getInstance(nextImageTypeString))
            else:
                raise Exception("ImageTypes Unknown Node")
    

    @staticmethod
    def valueOf(anyType: list[object]) -> ImageTypes:
        imageTypes: ImageTypes = ImageTypes()
        for index in range(0, len(anyType)):
            imageType: InputImageType = InputImageType.getInstance(anyType[index])
            imageTypes.getVector().add(imageType)
        return imageTypes
    

    def getVector(self) -> BasicArrayList:
        return self.vector
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutputData import ImageActionScriptOutputData
        newNode: Node = document.createElement(ImageActionScriptOutputData.TYPES)
        size: int = self.vector.size()
        for index in range(0, size):
            imageType: InputImageType = self.vector.get(index)
            newNode.appendChild(ModDomHelper.createTextNode(document, ImageActionScriptOutputData.TYPE, imageType.getName()))
        return newNode
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("ImageTypes: ")
        size: int = self.vector.size()
        for index in range(0, size):
            imageType: InputImageType = self.vector.get(index)
            stringBuffer.append(imageType.getName())
            if index < size - 1:
                stringBuffer.append(", ")
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.input.media.image.InputImageType import InputImageType
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList



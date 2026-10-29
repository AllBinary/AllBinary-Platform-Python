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
# package org.allbinary.logic.visual.dhtml.style.color

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class ColorsView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.commonPhoneStrings: CommonPhoneStrings = CommonPhoneStrings.getInstance()
        self.HEXRADIX: int = 16
        self.MAX: int = 255
        self.delta: int = 20
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getColorNode(self, document: Document, redIndex: int, greenIndex: int, blueIndex: int) -> Node:
        from org.allbinary.logic.visual.dhtml.style.color.ColorData import ColorData
        hexColorStringBuffer: StringMaker = StringMaker()
        if redIndex < self.HEXRADIX:
            hexColorStringBuffer.append(self.commonPhoneStrings.ZERO)
        hexColorStringBuffer.append(Integer.toString(redIndex, self.HEXRADIX))
        if greenIndex < self.HEXRADIX:
            hexColorStringBuffer.append(self.commonPhoneStrings.ZERO)
        hexColorStringBuffer.append(Integer.toString(greenIndex, self.HEXRADIX))
        if blueIndex < self.HEXRADIX:
            hexColorStringBuffer.append(self.commonPhoneStrings.ZERO)
        hexColorStringBuffer.append(Integer.toString(blueIndex, self.HEXRADIX))
        colorNode: Node = ModDomHelper.createNameValueNodes(document, ColorData.getInstance().NAME, str(hexColorStringBuffer))
        return colorNode
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.dhtml.style.color.ColorsData import ColorsData
        from org.allbinary.logic.visual.dhtml.style.color.ColorData import ColorData
        from org.allbinary.logic.visual.dhtml.style.color.ColorData import ColorData
        from org.allbinary.logic.visual.dhtml.style.color.ColorData import ColorData
        node: Node = ModDomHelper.createNameValueNodes(document, ColorsData.getInstance().NAME, "RGB Colors In Hex")
        blackNode: Node = ModDomHelper.createNameValueNodes(document, ColorData.getInstance().NAME, "000000")
        node.appendChild(blackNode)
        for index in range(0, self.MAX, self.delta):
            hexColorStringBuffer: StringMaker = StringMaker()
            if index < self.HEXRADIX:
                hexColorStringBuffer.append(self.commonPhoneStrings.ZERO)
            hexColorStringBuffer.append(Integer.toString(index, self.HEXRADIX))
            if index < self.HEXRADIX:
                hexColorStringBuffer.append(self.commonPhoneStrings.ZERO)
            hexColorStringBuffer.append(Integer.toString(index, self.HEXRADIX))
            if index < self.HEXRADIX:
                hexColorStringBuffer.append(self.commonPhoneStrings.ZERO)
            hexColorStringBuffer.append(Integer.toString(index, self.HEXRADIX))
            colorNode: Node = ModDomHelper.createNameValueNodes(document, ColorData.getInstance().NAME, str(hexColorStringBuffer))
            node.appendChild(colorNode)
        whiteNode: Node = ModDomHelper.createNameValueNodes(document, ColorData.getInstance().NAME, "FFFFFF")
        node.appendChild(whiteNode)
        for blueIndex in range(int(self.MAX / 2), self.MAX, self.delta):
            for greenIndex in range(0, int(self.MAX / 2), self.delta):
                for redIndex in range(0, int(self.MAX / 2), self.delta):
                    node.appendChild(self.getColorNode(document, redIndex, greenIndex, blueIndex))
        for redIndex in range(int(self.MAX / 2), self.MAX, self.delta):
            for greenIndex in range(0, int(self.MAX / 2), self.delta):
                for blueIndex in range(0, int(self.MAX / 2), self.delta):
                    node.appendChild(self.getColorNode(document, redIndex, greenIndex, blueIndex))
        for greenIndex in range(int(self.MAX / 2), self.MAX, self.delta):
            for redIndex in range(0, int(self.MAX / 2), self.delta):
                for blueIndex in range(0, int(self.MAX / 2), self.delta):
                    node.appendChild(self.getColorNode(document, redIndex, greenIndex, blueIndex))
        for greenIndex in range(0, self.MAX, 2 * self.delta):
            for redIndex in range(0, self.MAX, 2 * self.delta):
                for blueIndex in range(0, self.MAX, 2 * self.delta):
                    node.appendChild(self.getColorNode(document, redIndex, greenIndex, blueIndex))
        return node
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



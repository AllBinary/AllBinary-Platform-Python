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
# package org.allbinary.input.automation.actions.script.condition

from __future__ import annotations

from org.allbinary.input.automation.actions.script.condition.BasicProfileActionScriptCondition import BasicProfileActionScriptCondition
from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionInterface import ColorAtActionScriptConditionInterface


class ColorAtActionScriptCondition(BasicProfileActionScriptCondition, ColorAtActionScriptConditionInterface):
    NAME: str = "If Color At"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.colorAtActionScriptConditionJPanel: ColorAtActionScriptConditionJPanel = None
        self.point: Point = None
        self.colorRangeInterface: ColorRangeInterface = ColorRange()

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 0:
            self._constructor0(*args)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        super().__init__(ColorAtActionScriptCondition.NAME, node)
        self._init_fields()
        self.point = Point(0, 0)
        actionNode: Node = DomSearchHelper.getNode(ColorAtActionScriptConditionData.NAME, node.getChildNodes())
        if actionNode is not None:
            nodeList: NodeList = actionNode.getChildNodes()
            for index in range(0, nodeList.getLength()):
                childNode: Node = nodeList.item(index)
                if childNode.getNodeName().compareTo(ColorAtActionScriptConditionData.LOCATION_X) == 0:
                    locationX: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.point.x = str(locationX)
                elif childNode.getNodeName().compareTo(ColorAtActionScriptConditionData.LOCATION_Y) == 0:
                    locationY: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.point.y = str(locationY)
                elif childNode.getNodeName().compareTo(ColorAtActionScriptConditionData.MIN_RED) == 0:
                    string: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.getColorRangeInterface().setMinRed(str(string))
                elif childNode.getNodeName().compareTo(ColorAtActionScriptConditionData.MAX_RED) == 0:
                    string: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.getColorRangeInterface().setMaxRed(str(string))
                elif childNode.getNodeName().compareTo(ColorAtActionScriptConditionData.MIN_GREEN) == 0:
                    string: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.getColorRangeInterface().setMinGreen(str(string))
                elif childNode.getNodeName().compareTo(ColorAtActionScriptConditionData.MAX_GREEN) == 0:
                    string: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.getColorRangeInterface().setMaxGreen(str(string))
                elif childNode.getNodeName().compareTo(ColorAtActionScriptConditionData.MIN_BLUE) == 0:
                    string: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.getColorRangeInterface().setMinBlue(str(string))
                elif childNode.getNodeName().compareTo(ColorAtActionScriptConditionData.MAX_BLUE) == 0:
                    string: str = DomNodeHelper.getTextNodeValue(childNode)
                    self.getColorRangeInterface().setMaxBlue(str(string))
        else:
            raise Exception("Color At Action Script Condition Node Null")
        self.init()
    

    def _constructor0(self) -> None:
        super().__init__(ColorAtActionScriptCondition.NAME)
        self._init_fields()
        self.point = Point(0, 0)
        self.init()
    

    def init(self) -> None:
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionJPanel import ColorAtActionScriptConditionJPanel
        self.colorAtActionScriptConditionJPanel = ColorAtActionScriptConditionJPanel(self)
    

    def getPoint(self) -> Point:
        return self.point
    

    def setPoint(self, point: Point) -> None:
        self.point = point
    

    def showDialog(self) -> None:
        self.colorAtActionScriptConditionJPanel.getColorAtActionJDialog().setVisible(True)
    

    def toHashMap(self) -> dict:
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(ColorAtActionScriptConditionData.LOCATION_X, str(self.getPoint().x))
        hashMap.put(ColorAtActionScriptConditionData.LOCATION_Y, str(self.getPoint().y))
        hashMap.put(ColorAtActionScriptConditionData.MIN_RED, str(self.getColorRangeInterface().getMinRed()))
        hashMap.put(ColorAtActionScriptConditionData.MAX_RED, str(self.getColorRangeInterface().getMaxRed()))
        hashMap.put(ColorAtActionScriptConditionData.MIN_GREEN, str(self.getColorRangeInterface().getMinGreen()))
        hashMap.put(ColorAtActionScriptConditionData.MAX_GREEN, str(self.getColorRangeInterface().getMaxGreen()))
        hashMap.put(ColorAtActionScriptConditionData.MIN_BLUE, str(self.getColorRangeInterface().getMinBlue()))
        hashMap.put(ColorAtActionScriptConditionData.MAX_BLUE, str(self.getColorRangeInterface().getMaxBlue()))
        self.logUtil.putF("HashMap: " + str(hashMap), self, "toHashMap()")
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        node: Node = super().toXmlNode(document)
        node.appendChild(ModDomHelper.createNodeWithValueNodes(document, ColorAtActionScriptConditionData.NAME, self.toHashMap()))
        return node
    

    # throws Exception
    def shouldProcess(self, frame: int) -> bool:
        capturedBufferedImageCacheable: BufferedImageFrameCacheable = (CapturedBufferedImagesCacheSingleton.getInstance()).get(str(frame))
        bufferedImage: BufferedImage = capturedBufferedImageCacheable.getBufferedImage()
        automaticCacheInterface: AutomaticCacheInterface = ColorCacheFactory.getInstance()
        colorInteger: int = str(bufferedImage.getRGB(self.getPoint().x, self.getPoint().y))
        colorCacheable: ColorCacheable = automaticCacheInterface.get(colorInteger)
        color: Color = colorCacheable.getColor()
        if self.colorRangeInterface.isInRange(color):
            return super().shouldProcess(frame)
        return False
    

    def log(self) -> None:
        message: str = str(StringMaker().append("getPoint(): ").append(str(self.getPoint())).append(CommonSeps.getInstance().NEW_LINE).append(str(self.getColorRangeInterface())))
        self.logUtil.putF(message, self, "log")
    

    def getColorRangeInterface(self) -> ColorRangeInterface:
        return self.colorRangeInterface
    

    def setColorRangeInterface(self, colorRangeInterface: ColorRangeInterface) -> None:
        self.colorRangeInterface = colorRangeInterface
# from java.awt.Color import Color
# from java.awt.Point import Point
# from java.awt.image.BufferedImage import BufferedImage
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.graphics.color.ColorCacheFactory import ColorCacheFactory
from org.allbinary.graphics.color.ColorCacheable import ColorCacheable
from org.allbinary.input.media.image.capture.CapturedBufferedImagesCacheSingleton import CapturedBufferedImagesCacheSingleton
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.util.cache.AutomaticCacheInterface import AutomaticCacheInterface
from org.allbinary.media.image.analysis.ColorRange import ColorRange
from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface
from org.allbinary.media.image.cache.BufferedImageFrameCacheable import BufferedImageFrameCacheable
from org.allbinary.string.CommonSeps import CommonSeps
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList



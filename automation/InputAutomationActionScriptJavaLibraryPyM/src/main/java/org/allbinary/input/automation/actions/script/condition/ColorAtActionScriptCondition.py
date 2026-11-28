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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.input.automation.actions.script.condition.BasicProfileActionScriptCondition import BasicProfileActionScriptCondition
from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionInterface import ColorAtActionScriptConditionInterface


@java_inherited_overloads
class ColorAtActionScriptCondition(*java_bases(BasicProfileActionScriptCondition, ColorAtActionScriptConditionInterface)):
    NAME: str = "If Color At"
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("colorAtActionScriptConditionJPanel", None)
        vars(self).setdefault("point", None)
        vars(self).setdefault("colorRangeInterface", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.media.image.analysis.ColorRange import ColorRange
        from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "colorAtActionScriptConditionJPanel" not in vars(self): self.colorAtActionScriptConditionJPanel: ColorAtActionScriptConditionJPanel = None
        if "point" not in vars(self): self.point: Point = None
        self.colorRangeInterface: ColorRangeInterface = ColorRange()

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 0:
            __class__._constructor0(self, *args)
    

    def _constructor1(self, node: Node) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        super().__init__(ColorAtActionScriptCondition.NAME, node)
        __class__._init_fields(self)
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
        __class__._java_defaults(self)
        super().__init__(ColorAtActionScriptCondition.NAME)
        __class__._init_fields(self)
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
    

    def toHashMap(self) -> HashMap:
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
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
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = java_super_call(super(), "toXmlNode", document)
        node.appendChild(ModDomHelper.createNodeWithValueNodes(document, ColorAtActionScriptConditionData.NAME, self.toHashMap()))
        return node
    

    # throws Exception
    def shouldProcess(self, frame: int) -> bool:
        from org.allbinary.graphics.color.ColorCacheFactory import ColorCacheFactory
        from org.allbinary.graphics.color.ColorCacheable import ColorCacheable
        from org.allbinary.input.media.image.capture.CapturedBufferedImagesCacheSingleton import CapturedBufferedImagesCacheSingleton
        from org.allbinary.logic.util.cache.AutomaticCacheInterface import AutomaticCacheInterface
        from org.allbinary.media.image.cache.BufferedImageFrameCacheable import BufferedImageFrameCacheable
        capturedBufferedImageCacheable: BufferedImageFrameCacheable = (CapturedBufferedImagesCacheSingleton.getInstance()).get(str(frame))
        bufferedImage: BufferedImage = capturedBufferedImageCacheable.getBufferedImage()
        automaticCacheInterface: AutomaticCacheInterface = ColorCacheFactory.getInstance()
        colorInteger: int = str(bufferedImage.getRGB(self.getPoint().x, self.getPoint().y))
        colorCacheable: ColorCacheable = automaticCacheInterface.get(colorInteger)
        color: Color = colorCacheable.getColor()
        if self.colorRangeInterface.isInRange(color):
            return java_super_call(super(), "shouldProcess", frame)
        return False
    

    def log(self) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        message: str = str(StringMaker().append("getPoint(): ").append(str(self.getPoint())).append(CommonSeps.getInstance().NEW_LINE).append(str(self.getColorRangeInterface())))
        self.logUtil.putF(message, self, "log")
    

    def getColorRangeInterface(self) -> ColorRangeInterface:
        from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface
        return self.colorRangeInterface
    

    def setColorRangeInterface(self, colorRangeInterface: ColorRangeInterface) -> None:
        from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface
        self.colorRangeInterface = colorRangeInterface
# from java.awt.Color import Color
# from java.awt.Point import Point
# from java.awt.image.BufferedImage import BufferedImage
# from java.util.HashMap import HashMap
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.graphics.color.ColorCacheFactory import ColorCacheFactory
# from org.allbinary.graphics.color.ColorCacheable import ColorCacheable
# from org.allbinary.input.media.image.capture.CapturedBufferedImagesCacheSingleton import CapturedBufferedImagesCacheSingleton
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.util.cache.AutomaticCacheInterface import AutomaticCacheInterface
# from org.allbinary.media.image.analysis.ColorRange import ColorRange
# from org.allbinary.media.image.analysis.ColorRangeInterface import ColorRangeInterface
# from org.allbinary.media.image.cache.BufferedImageFrameCacheable import BufferedImageFrameCacheable
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList



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
# package org.allbinary.layer

from __future__ import annotations

from org.allbinary.graphics.RectangleFactory import RectangleFactory
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.view.ViewPositionBase import ViewPositionBase
from org.allbinary.layer.Layer import Layer
from org.allbinary.layer.LayerInterface import LayerInterface


class AllBinaryLayer(Layer, LayerInterface):
    NULL_ALLBINARY_LAYER: AllBinaryLayer = None
    TYPE: str = "Type: "

    def _init_fields(self) -> None:
        self.viewPositionEvent: ViewPositionEvent = ViewPositionEvent(self)
        self.halfWidth: int = 0
        self.halfHeight: int = 0
        self.name: str = None
        self.viewPosition: ViewPositionBase = ViewPositionBase.NULL_VIEW_POSITION
    

    def __init__(self, name: str, rectangle: Rectangle, viewPosition: ViewPositionBase) -> None:
        super().__init__(rectangle.getWidth(), rectangle.getHeight())
        self._init_fields()
        localName: str = None
        if name is None:
            localName = type(self).__module__ + "." + type(self).__qualname__
        else:
            localName = str(StringMaker().append(name).append(CommonSeps.getInstance().COLON).append(format(TsUtil.getInstance().hashCode(self), "x")))
        self.name = localName
        point: GPoint = rectangle.getPoint()
        self.setPosition(point.getX(), point.getY(), point.getZ())
        self.setHalfWidth((self.getWidth() >> 1))
        self.setHalfHeight((self.getHeight() >> 1))
        self.viewPosition = viewPosition
        self.viewPosition.setAllbinaryLayer(self)
    

    # throws Exception
    def onChangeEvent(self, layerManagerEvent: ViewPositionEvent) -> None:
        pass
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
    

    def getX2(self) -> int:
        return self.getXP() + self.getWidth()
    

    def getY2(self) -> int:
        return self.getYP() + self.getHeight()
    

    def getZ2(self) -> int:
        return int((self.getZP() + self.getDepth()))
    

    def getName(self) -> str:
        return self.name
    

    def setHalfWidth(self, halfWidth: int) -> None:
        self.halfWidth = halfWidth
    

    def getHalfWidth(self) -> int:
        return self.halfWidth
    

    def setHalfHeight(self, halfHeight: int) -> None:
        self.halfHeight = halfHeight
    

    def getHalfHeight(self) -> int:
        return self.halfHeight
    

    def getHalfDepth(self) -> int:
        return int(int(self.getDepth()) / 2)
    

    def getViewPosition(self) -> ViewPositionBase:
        return self.viewPosition
    

    def setViewPosition(self, viewPosition: ViewPositionBase) -> None:
        self.viewPosition = viewPosition
    

    def getGroupInterface(self) -> list[Group]:
        return BasicGroupFactory.getInstance().NONE_ARRAY
    

    def implmentsTickableInterface(self) -> bool:
        return False
    

    def implmentsGameInputInterface(self) -> bool:
        return False
    

    def implmentsArtificialIntelligenceCompositeInterface(self) -> bool:
        return False
    

    def implmentsCollidableInterface(self) -> bool:
        return False
    

    def implementsThreedInterface(self) -> bool:
        return OpenGLFeatureUtil.getInstance().isAnyThreed()
    

    def getType(self) -> int:
        return -1
    

    def getMultiPlayerType(self) -> int:
        return -1
    

    def toStringAppend(self, stringBuffer: StringMaker) -> None:
        commonSeps: CommonSeps = CommonSeps.getInstance()
        positionStrings: PositionStrings = PositionStrings.getInstance()
        commonLabels: CommonLabels = CommonLabels.getInstance()
        stringBuffer.append(self.getName())
        stringBuffer.append(commonSeps.COLON)
        stringBuffer.append(AllBinaryLayer.TYPE)
        stringBuffer.appendint(self.getType())
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(positionStrings.X_LABEL)
        stringBuffer.appendint(int(self.getXP()))
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(positionStrings.Y_LABEL)
        stringBuffer.appendint(int(self.getYP()))
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(positionStrings.Z_LABEL)
        stringBuffer.appendint(int(self.getZP()))
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(commonLabels.WIDTH_LABEL)
        stringBuffer.appendint(int(self.getWidth()))
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(commonLabels.HEIGHT_LABEL)
        stringBuffer.appendint(int(self.getHeight()))
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        self.toStringAppend(stringBuffer)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.identification.BasicGroupFactory import BasicGroupFactory
from org.allbinary.game.identification.Group import Group
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.view.event.ViewPositionEvent import ViewPositionEvent


AllBinaryLayer.NULL_ALLBINARY_LAYER = AllBinaryLayer(StringUtil.getInstance().EMPTY_STRING, RectangleFactory.SINGLETON, ViewPositionBase.NULL_VIEW_POSITION)


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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.image.opengles.OpenGLSurfaceChangedInterface import OpenGLSurfaceChangedInterface
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.view.event.ViewPositionEventListenerInterface import ViewPositionEventListenerInterface


class AllBinaryGameLayer(AllBinaryLayer, ViewPositionEventListenerInterface, OpenGLSurfaceChangedInterface):

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.basicSetColorUtil: BasicColorSetUtil = BasicColorSetUtil.getInstance()
        self.RED: BasicColor = BasicColorFactory.getInstance().RED
        self.paintable: Paintable = ((Paintable()  # Java anonymous class body:
#         self.basicSetColorUtil: BasicColorSetUtil = BasicColorSetUtil.getInstance()
#         self.BLACK: BasicColor = BasicColorFactory.getInstance().BLACK
#         
# 
#         def paint(self, graphics: Graphics) -> None:
#             self.basicSetColorUtil.setBasicColorP(graphics, self.BLACK)
) if SWTUtil.isSWT else NullPaintable.getInstance())
        self.gameKeyEventList: BasicArrayList = BasicArrayListD()
    

    def __init__(self, name: str, layerInfo: Rectangle, viewPosition: ViewPositionBase) -> None:
        super().__init__(name, layerInfo, viewPosition)
        self._init_fields()
    

    # throws Exception
    def set(self, gl: GL) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    def move(self) -> None:
        pass
    

    def getGameKeyEventList(self) -> BasicArrayList:
        return self.gameKeyEventList
    

    # throws Exception
    def processInput(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def onViewPositionChangeEvent(self) -> None:
        self.onChangeEvent(self.viewPositionEvent)
    

    # throws Exception
    def onChangeEvent(self, layerManagerEvent: ViewPositionEvent) -> None:
        from org.allbinary.game.layer.GameLayerUtil import GameLayerUtil
        if GameLayerUtil.isOnScreen(self):
            self.setVisible(True)
        else:
            self.setVisible(False)
    

    def paintFirst(self, graphics: Graphics) -> None:
        self.paintable.paint(graphics)
    

    def paintDebug(self, graphics: Graphics) -> None:
        viewPosition: ViewPositionBase = self.getViewPosition()
        viewX: int = viewPosition.getX()
        viewY: int = viewPosition.getY()
        self.basicSetColorUtil.setBasicColorP(graphics, self.RED)
        graphics.drawRect(viewX, viewY, self.getWidth(), self.getHeight())
    

    def setWidth(self, width: int) -> None:
        super().setLayerWidth(width)
        self.setHalfWidth(width >> 1)
    

    def setHeight(self, height: int) -> None:
        super().setLayerHeight(height)
        self.setHalfHeight(height >> 1)
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.view.ViewPositionBase import ViewPositionBase
from org.allbinary.view.event.ViewPositionEvent import ViewPositionEvent
from org.allbinary.game.layer.SWTUtil import SWTUtil



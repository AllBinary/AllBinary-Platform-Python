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
# package org.allbinary.game.health

from __future__ import annotations

from org.allbinary.game.health.HealthBarAnimation import HealthBarAnimation


class HealthBarThreedAnimation(HealthBarAnimation):

    def _init_fields(self) -> None:
        self.rectangle: Rectangle = None
        self.basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.object3dProcessor: Object3dProcessor = Object3dProcessorUtil.getInstance().getInstanceObject3dProcessor()
    

    def __init__(self, layerInterface: AllBinaryLayer, location: int) -> None:
        super().__init__(layerInterface, location)
        self._init_fields()
        self.basicColor = self.basicColorFactory.GREEN
        self.colorP = int(self.basicColor)
        self.rectangle = Rectangle(0, 0, 1, 1, self.basicColor)
        self.rectangle.setDoubleSidedEnabled(True)
        self.rectangle.setNormalsEnabled(False)
        self.rectangle.setTexturesEnabled(False)
    

    def updateColor(self) -> None:
        colorBufferList: ColorBufferList = self.rectangle.getVertices().getColor4BufferList()
        size: int = colorBufferList.size()
        index = size
        while (index := index - 1) >= 0:
            colorBufferList.set(index, self.basicColor)
    

    def updateSize(self) -> None:
        number3dBufferList: Number3dBufferList = self.rectangle.getVertices().getPointsOnFacesNumber3dBufferList()
        width: int = self.x2
        height: int = self.thickness * 2
        segsH: int = 1
        segsW: int = 1
        row: int = 0
        col: int = 0
        w: float = float(int(width / segsW))
        h: float = float(int(height / segsH))
        width5: float = float(width) / 2.0
        height5: float = float(height) / 2.0
        index: int = 0
        for row in range(0, segsH + 1):
            for col in range(0, segsW + 1):
                number3dBufferList.set(((index := index + 1) - 1), float(col) * w - width5, float(row) * h - height5, 0.0)
    

    def onHealthChange(self, newX2: int) -> None:
        super().onHealthChange(newX2)
        self.updateColor()
        self.updateSize()
    

    def paintThreedXYZ(self, graphics: Graphics, x: int, y: int, z: int) -> None:
        openGLESGraphics: OpenGLESGraphics = graphics
        gl: GL10 = openGLESGraphics.getGl10()
        viewPosition: ViewPositionBase = self.allbinaryLayer.getViewPosition()
        positionNumber3d: Number3d = self.rectangle.getPosition()
        positionNumber3d.x = -(float(viewPosition.getX()))
        positionNumber3d.z = -(float(viewPosition.getY()))
        positionNumber3d.y = viewPosition.getZ() + self.allbinaryLayer.getHeight()
        self.object3dProcessor.drawObject(gl, self.rectangle)
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Graphics import Graphics
from min3d.core.ColorBufferList import ColorBufferList
from min3d.core.Number3dBufferList import Number3dBufferList
from min3d.objectPrimitives.Rectangle import Rectangle
from min3d.vos.Number3d import Number3d
from org.allbinary.device.OpenGLESGraphics import OpenGLESGraphics
from org.allbinary.graphics.threed.min3d.renderer.Object3dProcessor import Object3dProcessor
from org.allbinary.graphics.threed.min3d.renderer.Object3dProcessorUtil import Object3dProcessorUtil
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.view.ViewPositionBase import ViewPositionBase



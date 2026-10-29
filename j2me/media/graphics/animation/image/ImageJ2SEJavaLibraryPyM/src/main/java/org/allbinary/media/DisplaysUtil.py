# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.media

from __future__ import annotations



class DisplaysUtil:
    instance: DisplaysUtil = None
    

    @staticmethod
    def getInstance() -> DisplaysUtil:
        return DisplaysUtil.instance
    

    def getPrimaryScreenSize(self) -> Rectangle:
        dimension: Dimension = Toolkit.getDefaultToolkit().getScreenSize()
        return Rectangle(PointFactory.getInstance().ZERO_ZERO, dimension.width, dimension.height)
    

    def getScreenSizesAsRectangleArray(self) -> list[Rectangle]:
        graphicsEnvironment: GraphicsEnvironment = GraphicsEnvironment.getLocalGraphicsEnvironment()
        graphicsDeviceArray: list[GraphicsDevice] = graphicsEnvironment.getScreenDevices()
        graphicsDevice: GraphicsDevice = None
        displayMode: DisplayMode = None
        rectangle: Rectangle = None
        size: int = len(graphicsDeviceArray)
        rectangleArray: list[Rectangle] = [None] * (size)
        for index in range(0, size):
            graphicsDevice = graphicsDeviceArray[index]
            displayMode = graphicsDevice.getDisplayMode()
            rectangle = Rectangle(PointFactory.getInstance().ZERO_ZERO, displayMode.getWidth(), displayMode.getHeight())
            rectangleArray[index] = rectangle
        return rectangleArray
# from java.awt.Dimension import Dimension
# from java.awt.DisplayMode import DisplayMode
# from java.awt.GraphicsDevice import GraphicsDevice
# from java.awt.GraphicsEnvironment import GraphicsEnvironment
# from java.awt.Toolkit import Toolkit
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle


DisplaysUtil.instance = DisplaysUtil()


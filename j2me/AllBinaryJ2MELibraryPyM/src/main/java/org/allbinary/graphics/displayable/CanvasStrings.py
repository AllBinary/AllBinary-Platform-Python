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
# package org.allbinary.graphics.displayable

from __future__ import annotations



class CanvasStrings:
    instance: CanvasStrings = None

    def _init_fields(self) -> None:
        self.CONSTRUCTOR: str = "MyCanvas::MyCanvas"
        self.PAUSE: str = "MyCanvas::pause"
        self.UN_PAUSE: str = "MyCanvas::unPause"
        self.SET_FULL_SCREEN_MODE: str = "setFullScreenMode"
        self.SIZE_CHANGED: str = "sizeChanged"
        self.SCALED_IMAGES: str = "scaledImages"
        self.PAINT: str = "paint"
        self.ON_DISPLAY_CHANGE_EVENT: str = "onDisplayChangeEvent"
        self.UPDATE_MEASUREMENT: str = "updateMeasurement"
        self.FD_WIDTH: str = " font/display width: "
        self.FD_HEIGHT: str = " font/display height: "
        self.EMPTY_CHILD_NAME_LIST: BasicArrayList = BasicArrayListUtil.getInstance().getImmutableInstance()
        self.ABOUT: str = "About"
        self.OPTIONS: str = "Options"
        self.FONT_ATLAS: str = "/font.png"
        self.OBJ_MODEL: str = "_obj"
        self.MD2_MODEL: str = "_md2"
        self._PNG: str = ".png"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CanvasStrings:
        return CanvasStrings.instance
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


CanvasStrings.instance = CanvasStrings()


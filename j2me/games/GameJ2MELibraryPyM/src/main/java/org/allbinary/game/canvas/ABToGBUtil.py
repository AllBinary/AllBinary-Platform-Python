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
# package org.allbinary.game.canvas

from __future__ import annotations



class ABToGBUtil:
    instance: ABToGBUtil = None

    def _init_fields(self) -> None:
        self.abCanvas: Canvas = NullCanvas.NULL_CANVAS
        self.allBinaryGameLayerManager: AllBinaryGameLayerManager = AllBinaryGameLayerManager.getNullInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ABToGBUtil:
        return ABToGBUtil.instance
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.NullCanvas import NullCanvas
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager


ABToGBUtil.instance = ABToGBUtil()


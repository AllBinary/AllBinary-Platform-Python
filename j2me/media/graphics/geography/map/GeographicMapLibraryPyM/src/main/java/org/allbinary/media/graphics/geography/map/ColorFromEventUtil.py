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
# package org.allbinary.media.graphics.geography.map

from __future__ import annotations



class ColorFromEventUtil:
    instance: ColorFromEventUtil = None

    def _init_fields(self) -> None:
        self.YELLOW: BasicColor = BasicColorFactory.getInstance().YELLOW
        self.COLOR_INT: int = int(self.YELLOW)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ColorFromEventUtil:
        return ColorFromEventUtil.instance
    

    def getForegroundColor(self, gameCanvasInterface: AllBinaryGameCanvas) -> BasicColor:
        color: BasicColor = self.YELLOW
        geographicMapCompositeInterface: GeographicMapCompositeInterface = gameCanvasInterface.getLayerManager()
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        if geographicMapInterface is not None:
            foregroundBasicColor: BasicColor = geographicMapInterface.getForegroundBasicColor()
            color = foregroundBasicColor
        return color
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


ColorFromEventUtil.instance = ColorFromEventUtil()


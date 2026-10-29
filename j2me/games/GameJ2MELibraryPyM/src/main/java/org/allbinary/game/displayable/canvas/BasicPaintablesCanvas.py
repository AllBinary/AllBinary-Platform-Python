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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from org.allbinary.game.displayable.canvas.GameCommandCanvas import GameCommandCanvas


class BasicPaintablesCanvas(GameCommandCanvas):

    def _init_fields(self) -> None:
        self.paintableArray: list[Paintable] = None
        self.colorFillPaintable: ColorFillBasePaintable = None
    

    def __init__(self, cmdListener: CommandListener, name: str, allBinaryGameLayerManager: AllBinaryGameLayerManager, paintableArray: list[Paintable]) -> None:
        super().__init__(cmdListener, name, allBinaryGameLayerManager.getBackgroundBasicColor(), allBinaryGameLayerManager.getForegroundBasicColor())
        self._init_fields()
        self.paintableArray = paintableArray
        self.colorFillPaintable = ColorFillPaintableFactory.getInstance().getInstance(allBinaryGameLayerManager.getBackgroundBasicColor(), False)
    

    def paint(self, graphics: Graphics) -> None:
        self.colorFillPaintable.paint(graphics)
        graphics.setColor(self.foregroundColor)
        for index in range(len(self.paintableArray) - 1, 0 - 1, -1):
            self.paintableArray[index].paint(graphics)
        super().paint(graphics)
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.paint.ColorFillBasePaintable import ColorFillBasePaintable
from org.allbinary.game.paint.ColorFillPaintableFactory import ColorFillPaintableFactory
from org.allbinary.graphics.paint.Paintable import Paintable



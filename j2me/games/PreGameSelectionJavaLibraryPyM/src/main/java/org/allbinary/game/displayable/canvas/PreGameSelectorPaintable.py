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

from org.allbinary.graphics.paint.InitUpdatePaintable import InitUpdatePaintable


class PreGameSelectorPaintable(InitUpdatePaintable):

    def _init_fields(self) -> None:
        self.title: str = None
        self.canvasDrawLineString: CanvasDrawLineString = None
        self.preGameScrollSelectionForm: PreGameScrollSelectionForm = None
    

    def __init__(self, title: str, preGameScrollSelectionForm: PreGameScrollSelectionForm) -> None:
        super().__init__()
        self._init_fields()
        self.title = title
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.canvasDrawLineString = CanvasDrawLineString(displayInfo.getLastHalfWidth(), 0)
        self.preGameScrollSelectionForm = preGameScrollSelectionForm
    

    def update(self) -> None:
        displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.canvasDrawLineString = CanvasDrawLineString(displayInfo.getLastHalfWidth(), 0)
    

    def paint(self, graphics: Graphics) -> None:
        graphics.setColor(int(BasicColorFactory.getInstance().WHITE))
        self.canvasDrawLineString.paint(graphics, self.title, 0)
        self.getPreGameSelectionForm().paint(graphics)
    

    def getPreGameSelectionForm(self) -> PreGameScrollSelectionForm:
        return self.preGameScrollSelectionForm
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.draw.CanvasDrawLineString import CanvasDrawLineString



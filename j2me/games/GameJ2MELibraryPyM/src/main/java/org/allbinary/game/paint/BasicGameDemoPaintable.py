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
# package org.allbinary.game.paint

from __future__ import annotations

from org.allbinary.graphics.paint.StatePaintable import StatePaintable


class BasicGameDemoPaintable(StatePaintable):

    def _init_fields(self) -> None:
        self.mainDemoStatePaintable: Paintable = None
        self.ownershipPaintable: Paintable = None
        self.helpPaintableInterface: Paintable = None
        self.currentStatePaintable: Paintable = NullPaintable.getInstance()
    

    def __init__(self, mainDemoStatePaintable: Paintable, ownershipPaintable: Paintable, helpPaintableInterface: Paintable) -> None:
        super().__init__()
        self._init_fields()
        self.mainDemoStatePaintable = mainDemoStatePaintable
        self.setCurrentStatePaintable(NullPaintable.getInstance())
        self.ownershipPaintable = ownershipPaintable
        self.helpPaintableInterface = helpPaintableInterface
    

    def setState(self, state: int) -> None:
        if state == 0:
            self.setCurrentStatePaintable(self.getMainDemoStatePaintable())
        elif state == 1:
            self.setCurrentStatePaintable(self.helpPaintableInterface)
        else:
            self.setCurrentStatePaintable(self.ownershipPaintable)
    

    def paint(self, graphics: Graphics) -> None:
        self.getCurrentStatePaintable().paint(graphics)
    

    def getHelpPaintableInterface(self) -> Paintable:
        return self.helpPaintableInterface
    

    def setCurrentStatePaintable(self, currentStatePaintable: Paintable) -> None:
        self.currentStatePaintable = currentStatePaintable
    

    def getCurrentStatePaintable(self) -> Paintable:
        return self.currentStatePaintable
    

    def getMainDemoStatePaintable(self) -> Paintable:
        return self.mainDemoStatePaintable
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable



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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from org.allbinary.game.displayable.canvas.BaseMenuBehavior import BaseMenuBehavior


class InGameMenuBehavior(BaseMenuBehavior):
    instanceC: InGameMenuBehavior = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> InGameMenuBehavior:
        return InGameMenuBehavior.instanceC
    

    # throws Exception
    def onDisplayChangeEvent(self, allBinaryGameCanvas: AllBinaryGameCanvas, displayChangeEvent: DisplayChangeEvent) -> None:
        allBinaryGameCanvas.updateMenuFromEvent(displayChangeEvent)
    

    def initSpecialPaint(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        from org.allbinary.game.displayable.canvas.GameCanvasNonBotPaintable import GameCanvasNonBotPaintable
        allBinaryGameCanvas.setNonBotPaintableP(GameCanvasNonBotPaintable(allBinaryGameCanvas))
    

    # throws Exception
    def initMenu(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.initMenu2()
    

    # throws Exception
    def updateMenu(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.initMenu2()
    

    # throws Exception
    def popupMenu(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.popupMenu2()
    

    def closeMenu(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.closeMenu2()
from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent


InGameMenuBehavior.instanceC = InGameMenuBehavior()


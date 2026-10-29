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



class BaseMenuBehavior:
    instance: BaseMenuBehavior = None
    

    @staticmethod
    def getInstance() -> BaseMenuBehavior:
        return BaseMenuBehavior.instance
    

    # throws Exception
    def onDisplayChangeEvent(self, allBinaryGameCanvas: AllBinaryGameCanvas, displayChangeEvent: DisplayChangeEvent) -> None:
        pass
    

    def initSpecialPaint(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        allBinaryGameCanvas.setNonBotPaintableP(NullPaintable.getInstance())
    

    # throws Exception
    def initMenu(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        pass
    

    # throws Exception
    def updateMenu(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        pass
    

    # throws Exception
    def popupMenu(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        pass
    

    def closeMenu(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        pass
from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent
from org.allbinary.graphics.paint.NullPaintable import NullPaintable


BaseMenuBehavior.instance = BaseMenuBehavior()


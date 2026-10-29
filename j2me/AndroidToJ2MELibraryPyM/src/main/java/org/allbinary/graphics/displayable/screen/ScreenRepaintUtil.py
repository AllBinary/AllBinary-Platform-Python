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
# package org.allbinary.graphics.displayable.screen

from __future__ import annotations



class ScreenRepaintUtil:
    

    @staticmethod
    def repaint(displayable: Displayable) -> None:
        canvas: Canvas = displayable
        canvas.repaint()
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Displayable import Displayable



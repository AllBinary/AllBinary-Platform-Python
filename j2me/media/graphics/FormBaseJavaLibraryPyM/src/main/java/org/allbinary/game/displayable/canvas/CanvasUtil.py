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



class CanvasUtil:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getKeyName(key: int) -> str:
        commonPhoneStrings: CommonPhoneStrings = CommonPhoneStrings.getInstance()
        if key == Canvas.UP:
            return commonPhoneStrings.UP
        elif key == Canvas.DOWN:
            return commonPhoneStrings.DOWN
        elif key == Canvas.RIGHT:
            return commonPhoneStrings.RIGHT
        elif key == Canvas.LEFT:
            return commonPhoneStrings.LEFT
        elif key == Canvas.FIRE:
            return commonPhoneStrings.FIRE
        return "UNKNOWN KEY"
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings



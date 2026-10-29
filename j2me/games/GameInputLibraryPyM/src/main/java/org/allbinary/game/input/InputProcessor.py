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
# package org.allbinary.game.input

from __future__ import annotations



class InputProcessor:

    def _init_fields(self) -> None:
        self.gameInputStrings: GameInputStrings = GameInputStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    def keyPressedByDevice(self, keyCode: int, deviceId: int) -> None:
        pass
    

    def keyReleasedByDevice(self, canvas: Canvas, keyCode: int, deviceId: int) -> None:
        pass
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.input.GameInputStrings import GameInputStrings



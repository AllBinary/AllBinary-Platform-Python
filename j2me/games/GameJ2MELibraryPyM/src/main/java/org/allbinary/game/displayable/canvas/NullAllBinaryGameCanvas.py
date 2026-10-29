# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

from org.allbinary.game.displayable.canvas.AllBinaryGameCanvasInterface import AllBinaryGameCanvasInterface


class NullAllBinaryGameCanvas(AllBinaryGameCanvasInterface):
    NULL_ALLBINARY_GAME_CANVAS: NullAllBinaryGameCanvas = None
    

    def getLayerManager(self) -> AllBinaryGameLayerManager:
        raise RuntimeError()
    

    def addCommand(self, cmd: Command) -> None:
        raise RuntimeError()
    

    def getHeight(self) -> int:
        raise RuntimeError()
    

    def getWidth(self) -> int:
        raise RuntimeError()
    

    def removeCommand(self, cmd: Command) -> None:
        raise RuntimeError()
    

    def setCommandListener(self, l: CommandListener) -> None:
        raise RuntimeError()
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager


NullAllBinaryGameCanvas.NULL_ALLBINARY_GAME_CANVAS = NullAllBinaryGameCanvas()


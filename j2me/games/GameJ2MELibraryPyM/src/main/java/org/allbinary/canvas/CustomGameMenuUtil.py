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
# package org.allbinary.canvas

from __future__ import annotations



class CustomGameMenuUtil:
    

    @staticmethod
    def add(canvas: MyCanvas) -> None:
        gameCommandsFactory: GameCommandsFactory = GameCommandsFactory.getInstance()
        if AppletUtil.isAppletLoader(canvas):
            pass
        elif J2MEUtil.isHTML():
            pass
        else:
            canvas.addCommand(gameCommandsFactory.EXIT_COMMAND)
from org.allbinary.AppletUtil import AppletUtil
from org.allbinary.J2MEUtil import J2MEUtil
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas



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
# package org.allbinary.graphics.displayable

from __future__ import annotations



# Java interface
class DisplayableInterface:
    

    def addCommand(self, cmd: Command) -> None:
        raise NotImplementedError()
    

    def getHeight(self) -> int:
        raise NotImplementedError()
    

    def getWidth(self) -> int:
        raise NotImplementedError()
    

    def removeCommand(self, cmd: Command) -> None:
        raise NotImplementedError()
    

    def setCommandListener(self, l: CommandListener) -> None:
        raise NotImplementedError()
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.CommandListener import CommandListener



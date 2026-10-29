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
# package org.allbinary.graphics.form.item

from __future__ import annotations

from org.allbinary.graphics.form.item.ABTextItem import ABTextItem


class CommandTextItem(ABTextItem):

    def _init_fields(self) -> None:
        self.command: Command = None
    

    def __init__(self, command: Command, layout: int, altText: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(command.getLabel(), layout, altText, backgroundBasicColor, foregroundBasicColor)
        self._init_fields()
        self.command = command
    

    def isFocusable(self) -> bool:
        return True
    

    def getCommand(self) -> Command:
        return self.command
# from javax.microedition.lcdui.Command import Command
from org.allbinary.graphics.color.BasicColor import BasicColor



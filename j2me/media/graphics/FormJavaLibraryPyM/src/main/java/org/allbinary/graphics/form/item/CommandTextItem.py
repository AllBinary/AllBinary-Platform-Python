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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.form.item.ABTextItem import ABTextItem


@java_inherited_overloads
class CommandTextItem(ABTextItem):
    def _java_defaults(self):
        vars(self).setdefault("command", None)

    def _init_fields(self) -> None:
        if "command" not in vars(self): self.command: Command = None
    

    def __init__(self, command: Command, layout: int, altText: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Command import Command
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(command.getLabel(), layout, altText, backgroundBasicColor, foregroundBasicColor)
        __class__._init_fields(self)
        self.command = command
    

    def isFocusable(self) -> bool:
        return True
    

    def getCommand(self) -> Command:
        from javax.microedition.lcdui.Command import Command
        return self.command
# from javax.microedition.lcdui.Command import Command
# from org.allbinary.graphics.color.BasicColor import BasicColor



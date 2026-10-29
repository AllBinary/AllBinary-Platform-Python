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
# package org.allbinary.logic.visual.dhtml.html.input

from __future__ import annotations

from org.allbinary.logic.visual.dhtml.html.input.HtmlValueInput import HtmlValueInput


class HtmlLengthInput(HtmlValueInput):

    def _init_fields(self) -> None:
        self.MAXLENGTH: str = "MAXLENGTH"
        self.SIZE: str = "SIZE"
        self.length: str = None
        self.size: str = None
    

    def __init__(self, before: str, type_: str, name: str, value: str, after: str) -> None:
        super().__init__(before, type_, name, value, after)
        self._init_fields()
    

    def setMaxLength(self, length: int) -> None:
        len(self) = str(length)
        self.addAttribute(self.MAXLENGTH, len(self))
    

    def setSize(self, size: int) -> None:
        self.size = str(size)
        self.addAttribute(self.MAXLENGTH, self.size)



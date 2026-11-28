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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.visual.dhtml.html.input.HtmlValueInput import HtmlValueInput


@java_inherited_overloads
class HtmlLengthInput(HtmlValueInput):
    def _java_defaults(self):
        vars(self).setdefault("MAXLENGTH", None)
        vars(self).setdefault("SIZE", None)
        vars(self).setdefault("length", None)
        vars(self).setdefault("size", None)

    def _init_fields(self) -> None:
        self.MAXLENGTH: str = "MAXLENGTH"
        self.SIZE: str = "SIZE"
        if "length" not in vars(self): self.length: str = None
        if "size" not in vars(self): self.size: str = None
    

    def __init__(self, before: str, type_: str, name: str, value: str, after: str) -> None:
        __class__._java_defaults(self)
        super().__init__(before, type_, name, value, after)
        __class__._init_fields(self)
    

    def setMaxLength(self, length: int) -> None:
        self.length = str(length)
        self.addAttribute(self.MAXLENGTH, self.length)
    

    def setSize(self, size: int) -> None:
        self.size = str(size)
        self.addAttribute(self.MAXLENGTH, self.size)



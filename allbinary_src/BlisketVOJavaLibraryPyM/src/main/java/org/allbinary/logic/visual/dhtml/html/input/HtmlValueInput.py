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
from org.allbinary.logic.visual.dhtml.html.input.HtmlInput import HtmlInput


@java_inherited_overloads
class HtmlValueInput(HtmlInput):
    def _java_defaults(self):
        vars(self).setdefault("value", None)
        vars(self).setdefault("VALUE", None)

    def _init_fields(self) -> None:
        if "value" not in vars(self): self.value: str = None
        self.VALUE: str = "VALUE"
    

    def __init__(self, before: str, type_: str, name: str, value: str, after: str) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.string.StringUtil import StringUtil
        super().__init__(before, type_, name, after)
        __class__._init_fields(self)
        stringUtil: StringUtil = StringUtil.getInstance()
        self.value = stringUtil.EMPTY_STRING
        self.addAttribute(self.VALUE, value)
# from org.allbinary.logic.string.StringUtil import StringUtil



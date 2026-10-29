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

from org.allbinary.logic.visual.dhtml.html.input.HtmlInput import HtmlInput


class HtmlValueInput(HtmlInput):

    def _init_fields(self) -> None:
        self.value: str = None
        self.VALUE: str = "VALUE"
    

    def __init__(self, before: str, type_: str, name: str, value: str, after: str) -> None:
        super().__init__(before, type_, name, after)
        self._init_fields()
        stringUtil: StringUtil = StringUtil.getInstance()
        self.value = stringUtil.EMPTY_STRING
        self.addAttribute(self.VALUE, value)
from org.allbinary.logic.string.StringUtil import StringUtil



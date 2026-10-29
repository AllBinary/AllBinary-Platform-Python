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

from org.allbinary.logic.visual.dhtml.html.HtmlTag import HtmlTag


class HtmlInput(HtmlTag):

    def _init_fields(self) -> None:
        self.END: str = ">"
        self.STARTINPUT: str = "<INPUT "
        self.ENDINPUT: str = "</INPUT>"
        self.TYPE: str = "TYPE=\""
        self.NAME: str = "NAME=\""
        self.before: str = None
        self.type_: str = None
        self.name: str = None
        self.after: str = None
    

    def __init__(self, before: str, type_: str, name: str, after: str) -> None:
        super().__init__()
        self._init_fields()
        self.before = before
        self.type_ = type_
        self.name = name
        self.after = after
    

    def toString(self) -> str:
        stringUtil: StringUtil = StringUtil.getInstance()
        result: str = stringUtil.EMPTY_STRING
        attributeKeys: list[object] = self.otherAttributes.keySet().toArray()
        attributeSize: int = len(attributeKeys)
        result = self.before
        result += self.STARTINPUT
        result += self.TYPE
        result += self.type_
        result += "\" "
        result += self.NAME
        result += self.name
        result += "\" "
        for i in range(0, attributeSize):
            key: str = attributeKeys[i]
            value: str = self.otherAttributes.get(key)
            if value is not None and ((value > stringUtil.EMPTY_STRING) - (value < stringUtil.EMPTY_STRING)) != 0:
                result += key
                result += "=\""
                result += value
                result += "\" "
        result += self.END
        result += self.ENDINPUT
        result += self.after
        return result

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringUtil import StringUtil



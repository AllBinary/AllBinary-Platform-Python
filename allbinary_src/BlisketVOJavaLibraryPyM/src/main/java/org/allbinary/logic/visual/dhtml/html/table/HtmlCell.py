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
# package org.allbinary.logic.visual.dhtml.html.table

from __future__ import annotations

from org.allbinary.logic.visual.dhtml.html.HtmlTag import HtmlTag


class HtmlCell(HtmlTag):

    def _init_fields(self) -> None:
        self.END: str = ">"
        self.START: str = "<td "
        self.ENDTAG: str = "</td>"
        self.HEIGHT: str = "height"
        self.WIDTH: str = "width"
        self.height: str = None
        self.width: str = None
        self.before: str = None
        self.body: str = None
        self.after: str = None
    

    def __init__(self, before: str, width: str, height: str, after: str) -> None:
        super().__init__()
        self._init_fields()
        self.before = str(before)
        self.after = str(after)
        self.height = str(height)
        self.width = str(width)
        self.addAttribute(self.HEIGHT, self.height)
        self.addAttribute(self.WIDTH, self.width)
    

    def addText(self, body: str) -> None:
        self.body = body
    

    def toString(self) -> str:
        stringUtil: StringUtil = StringUtil.getInstance()
        result: str = stringUtil.EMPTY_STRING
        attributeKeys: list[object] = self.otherAttributes.keySet().toArray()
        attributeSize: int = len(attributeKeys)
        result = self.before
        result += self.START
        result += " "
        for i in range(0, attributeSize):
            key: str = attributeKeys[i]
            value: str = self.otherAttributes.get(key)
            if value is not None and ((value > stringUtil.EMPTY_STRING) - (value < stringUtil.EMPTY_STRING)) != 0:
                result += key
                result += "=\""
                result += value
                result += "\" "
        result += self.END
        result += self.body
        result += self.ENDTAG
        result += self.after
        return result

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringUtil import StringUtil



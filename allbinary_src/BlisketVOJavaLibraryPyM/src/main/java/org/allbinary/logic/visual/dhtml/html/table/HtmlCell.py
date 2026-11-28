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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.visual.dhtml.html.HtmlTag import HtmlTag


@java_inherited_overloads
class HtmlCell(HtmlTag):
    def _java_defaults(self):
        vars(self).setdefault("END", None)
        vars(self).setdefault("START", None)
        vars(self).setdefault("ENDTAG", None)
        vars(self).setdefault("HEIGHT", None)
        vars(self).setdefault("WIDTH", None)
        vars(self).setdefault("height", None)
        vars(self).setdefault("width", None)
        vars(self).setdefault("before", None)
        vars(self).setdefault("body", None)
        vars(self).setdefault("after", None)

    def _init_fields(self) -> None:
        self.END: str = ">"
        self.START: str = "<td "
        self.ENDTAG: str = "</td>"
        self.HEIGHT: str = "height"
        self.WIDTH: str = "width"
        if "height" not in vars(self): self.height: str = None
        if "width" not in vars(self): self.width: str = None
        if "before" not in vars(self): self.before: str = None
        if "body" not in vars(self): self.body: str = None
        if "after" not in vars(self): self.after: str = None
    

    def __init__(self, before: str, width: str, height: str, after: str) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.before = str(before)
        self.after = str(after)
        self.height = str(height)
        self.width = str(width)
        self.addAttribute(self.HEIGHT, self.height)
        self.addAttribute(self.WIDTH, self.width)
    

    def addText(self, body: str) -> None:
        self.body = body
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        stringUtil: StringUtil = StringUtil.getInstance()
        result: str = stringUtil.EMPTY_STRING
        attributeKeys: list[object] = self.otherAttributes.keySet().toArray()
        attributeSize: int = len(attributeKeys)
        result = self.before
        result += str(self.START)
        result += " "
        for i in range(0, attributeSize):
            key: str = attributeKeys[i]
            value: str = self.otherAttributes.get(key)
            if value is not None and ((value > stringUtil.EMPTY_STRING) - (value < stringUtil.EMPTY_STRING)) != 0:
                result += str(key)
                result += "=\""
                result += str(value)
                result += "\" "
        result += str(self.END)
        result += str(self.body)
        result += str(self.ENDTAG)
        result += str(self.after)
        return result

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.logic.string.StringUtil import StringUtil



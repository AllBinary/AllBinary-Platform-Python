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
from org.allbinary.logic.visual.dhtml.html.HtmlTag import HtmlTag


@java_inherited_overloads
class HtmlInput(HtmlTag):
    def _java_defaults(self):
        vars(self).setdefault("END", None)
        vars(self).setdefault("STARTINPUT", None)
        vars(self).setdefault("ENDINPUT", None)
        vars(self).setdefault("TYPE", None)
        vars(self).setdefault("NAME", None)
        vars(self).setdefault("before", None)
        vars(self).setdefault("type_", None)
        vars(self).setdefault("name", None)
        vars(self).setdefault("after", None)

    def _init_fields(self) -> None:
        self.END: str = ">"
        self.STARTINPUT: str = "<INPUT "
        self.ENDINPUT: str = "</INPUT>"
        self.TYPE: str = "TYPE=\""
        self.NAME: str = "NAME=\""
        if "before" not in vars(self): self.before: str = None
        if "type_" not in vars(self): self.type_: str = None
        if "name" not in vars(self): self.name: str = None
        if "after" not in vars(self): self.after: str = None
    

    def __init__(self, before: str, type_: str, name: str, after: str) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.before = before
        self.type_ = type_
        self.name = name
        self.after = after
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        stringUtil: StringUtil = StringUtil.getInstance()
        result: str = stringUtil.EMPTY_STRING
        attributeKeys: list[object] = self.otherAttributes.keySet().toArray()
        attributeSize: int = len(attributeKeys)
        result = self.before
        result += str(self.STARTINPUT)
        result += str(self.TYPE)
        result += str(self.type_)
        result += "\" "
        result += str(self.NAME)
        result += str(self.name)
        result += "\" "
        for i in range(0, attributeSize):
            key: str = attributeKeys[i]
            value: str = self.otherAttributes.get(key)
            if value is not None and ((value > stringUtil.EMPTY_STRING) - (value < stringUtil.EMPTY_STRING)) != 0:
                result += str(key)
                result += "=\""
                result += str(value)
                result += "\" "
        result += str(self.END)
        result += str(self.ENDINPUT)
        result += str(self.after)
        return result

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.logic.string.StringUtil import StringUtil



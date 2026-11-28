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
class HtmlTable(HtmlTag):
    def _java_defaults(self):
        vars(self).setdefault("END", None)
        vars(self).setdefault("START", None)
        vars(self).setdefault("ENDTAG", None)
        vars(self).setdefault("CLASS", None)
        vars(self).setdefault("DIRECTION", None)
        vars(self).setdefault("ID", None)
        vars(self).setdefault("LANG", None)
        vars(self).setdefault("UNITS", None)
        vars(self).setdefault("BORDER", None)
        vars(self).setdefault("CELLPADDING", None)
        vars(self).setdefault("CELLSPACING", None)
        vars(self).setdefault("COLS", None)
        vars(self).setdefault("FLOAT", None)
        vars(self).setdefault("FRAME", None)
        vars(self).setdefault("RULES", None)
        vars(self).setdefault("STYLE", None)
        vars(self).setdefault("BORDERCOLLAPSE", None)
        vars(self).setdefault("numberOfColumns", 0)
        vars(self).setdefault("before", None)
        vars(self).setdefault("border", None)
        vars(self).setdefault("cellpadding", None)
        vars(self).setdefault("cellspacing", None)
        vars(self).setdefault("style", None)
        vars(self).setdefault("name", None)
        vars(self).setdefault("after", None)
        vars(self).setdefault("htmlRowsVector", None)

    def _init_fields(self) -> None:
        self.END: str = ">"
        self.START: str = "<table "
        self.ENDTAG: str = "</table>"
        self.CLASS: str = "class"
        self.DIRECTION: str = "dir"
        self.ID: str = "id"
        self.LANG: str = "lang"
        self.UNITS: str = "units"
        self.BORDER: str = "border"
        self.CELLPADDING: str = "cellpadding"
        self.CELLSPACING: str = "cellspacing"
        self.COLS: str = "cols"
        self.FLOAT: str = "float"
        self.FRAME: str = "frame"
        self.RULES: str = "rules"
        self.STYLE: str = "style"
        self.BORDERCOLLAPSE: str = "border-collapse: collapse"
        self.numberOfColumns: int = 0
        if "before" not in vars(self): self.before: str = None
        if "border" not in vars(self): self.border: str = None
        if "cellpadding" not in vars(self): self.cellpadding: str = None
        if "cellspacing" not in vars(self): self.cellspacing: str = None
        if "style" not in vars(self): self.style: str = None
        if "name" not in vars(self): self.name: str = None
        if "after" not in vars(self): self.after: str = None
        if "htmlRowsVector" not in vars(self): self.htmlRowsVector: BasicArrayList = None
    

    def __init__(self, before: str, cellpadding: str, cellspacing: str, after: str) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
        super().__init__()
        __class__._init_fields(self)
        self.before = before
        self.cellpadding = cellpadding
        self.cellspacing = cellspacing
        self.after = after
        self.htmlRowsVector = BasicArrayListD()
        self.addAttribute(self.BORDER, CommonPhoneStrings.getInstance().ZERO)
        self.addAttribute(self.CELLPADDING, self.cellpadding)
        self.addAttribute(self.CELLSPACING, self.cellspacing)
        self.addAttribute(self.STYLE, self.BORDERCOLLAPSE)
    

    def addRow(self, htmlRow: HtmlRow) -> None:
        if self.numberOfColumns < htmlRow.getNumberOfColumns():
            self.numberOfColumns = htmlRow.getNumberOfColumns()
        self.htmlRowsVector.add(htmlRow)
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        stringUtil: StringUtil = StringUtil.getInstance()
        result: str = stringUtil.EMPTY_STRING
        attributeKeys: list[object] = self.otherAttributes.keySet().toArray()
        result = self.before
        result += str(self.START)
        result += " "
        for i in range(0, len(attributeKeys)):
            key: str = attributeKeys[i]
            value: str = self.otherAttributes.get(key)
            if value is not None and ((value > stringUtil.EMPTY_STRING) - (value < stringUtil.EMPTY_STRING)) != 0:
                result += str(key)
                result += "=\""
                result += str(value)
                result += "\" "
        result += str(self.END)
        size: int = self.htmlRowsVector.size()
        for i in range(0, size):
            result += str(str(self.htmlRowsVector.get(i)))
            result += " "
        result += str(self.ENDTAG)
        result += str(self.after)
        return result

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings



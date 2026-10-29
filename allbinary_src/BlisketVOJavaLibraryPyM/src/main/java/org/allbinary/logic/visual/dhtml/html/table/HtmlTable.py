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


class HtmlTable(HtmlTag):

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
        self.before: str = None
        self.border: str = None
        self.cellpadding: str = None
        self.cellspacing: str = None
        self.style: str = None
        self.name: str = None
        self.after: str = None
        self.htmlRowsVector: BasicArrayList = None
    

    def __init__(self, before: str, cellpadding: str, cellspacing: str, after: str) -> None:
        super().__init__()
        self._init_fields()
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
        stringUtil: StringUtil = StringUtil.getInstance()
        result: str = stringUtil.EMPTY_STRING
        attributeKeys: list[object] = self.otherAttributes.keySet().toArray()
        result = self.before
        result += self.START
        result += " "
        for i in range(0, len(attributeKeys)):
            key: str = attributeKeys[i]
            value: str = self.otherAttributes.get(key)
            if value is not None and ((value > stringUtil.EMPTY_STRING) - (value < stringUtil.EMPTY_STRING)) != 0:
                result += key
                result += "=\""
                result += value
                result += "\" "
        result += self.END
        size: int = self.htmlRowsVector.size()
        for i in range(0, size):
            result += str(self.htmlRowsVector.get(i))
            result += " "
        result += self.ENDTAG
        result += self.after
        return result

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings



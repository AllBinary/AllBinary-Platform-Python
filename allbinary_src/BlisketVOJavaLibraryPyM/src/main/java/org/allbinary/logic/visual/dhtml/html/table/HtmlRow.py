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


class HtmlRow(HtmlTag):

    def _init_fields(self) -> None:
        self.END: str = ">"
        self.START: str = "<tr "
        self.ENDTAG: str = "</tr>"
        self.numberOfColumns: int = 0
        self.before: str = None
        self.after: str = None
        self.htmlCellsVector: BasicArrayList = None
    

    def __init__(self, before: str, after: str) -> None:
        super().__init__()
        self._init_fields()
        self.before = str(before)
        self.after = str(after)
        self.htmlCellsVector = BasicArrayListD()
    

    def addCell(self, htmlCell: HtmlCell) -> None:
        self.htmlCellsVector.add(htmlCell)
        self.numberOfColumns += 1
    

    def getNumberOfColumns(self) -> int:
        return self.numberOfColumns
    

    def toString(self) -> str:
        stringUtil: StringUtil = StringUtil.getInstance()
        result: str = stringUtil.EMPTY_STRING
        attributeKeys: list[object] = self.otherAttributes.keySet().toArray()
        attributeSize: int = len(attributeKeys)
        cellSize: int = self.htmlCellsVector.size()
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
        for i in range(0, cellSize):
            result += str(self.htmlCellsVector.get(i))
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



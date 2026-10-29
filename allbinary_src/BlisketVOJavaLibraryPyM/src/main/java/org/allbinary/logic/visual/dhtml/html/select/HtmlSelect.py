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
# package org.allbinary.logic.visual.dhtml.html.select

from __future__ import annotations

from org.allbinary.logic.visual.dhtml.html.HtmlTag import HtmlTag


class HtmlSelect(HtmlTag):

    def _init_fields(self) -> None:
        self.END: str = ">"
        self.STARTSELECT: str = "<SELECT "
        self.ENDSELECT: str = "</SELECT>"
        self.SIZE: str = "SIZE=\""
        self.NAME: str = "NAME=\""
        self.STARTOPTION: str = "<OPTION"
        self.SELETED: str = "SELECTED"
        self.ENDOPTION: str = "</OPTION>"
        self.before: str = None
        self.name: str = None
        self.after: str = None
        self.size: str = None
        self.selected: str = None
        self.options: BasicArrayList = None
        self.multiple: str = "multiple"
        self.isMultipleSelect: bool = False
    

    def __init__(self, before: str, size: str, name: str, after: str) -> None:
        super().__init__()
        self._init_fields()
        self.before = before
        self.size = size
        self.name = name
        self.after = after
        self.options = BasicArrayListD()
    

    def addOption(self, key: str) -> None:
        self.options.add(key)
    

    def addOptions(self, fileName: str) -> None:
        try:
            lineReader: LineReader = LineReader(fileName)
            while lineReader.hasNext():
                option: str = lineReader.next()
                self.addOption(option)
        except Exception as e:
            self.addOption("Error")
    

    def setSelected(self, selected: str) -> None:
        self.selected = selected
    

    def isMultiple(self) -> bool:
        return self.isMultipleSelect
    

    def setMultiple(self, value: bool) -> None:
        self.isMultipleSelect = value
    

    def getOptions(self) -> str:
        stringUtil: StringUtil = StringUtil.getInstance()
        result: str = stringUtil.EMPTY_STRING
        optionsArray: list[object] = self.options.toArray()
        optionsSize: int = len(optionsArray)
        for i in range(0, optionsSize):
            value: str = optionsArray[i]
            if value is not None and value.compareTo(stringUtil.EMPTY_STRING) != 0:
                result += self.STARTOPTION
                result += self.END
                result += value
                result += self.ENDOPTION
        return result
    

    def toString(self) -> str:
        stringUtil: StringUtil = StringUtil.getInstance()
        result: str = stringUtil.EMPTY_STRING
        attributeKeys: list[object] = self.otherAttributes.keySet().toArray()
        attributeSize: int = len(attributeKeys)
        result = self.before
        result += self.STARTSELECT
        result += self.NAME
        result += self.name
        result += "\" "
        result += self.SIZE
        result += self.size
        result += "\" "
        for i in range(0, attributeSize):
            key: str = attributeKeys[i]
            value: str = self.otherAttributes.get(key)
            if value is not None and value.compareTo(stringUtil.EMPTY_STRING) != 0:
                result += key
                result += "=\""
                result += value
                result += "\" "
        if self.isMultiple():
            result += " " + self.multiple + " "
        result += self.END
        result += self.getOptions()
        result += self.ENDSELECT
        result += self.after
        return result

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.io.LineReader import LineReader
from org.allbinary.logic.string.StringUtil import StringUtil



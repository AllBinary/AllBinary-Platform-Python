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
# package org.allbinary.logic.visual.dhtml.html

from __future__ import annotations



class HtmlForm:

    def _init_fields(self) -> None:
        self.FORMBEGIN: str = "<form "
        self.END: str = ">"
        self.FORMEND: str = "</form>"
        self.ACTION: str = "ACTION=\""
        self.GET: str = "GET\""
        self.POST: str = "POST\""
        self.METHODS: list[str] = [self.GET, self.POST]
        self.METHOD: str = "METHOD=\""
        self.method: str = None
        self.action: str = None
        self.inputs: BasicArrayList = None
    

    def __init__(self, action: str) -> None:
        self._init_fields()
        self.action = action
        self.inputs = BasicArrayListD()
    

    def setPost(self) -> None:
        self.method = self.POST
    

    def setGet(self) -> None:
        self.method = self.GET
    

    def addInput(self, htmlInput: HtmlInput) -> None:
        self.inputs.add(htmlInput)
    

    def addTable(self, htmlTable: HtmlTable) -> None:
        self.inputs.add(htmlTable)
    

    def toString(self) -> str:
        stringUtil: StringUtil = StringUtil.getInstance()
        result: str = stringUtil.EMPTY_STRING
        inputArray: list[object] = self.inputs.toArray()
        inputSize: int = len(inputArray)
        result = self.FORMBEGIN
        result += self.METHOD
        result += self.method
        result += "\" "
        result += self.ACTION
        result += self.action
        result += "\" "
        result += self.END
        for i in range(0, inputSize):
            result += str(inputArray[i])
            result += " "
        result += self.FORMEND
        return result

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.visual.dhtml.html.input.HtmlInput import HtmlInput
from org.allbinary.logic.visual.dhtml.html.table.HtmlTable import HtmlTable



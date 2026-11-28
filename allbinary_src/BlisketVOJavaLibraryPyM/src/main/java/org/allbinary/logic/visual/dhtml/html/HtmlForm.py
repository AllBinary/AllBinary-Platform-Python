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
        if "method" not in vars(self): self.method: str = None
        if "action" not in vars(self): self.action: str = None
        if "inputs" not in vars(self): self.inputs: BasicArrayList = None
    

    def __init__(self, action: str) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        __class__._init_fields(self)
        self.action = action
        self.inputs = BasicArrayListD()
    

    def setPost(self) -> None:
        self.method = self.POST
    

    def setGet(self) -> None:
        self.method = self.GET
    

    def addInput(self, htmlInput: HtmlInput) -> None:
        from org.allbinary.logic.visual.dhtml.html.input.HtmlInput import HtmlInput
        self.inputs.add(htmlInput)
    

    def addTable(self, htmlTable: HtmlTable) -> None:
        from org.allbinary.logic.visual.dhtml.html.table.HtmlTable import HtmlTable
        self.inputs.add(htmlTable)
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        stringUtil: StringUtil = StringUtil.getInstance()
        result: str = stringUtil.EMPTY_STRING
        inputArray: list[object] = self.inputs.toArray()
        inputSize: int = len(inputArray)
        result = self.FORMBEGIN
        result += str(self.METHOD)
        result += str(self.method)
        result += "\" "
        result += str(self.ACTION)
        result += str(self.action)
        result += "\" "
        result += str(self.END)
        for i in range(0, inputSize):
            result += str(str(inputArray[i]))
            result += " "
        result += str(self.FORMEND)
        return result

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.visual.dhtml.html.input.HtmlInput import HtmlInput
# from org.allbinary.logic.visual.dhtml.html.table.HtmlTable import HtmlTable



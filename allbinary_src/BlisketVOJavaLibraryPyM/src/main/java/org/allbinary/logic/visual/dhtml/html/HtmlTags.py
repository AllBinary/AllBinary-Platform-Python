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



class HtmlTags:

    def _init_fields(self) -> None:
        self.htmlTagVector: BasicArrayList = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.htmlTagVector = BasicArrayListD()
    

    def get(self, index: int) -> HtmlTag:
        return self.htmlTagVector.get(index)
    

    def add(self, htmlTag: HtmlTag) -> None:
        self.htmlTagVector.add(htmlTag)
    

    def size(self) -> int:
        return self.htmlTagVector.size()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil



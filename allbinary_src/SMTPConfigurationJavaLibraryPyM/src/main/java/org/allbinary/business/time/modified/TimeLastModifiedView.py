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
# package org.allbinary.business.time.modified

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class TimeLastModifiedView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.timeLastModified: TimeLastModified = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, timeLastModified: TimeLastModified) -> None:
        self._init_fields()
        self.setTimeLastModified(timeLastModified)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.business.time.modified.TimeLastModified import TimeLastModified
        self._init_fields()
        self.setTimeLastModified(TimeLastModified(DomNodeHelper.getTextNodeValue(node)))
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        return ModDomHelper.createTextNode(document, EntryData.getInstance().TIMECREATED, str(self.getTimeLastModified()))
    

    def getTimeLastModified(self) -> TimeLastModified:
        return self.timeLastModified
    

    def setTimeLastModified(self, timeLastModified: TimeLastModified) -> None:
        self.timeLastModified = timeLastModified
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



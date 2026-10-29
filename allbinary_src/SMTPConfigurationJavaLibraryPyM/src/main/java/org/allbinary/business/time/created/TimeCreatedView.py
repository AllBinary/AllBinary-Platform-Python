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
# package org.allbinary.business.time.created

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class TimeCreatedView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.timeCreated: TimeCreated = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, timeCreated: TimeCreated) -> None:
        self._init_fields()
        self.setTimeCreated(timeCreated)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.business.time.created.TimeCreated import TimeCreated
        self._init_fields()
        self.setTimeCreated(TimeCreated(DomNodeHelper.getTextNodeValue(node)))
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        return ModDomHelper.createTextNode(document, EntryData.getInstance().TIMECREATED, str(self.getTimeCreated()))
    

    def getTimeCreated(self) -> TimeCreated:
        return self.timeCreated
    

    def setTimeCreated(self, timeCreated: TimeCreated) -> None:
        self.timeCreated = timeCreated
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



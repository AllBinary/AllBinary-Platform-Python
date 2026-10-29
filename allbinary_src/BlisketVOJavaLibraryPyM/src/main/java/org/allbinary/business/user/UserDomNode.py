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
# package org.allbinary.business.user

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class UserDomNode(DomNodeInterface):

    def _init_fields(self) -> None:
        self.dataMappingInterface: TableMappingInterface = None
    

    def __init__(self, dataMappingInterface: TableMappingInterface) -> None:
        self._init_fields()
        self.dataMappingInterface = dataMappingInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.UserData import UserData
        EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        hashMap: dict = self.dataMappingInterface.toHashMap()
        hashMap.put(EntryData.getInstance().LASTMODIFIED, EMPTY_STRING)
        hashMap.put(EntryData.getInstance().ENCRYPTION, EMPTY_STRING)
        hashMap.put(UserData.PASSWORD, EMPTY_STRING)
        return ModDomHelper.createNameValueNodes(document, UserData.NAME, hashMap)
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        return None
    

    # throws Exception
    def view(self) -> str:
        return None
# from java.util.HashMap import HashMap
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.string.StringUtil import StringUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



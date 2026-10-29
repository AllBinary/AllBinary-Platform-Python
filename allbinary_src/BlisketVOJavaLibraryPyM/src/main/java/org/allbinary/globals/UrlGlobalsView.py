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
# package org.allbinary.globals

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class UrlGlobalsView(DomNodeInterface):
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.globals.UrlGlobalsData import UrlGlobalsData
        from org.allbinary.globals.UrlGlobalsData import UrlGlobalsData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(UrlGlobalsData.WEBAPPPATH, org.allbinary.globals.URLGLOBALS.getWebappPath())
        node: Node = ModDomHelper.createNameValueNodes(document, UrlGlobalsData.NAME, hashMap)
        return node
# from java.util.HashMap import HashMap
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



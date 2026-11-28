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
# package org.allbinary.data.tree.dom

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class FileDomDataModel(DomNodeInterface):

    def _init_fields(self) -> None:
        if "file" not in vars(self): self.file: AbFile = None
    

    def __init__(self, file: AbFile) -> None:
        from org.allbinary.logic.io.file.AbFile import AbFile
        __class__._init_fields(self)
        self.file = file
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.data.tree.dom.FileTableMapping import FileTableMapping
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from java.util.HashMap import HashMap
        from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        tableMappingInterface: TableMappingInterface = FileTableMapping(self.file)
        hashMap: HashMap = tableMappingInterface.toHashMap()
        return ModDomHelper.createNodeWithValueNodes(document, "file", hashMap)
# from java.util.HashMap import HashMap
# from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node



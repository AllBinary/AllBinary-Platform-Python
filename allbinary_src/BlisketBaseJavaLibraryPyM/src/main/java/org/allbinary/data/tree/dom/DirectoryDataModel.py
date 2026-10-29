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

from org.allbinary.logic.visual.transform.TransformInterface import TransformInterface
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class DirectoryDataModel(DomNodeInterface, TransformInterface):

    def _init_fields(self) -> None:
        self.fileBasicArrayList: BasicArrayList = None
        self.transformDocumentInterface: TransformDocumentInterface = None
        self.NO_TYPE: int = 0
    

    def __init__(self, file: AbFile) -> None:
        self._init_fields()
        self.fileBasicArrayList = Directory.getInstance().search(file)
        self.transformDocumentInterface = TransformDocumentFactory.getInstance()
    

    def getTypeId(self) -> int:
        return self.NO_TYPE
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        return None
    

    def setTransformDocumentInterface(self, transformDocumentInterface: TransformDocumentInterface) -> None:
        self.transformDocumentInterface = transformDocumentInterface
    

    def getTransformDocumentInterface(self) -> TransformDocumentInterface:
        return self.transformDocumentInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.data.tree.dom.FileDomDataModel import FileDomDataModel
        dirNode: Node = document.createElement("dir")
        size: int = self.fileBasicArrayList.size()
        nextFile: AbFile = None
        fileNode: Node = None
        for index in range(0, size):
            nextFile = self.fileBasicArrayList.get(index)
            fileNode = FileDomDataModel(nextFile).toXmlNode(document)
            dirNode.appendChild(fileNode)
        return dirNode
    

    # throws Exception
    def toXmlDoc(self) -> Document:
        return self.getTransformDocumentInterface().getDoc()
    

    # throws Exception
    def view(self) -> str:
        node: Node = self.toXmlNode(self.getTransformDocumentInterface().getDoc())
        self.getTransformDocumentInterface().getBaseNode().appendChild(node)
        return XmlDocumentHelper.toString(self.getTransformDocumentInterface().getDoc())
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.directory.Directory import Directory
from org.allbinary.logic.visual.transform.data.TransformDocumentFactory import TransformDocumentFactory
from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



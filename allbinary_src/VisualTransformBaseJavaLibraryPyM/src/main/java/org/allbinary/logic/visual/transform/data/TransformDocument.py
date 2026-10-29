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
# package org.allbinary.logic.visual.transform.data

from __future__ import annotations

from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface


class TransformDocument(TransformDocumentInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.baseNode: Node = None
        self.document: Document = None
    

    def __init__(self) -> None:
        self._init_fields()
        try:
            self.document = DomDocumentHelper.create()
            allbinaryNode: Node = self.document.createElement("allbinary")
            self.baseNode = allbinaryNode
            self.document.appendChild(self.baseNode)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.putF(self.log(), self, self.commonStrings.CONSTRUCTOR)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
            raise e
    

    def getBaseNode(self) -> Node:
        return self.baseNode
    

    def getDoc(self) -> Document:
        return self.document
    

    # throws Exception
    def log(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        if self.baseNode is not None:
            stringBuffer.append("BaseNode: ")
            stringBuffer.append(self.baseNode.getNodeName())
        else:
            stringBuffer.append("Log-Error: BaseNode is Null")
        stringBuffer.append("\nDocument: ")
        stringBuffer.append(XmlDocumentHelper.toString(self.document))
        return str(stringBuffer)
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



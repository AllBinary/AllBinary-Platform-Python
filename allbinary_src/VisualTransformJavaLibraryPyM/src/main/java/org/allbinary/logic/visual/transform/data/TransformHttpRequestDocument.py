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


class TransformHttpRequestDocument(TransformDocumentInterface):
    language: str = "en"
    local: str = "US"

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "baseNode" not in vars(self): self.baseNode: Node = None
        if "document" not in vars(self): self.document: Document = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            __class__._constructor2(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    def _constructor2(self, pageContext: PageContext, weblisketSession: WeblisketSession) -> None:
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.logic.communication.http.AcceptableResponseGenerator import AcceptableResponseGenerator
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        try:
            contentType: str = AcceptableResponseGenerator.getInstance().get(pageContext.getRequest())
            self.document = DomDocumentHelper.create()
            contentTypeNode: Node = self.document.createElement(contentType)
            languageTypeNode: Node = self.document.createElement(TransformHttpRequestDocument.language)
            localTypeNode: Node = self.document.createElement(TransformHttpRequestDocument.local)
            self.baseNode = localTypeNode
            languageTypeNode.appendChild(localTypeNode)
            contentTypeNode.appendChild(languageTypeNode)
            self.document.appendChild(contentTypeNode)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.putF(self.log(), self, self.commonStrings.CONSTRUCTOR)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
            raise e
    

    def _constructor1(self, searchRequest: SearchRequest) -> None:
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.logic.control.search.SearchRequest import SearchRequest
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        try:
            contentType: str = searchRequest.getContentType()
            self.document = DomDocumentHelper.create()
            contentTypeNode: Node = self.document.createElement(contentType)
            languageTypeNode: Node = self.document.createElement(TransformHttpRequestDocument.language)
            localTypeNode: Node = self.document.createElement(TransformHttpRequestDocument.local)
            self.baseNode = localTypeNode
            languageTypeNode.appendChild(localTypeNode)
            contentTypeNode.appendChild(languageTypeNode)
            self.document.appendChild(contentTypeNode)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
            raise e
    

    def getBaseNode(self) -> Node:
        from org.w3c.dom.Node import Node
        return self.baseNode
    

    def getDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return self.document
    

    # throws Exception
    def log(self) -> str:
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        if self.baseNode is not None:
            stringBuffer.append("BaseNode: ")
            stringBuffer.append(self.baseNode.getNodeName())
        else:
            stringBuffer.append("Log-Error: BaseNode is Null")
        stringBuffer.append("\nDocument: ")
        stringBuffer.append(XmlDocumentHelper.toString(self.document))
        return str(stringBuffer)
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
# from org.allbinary.logic.communication.http.AcceptableResponseGenerator import AcceptableResponseGenerator
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.search.SearchRequest import SearchRequest
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



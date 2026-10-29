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
# package org.allbinary.data.tree.dom.document

from __future__ import annotations



class DomDocumentHelper:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def init() -> None:
        System.setProperty("jdk.xml.maxElementDepth", "0")
        System.setProperty("jdk.xml.xpathExprOpLimit", "0")
        System.setProperty("jdk.xml.xpathTotalOpLimit", "0")
        LIMIT: str = "500000"
        System.setProperty("jdk.xml.maxGeneralEntitySizeLimit", LIMIT)
        System.setProperty("jdk.xml.totalEntitySizeLimit", LIMIT)
    

    @staticmethod
    def create() -> Document:
        try:
            factory: DocumentBuilderFactory = DocumentBuilderFactory.newInstance()
            builder: DocumentBuilder = factory.newDocumentBuilder()
            document: Document = builder.newDocument()
            return document
        except Exception as e:
            return None
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def create(inputStream: InputStream) -> Document:
        try:
            factory: DocumentBuilderFactory = DocumentBuilderFactory.newInstance()
            builder: DocumentBuilder = factory.newDocumentBuilder()
            document: Document = builder.parse(inputStream)
            return document
        except Exception as e:
            raise e
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def create(xmlString: str) -> Document:
        try:
            factory: DocumentBuilderFactory = DocumentBuilderFactory.newInstance()
            builder: DocumentBuilder = factory.newDocumentBuilder()
            document: Document = builder.parse(StringBufferInputStream(xmlString))
            return document
        except Exception as e:
            raise e
# from java.io.InputStream import InputStream
# from java.io.StringBufferInputStream import StringBufferInputStream
# from javax.xml.parsers.DocumentBuilder import DocumentBuilder
# from javax.xml.parsers.DocumentBuilderFactory import DocumentBuilderFactory
from org.w3c.dom.Document import Document



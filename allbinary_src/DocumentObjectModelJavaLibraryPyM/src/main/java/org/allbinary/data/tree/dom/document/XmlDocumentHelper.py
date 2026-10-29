# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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



class XmlDocumentHelper:
    instance: XmlDocumentHelper = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.INDENT_NUMBER: str = "indent-number"
        self.transformer: Transformer = None
    

    @staticmethod
    def getInstance() -> XmlDocumentHelper:
        return XmlDocumentHelper.instance
    

    def __init__(self) -> None:
        self._init_fields()
        self.init(4, True)
    

    def init(self, indent: int, ignoreDeclaration: bool) -> None:
        try:
            booleanFactory: BooleanFactory = BooleanFactory.getInstance()
            transformerFactory: TransformerFactory = TransformerFactory.newInstance()
            transformerFactory.setAttribute(self.INDENT_NUMBER, indent)
            self.transformer = transformerFactory.newTransformer()
            self.transformer.setOutputProperty(OutputKeys.ENCODING, CharacterSetData.getInstance().UTF_8)
            self.transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, (booleanFactory.YES if ignoreDeclaration else booleanFactory.NO))
            self.transformer.setOutputProperty(OutputKeys.INDENT, booleanFactory.YES)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.INIT, e)
    

    # throws Exception
    def format(self, xmlString: str) -> str:
        src: InputSource = InputSource(StringReader(xmlString))
        document: Document = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(src)
        out: Writer = StringWriter()
        self.transformer.transform(DOMSource(document), StreamResult(out))
        return str(out)
    

    # throws Exception
    @staticmethod
    def toString(document: Document) -> str:
        try:
            domSource: DOMSource = DOMSource(document)
            byteArrayOutputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            streamResult: StreamResult = StreamResult(byteArrayOutputStream)
            copyTransformerFactory: TransformerFactory = TransformerFactory.newInstance()
            copyTransformer: Transformer = copyTransformerFactory.newTransformer()
            copyTransformer.transform(domSource, streamResult)
            return str(byteArrayOutputStream)
        except Exception as e:
            raise e
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.StringReader import StringReader
# from java.io.StringWriter import StringWriter
# from java.io.Writer import Writer
# from javax.xml.parsers.DocumentBuilderFactory import DocumentBuilderFactory
# from javax.xml.transform.OutputKeys import OutputKeys
# from javax.xml.transform.Transformer import Transformer
# from javax.xml.transform.TransformerFactory import TransformerFactory
# from javax.xml.transform.dom.DOMSource import DOMSource
# from javax.xml.transform.stream.StreamResult import StreamResult
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.java.characters.CharacterSetData import CharacterSetData
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.xml.sax.InputSource import InputSource


XmlDocumentHelper.instance = XmlDocumentHelper()


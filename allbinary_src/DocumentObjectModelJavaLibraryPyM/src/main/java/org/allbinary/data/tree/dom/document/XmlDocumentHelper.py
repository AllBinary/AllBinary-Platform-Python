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

import threading
from java.lang.JavaRuntimeStatic import lazy_static


class XmlDocumentHelper:
    instance: XmlDocumentHelper = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.INDENT_NUMBER: str = "indent-number"
        self.indent: int = 0
        self.ignoreDeclaration: bool = False
    

    @staticmethod
    def getInstance() -> XmlDocumentHelper:
        return XmlDocumentHelper.instance
    

    def __init__(self) -> None:
        self._init_fields()
        self.init(4, True)
    

    def init(self, indent: int, ignoreDeclaration: bool) -> None:
        with self._lock:
            return self._init_unlocked(indent, ignoreDeclaration)

    def _init_unlocked(self, indent: int, ignoreDeclaration: bool) -> None:
        self.indent = indent
        self.ignoreDeclaration = ignoreDeclaration
    

    # throws TransformerConfigurationException
    def createTransformer_j2(self, indent: int, ignoreDeclaration: bool) -> Transformer:
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        from org.allbinary.logic.java.characters.CharacterSetData import CharacterSetData
        booleanFactory: BooleanFactory = BooleanFactory.getInstance()
        transformerFactory: TransformerFactory = TransformerFactory.newInstance()
        transformerFactory.setAttribute(self.INDENT_NUMBER, indent)
        transformer: Transformer = transformerFactory.newTransformer()
        transformer.setOutputProperty(OutputKeys.ENCODING, CharacterSetData.getInstance().UTF_8)
        transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, (booleanFactory.YES if ignoreDeclaration else booleanFactory.NO))
        transformer.setOutputProperty(OutputKeys.INDENT, booleanFactory.YES)
        return transformer
    

    # throws TransformerConfigurationException
    def createTransformer_j0(self) -> Transformer:
        currentIndent: int = 0
        currentIgnoreDeclaration: bool = False
        with self._lock:  # synchronized (self)
            currentIndent = self.indent
            currentIgnoreDeclaration = self.ignoreDeclaration
        return self.createTransformer(currentIndent, currentIgnoreDeclaration)

    def createTransformer(self, *args):
        return getattr(self, "createTransformer_j" + str(len(args)))(*args)
    

    # throws Exception
    def format(self, xmlString: str) -> str:
        return self.formatWithTransformer(xmlString, self.createTransformer())
    

    # throws Exception
    def formatWithTransformer(self, xmlString: str, transformer: Transformer) -> str:
        from java.io.Writer import Writer
        from org.w3c.dom.Document import Document
        from org.xml.sax.InputSource import InputSource
        src: InputSource = InputSource(StringReader(xmlString))
        document: Document = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(src)
        out: Writer = StringWriter()
        transformer.transform(DOMSource(document), StreamResult(out))
        return str(out)
    

    # throws Exception
    @staticmethod
    def toString(document: Document) -> str:
        from org.w3c.dom.Document import Document
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
# from javax.xml.transform.TransformerConfigurationException import TransformerConfigurationException
# from javax.xml.transform.TransformerFactory import TransformerFactory
# from javax.xml.transform.dom.DOMSource import DOMSource
# from javax.xml.transform.stream.StreamResult import StreamResult
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
# from org.allbinary.logic.java.characters.CharacterSetData import CharacterSetData
# from org.w3c.dom.Document import Document
# from org.xml.sax.InputSource import InputSource


def _XmlDocumentHelper_instance() -> object:
    return XmlDocumentHelper()

lazy_static(XmlDocumentHelper, "instance", _XmlDocumentHelper_instance)


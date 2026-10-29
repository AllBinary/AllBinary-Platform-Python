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



#import org.allbinary.data.tree.dom.document.DomDocumentHelper;
class XslHelper:
    instance: XslHelper = None
    

    @staticmethod
    def getInstance() -> XslHelper:
        return XslHelper.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def translate(self, xsltStreamSource: StreamSource, xmlStreamSource: StreamSource, streamResult: StreamResult) -> OutputStream:
        try:
            transformerFactory: TransformerFactory = TransformerFactory.newInstance()
            transformer: Transformer = transformerFactory.newTransformer(xsltStreamSource)
            transformer.transform(xmlStreamSource, streamResult)
            return streamResult.getOutputStream()
        except Exception as e:
            raise e
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def translate(self, resolver: URIResolver, xsltStreamSource: StreamSource, xmlStreamSource: StreamSource, streamResult: StreamResult) -> OutputStream:
        try:
            tFactory: TransformerFactory = TransformerFactory.newInstance()
            tFactory.setURIResolver(resolver)
            transformer: Transformer = tFactory.newTransformer(xsltStreamSource)
            transformer.transform(xmlStreamSource, streamResult)
            return streamResult.getOutputStream()
        except Exception as e:
            raise e
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def translate(self, xsltStreamSource: StreamSource, xmlDocument: Document) -> str:
        try:
            outputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            return str(self.translate(xsltStreamSource, StreamSource(StringBufferInputStream(XmlDocumentHelper.toString(xmlDocument))), StreamResult(outputStream)))
        except Exception as e:
            raise e
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def translate(self, xsltStreamSource: StreamSource, xmlStreamSource: StreamSource) -> str:
        try:
            outputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            return str(self.translate(xsltStreamSource, xmlStreamSource, StreamResult(outputStream)))
        except Exception as e:
            raise e
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def translate(self, resolver: URIResolver, xsltStreamSource: StreamSource, xmlStreamSource: StreamSource) -> str:
        try:
            outputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            return str(self.translate(resolver, xsltStreamSource, xmlStreamSource, StreamResult(outputStream)))
        except Exception as e:
            raise e
    

    # throws Exception
    def export(self, outputFile: File, xsltFilePath: str, xmlDocument: Document) -> None:
        try:
            outputFile.createNewFile()
            self.translate(StreamSource(xsltFilePath), StreamSource(StringBufferInputStream(XmlDocumentHelper.toString(xmlDocument))), StreamResult(outputFile))
        except Exception as e:
            raise e
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.File import File
# from java.io.OutputStream import OutputStream
# from java.io.StringBufferInputStream import StringBufferInputStream
# from javax.xml.transform.Transformer import Transformer
# from javax.xml.transform.TransformerFactory import TransformerFactory
# from javax.xml.transform.URIResolver import URIResolver
# from javax.xml.transform.stream.StreamResult import StreamResult
# from javax.xml.transform.stream.StreamSource import StreamSource
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.w3c.dom.Document import Document


XslHelper.instance = XslHelper()


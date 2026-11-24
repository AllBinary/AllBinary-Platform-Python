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

from java.lang.JavaRuntimeStatic import lazy_static


#import org.allbinary.data.tree.dom.document.DomDocumentHelper;
class XslHelper:
    instance: XslHelper = None
    

    @staticmethod
    def getInstance() -> XslHelper:
        return XslHelper.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def translate_j3_1(self, xsltStreamSource: StreamSource, xmlStreamSource: StreamSource, streamResult: StreamResult) -> OutputStream:
        from java.io.OutputStream import OutputStream
        try:
            transformerFactory: TransformerFactory = TransformerFactory.newInstance()
            transformer: Transformer = transformerFactory.newTransformer(xsltStreamSource)
            transformer.transform(xmlStreamSource, streamResult)
            return streamResult.getOutputStream()
        except Exception as e:
            raise e
    

    # throws Exception
    def translate_j4(self, resolver: URIResolver, xsltStreamSource: StreamSource, xmlStreamSource: StreamSource, streamResult: StreamResult) -> OutputStream:
        from java.io.OutputStream import OutputStream
        try:
            tFactory: TransformerFactory = TransformerFactory.newInstance()
            tFactory.setURIResolver(resolver)
            transformer: Transformer = tFactory.newTransformer(xsltStreamSource)
            transformer.transform(xmlStreamSource, streamResult)
            return streamResult.getOutputStream()
        except Exception as e:
            raise e
    

    # throws Exception
    def translateTemplate(self, templates: Templates, xmlStreamSource: StreamSource) -> str:
        try:
            outputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            streamResult: StreamResult = StreamResult(outputStream)
            templates.newTransformer().transform(xmlStreamSource, streamResult)
            return str(streamResult.getOutputStream())
        except Exception as e:
            raise e
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def translate_j2_1(self, xsltStreamSource: StreamSource, xmlDocument: Document) -> str:
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        from org.w3c.dom.Document import Document
        try:
            outputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            return str(self.translate(xsltStreamSource, StreamSource(StringBufferInputStream(XmlDocumentHelper.toString(xmlDocument))), StreamResult(outputStream)))
        except Exception as e:
            raise e
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def translate_j2_2(self, xsltStreamSource: StreamSource, xmlStreamSource: StreamSource) -> str:
        try:
            outputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            return str(self.translate(xsltStreamSource, xmlStreamSource, StreamResult(outputStream)))
        except Exception as e:
            raise e
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def translate_j3_2(self, resolver: URIResolver, xsltStreamSource: StreamSource, xmlStreamSource: StreamSource) -> str:
        try:
            outputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            return str(self.translate(resolver, xsltStreamSource, xmlStreamSource, StreamResult(outputStream)))
        except Exception as e:
            raise e

    def translate(self, *args):
        if len(args) == 3 and True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and not isinstance(args[2], (str, list, int, float)):
            return self.translate_j3_1(*args)
        if len(args) == 2 and True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)):
            return self.translate_j2_1(*args)
        if len(args) == 2:
            return self.translate_j2_2(*args)
        if len(args) == 3:
            return self.translate_j3_2(*args)
        return getattr(self, "translate_j" + str(len(args)))(*args)
    

    # throws Exception
    def export(self, outputFile: File, xsltFilePath: str, xmlDocument: Document) -> None:
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        from org.w3c.dom.Document import Document
        try:
            outputFile.createNewFile()
            self.translate(StreamSource(xsltFilePath), StreamSource(StringBufferInputStream(XmlDocumentHelper.toString(xmlDocument))), StreamResult(outputFile))
        except Exception as e:
            raise e
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.File import File
# from java.io.OutputStream import OutputStream
# from java.io.StringBufferInputStream import StringBufferInputStream
# from javax.xml.transform.Templates import Templates
# from javax.xml.transform.Transformer import Transformer
# from javax.xml.transform.TransformerFactory import TransformerFactory
# from javax.xml.transform.URIResolver import URIResolver
# from javax.xml.transform.stream.StreamResult import StreamResult
# from javax.xml.transform.stream.StreamSource import StreamSource
# from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
# from org.w3c.dom.Document import Document


def _XslHelper_instance() -> object:
    return XslHelper()

lazy_static(XslHelper, "instance", _XslHelper_instance)


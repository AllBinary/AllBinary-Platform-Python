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
        from java.io.ByteArrayOutputStream import ByteArrayOutputStream
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
        from java.io.ByteArrayOutputStream import ByteArrayOutputStream
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
        from java.io.ByteArrayOutputStream import ByteArrayOutputStream
        try:
            outputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            return str(self.translate(xsltStreamSource, xmlStreamSource, StreamResult(outputStream)))
        except Exception as e:
            raise e
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def translate_j3_2(self, resolver: URIResolver, xsltStreamSource: StreamSource, xmlStreamSource: StreamSource) -> str:
        from java.io.ByteArrayOutputStream import ByteArrayOutputStream
        try:
            outputStream: ByteArrayOutputStream = ByteArrayOutputStream()
            return str(self.translate(resolver, xsltStreamSource, xmlStreamSource, StreamResult(outputStream)))
        except Exception as e:
            raise e

    def translate(self, *args):
        if len(args) == 3 and True and (args[0] is None or any(base.__name__ == "StreamSource" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "StreamSource" for base in type(args[1]).__mro__)) and (args[2] is None or any(base.__name__ == "StreamResult" for base in type(args[2]).__mro__)):
            return __class__.__dict__["translate_j3_1"].__get__(self, __class__)(*args)
        if len(args) == 2 and True and (args[0] is None or any(base.__name__ == "StreamSource" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "Document" for base in type(args[1]).__mro__)):
            return __class__.__dict__["translate_j2_1"].__get__(self, __class__)(*args)
        if len(args) == 2:
            return __class__.__dict__["translate_j2_2"].__get__(self, __class__)(*args)
        if len(args) == 3:
            return __class__.__dict__["translate_j3_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("translate_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().translate(*args)
    

    # throws Exception
    def export(self, outputFile: File, xsltFilePath: str, xmlDocument: Document) -> None:
        from java.io.File import File
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


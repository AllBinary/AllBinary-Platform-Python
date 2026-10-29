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
# package org.allbinary.logic.visual.transform

from __future__ import annotations

from org.allbinary.logic.visual.transform.info.CompositeTransformInfoInterface import CompositeTransformInfoInterface


# Java interface
class BasicTransformerInterface(CompositeTransformInfoInterface):
    

    def setInputStream(self, inputStream: InputStream) -> None:
        raise NotImplementedError()
    

    def setURIResolver(self, uriResolver: URIResolver) -> None:
        raise NotImplementedError()
    

    def getStreamSource(self) -> StreamSource:
        raise NotImplementedError()
    

    def getInputStream(self) -> InputStream:
        raise NotImplementedError()
    

    def getURIResolver(self) -> URIResolver:
        raise NotImplementedError()
    

    # throws Exception
    def translate(self, xmlDocumentStr: str) -> str:
        raise NotImplementedError()
# from java.io.InputStream import InputStream
# from javax.xml.transform.URIResolver import URIResolver
# from javax.xml.transform.stream.StreamSource import StreamSource



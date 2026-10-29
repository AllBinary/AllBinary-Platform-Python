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

from org.allbinary.logic.visual.transform.BasicTransformerInterface import BasicTransformerInterface


class AbTransformer(BasicTransformerInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.transformInfoInterface: TransformInfoInterface = None
        self.inputStream: InputStream = None
        self.uriResolver: URIResolver = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        self._init_fields()
        self.transformInfoInterface = transformInfoInterface
    

    def getTransformInfoInterface(self) -> TransformInfoInterface:
        return self.transformInfoInterface
    

    def setInputStream(self, inputStream: InputStream) -> None:
        self.inputStream = inputStream
    

    def setURIResolver(self, uriResolver: URIResolver) -> None:
        self.uriResolver = uriResolver
    

    def getInputStream(self) -> InputStream:
        return self.inputStream
    

    def getURIResolver(self) -> URIResolver:
        return self.uriResolver
    

    def getStreamSource(self) -> StreamSource:
        return StreamSource(self.getInputStream())
    

    # throws Exception
    def translate(self, xmlDocumentStr: str) -> str:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XMLLOGGING):
                self.logUtil.putF("xml: \n" + xmlDocumentStr, self, "translate(String xmlDocumentStr)")
            if self.getURIResolver() is None:
                raise Exception("No URIResolver")
            result: str = XslHelper.getInstance().translate(self.getURIResolver(), StreamSource(self.getInputStream()), StreamSource(StringBufferInputStream(xmlDocumentStr)))
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XSLLOGGING):
                self.logUtil.putF("translated xml: " + result, self, "translate(String xmlDocumentStr)")
            transformInfoObjectConfigGeneratorInterface: TransformInfoObjectConfigGenerator = TransformInfoObjectConfigGeneratorFactory.getInstance().getInstance(self.getTransformInfoInterface())
            return transformInfoObjectConfigGeneratorInterface.process(result)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.transformInfoInterface.log(), self, "translate(document)", e)
            raise e
# from java.io.InputStream import InputStream
# from java.io.StringBufferInputStream import StringBufferInputStream
# from javax.xml.transform.URIResolver import URIResolver
# from javax.xml.transform.stream.StreamSource import StreamSource
from org.allbinary.data.tree.dom.XslHelper import XslHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.logic.visual.transform.info.objectConfig.generator.TransformInfoObjectConfigGenerator import TransformInfoObjectConfigGenerator
from org.allbinary.logic.visual.transform.info.objectConfig.generator.TransformInfoObjectConfigGeneratorFactory import TransformInfoObjectConfigGeneratorFactory
from org.allbinary.string.CommonStrings import CommonStrings



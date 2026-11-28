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

# from javax.xml.transform.URIResolver import URIResolver


class BasicUriResolver(URIResolver):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.uriResolverStrings: URIResolverStrings = URIResolverStrings.getInstance()
        if "extension" not in vars(self): self.extension: str = None
    

    def __init__(self, extension: str) -> None:
        __class__._init_fields(self)
        self.extension = extension
    

    def getExtension(self) -> str:
        return self.extension
    

    # throws TransformerException
    def resolve(self, href: str, base: str) -> Source:
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
        from org.allbinary.logic.io.path.AbFilePath import AbFilePath
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.visual.transform.info.template.TransformInfoTemplateData import TransformInfoTemplateData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(URLGLOBALS.getMainPath())
            stringBuffer.append(FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
            stringBuffer.append(href)
            abPath: AbPath = AbFilePath(str(stringBuffer))
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().XMLLOGGING):
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(self.uriResolverStrings.ATTEMPT)
                stringBuffer.append(href)
                stringBuffer.append(self.uriResolverStrings.BASE)
                stringBuffer.append(base)
                stringBuffer.append(self.uriResolverStrings.NEW_PATH)
                stringBuffer.append(str(abPath))
                stringBuffer.append(self.uriResolverStrings.NOTE)
                stringBuffer.append(FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
                stringBuffer.append(self.uriResolverStrings.URL_GLOBAL)
                stringBuffer.append(self.uriResolverStrings.REQUIRED_EXTENSION)
                stringBuffer.append(self.extension)
                self.logUtil.putF(str(stringBuffer), self, self.uriResolverStrings.RESOLVE)
            return StreamSource(CryptFileReader(TransformInfoTemplateData.getInstance().UNCRYPTED_EXTENSION, TransformInfoTemplateData.getInstance().ENCRYPTED_EXTENSION).getInputStream(abPath))
        except TransformerException as e:
            raise e
        except Exception as e:
            raise TransformerException(e)
    

    def toString(self) -> str:
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.string.StringMaker import StringMaker
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(URLGLOBALS.getMainPath())
            stringBuffer.append(FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
            stringBuffer.append(self.uriResolverStrings.IMPORT_URL)
            return str(stringBuffer)
        except Exception as e:
            return "BasicUriResolver - Does not work without webapp path should be changed"

    def __str__(self) -> str:
        return self.toString()
# from javax.xml.transform.Source import Source
# from javax.xml.transform.TransformerException import TransformerException
# from javax.xml.transform.stream.StreamSource import StreamSource
# from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
# from org.allbinary.logic.io.path.AbFilePath import AbFilePath
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.visual.transform.info.template.TransformInfoTemplateData import TransformInfoTemplateData
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.data.tree.dom.URIResolverStrings import URIResolverStrings



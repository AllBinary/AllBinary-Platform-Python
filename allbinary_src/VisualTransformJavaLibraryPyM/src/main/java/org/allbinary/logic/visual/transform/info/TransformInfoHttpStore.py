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
# package org.allbinary.logic.visual.transform.info

from __future__ import annotations

from org.allbinary.logic.visual.transform.info.TransformInfoHttp import TransformInfoHttp
from org.allbinary.logic.visual.transform.info.TransformInfoHttpStoreInterface import TransformInfoHttpStoreInterface


class TransformInfoHttpStore(TransformInfoHttp, TransformInfoHttpStoreInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 3:
            self._constructor3(*args)
    

    def _constructor2(self, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__(propertiesHashMap, pageContext, True)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, self.commonStrings.CONSTRUCTOR)
    

    def _constructor3(self, databaseHashMap: dict, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__(databaseHashMap, propertiesHashMap, pageContext)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Database HashMap: ")
            stringBuffer.append(str(databaseHashMap))
            stringBuffer.append("\nProperties HashMap: ")
            stringBuffer.append(str(propertiesHashMap))
            self.logUtil.putF(str(stringBuffer), self, "Constructor(HashMap, HashMap , PageContext)")
        self.setStoreName(databaseHashMap.get(StoreFrontData.getInstance().NAME))
    

    def _constructor3(self, storeFrontInterface: StoreFrontInterface, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__(propertiesHashMap, pageContext)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, self.commonStrings.CONSTRUCTOR)
        self.setStoreName(storeFrontInterface.getName())
    

    # throws Exception
    def getPath(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.URLGLOBALS.getMainPath())
        stringBuffer.append(self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
        stringBuffer.append(self.getStoreName())
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        return str(stringBuffer)
    

    # throws Exception
    def getTemplateFilePath(self) -> AbPath:
        return AbPath(self.getPath(), self.getTemplateFile())
    

    # throws Exception
    def getObjectConfigFilePath(self) -> AbPath:
        return AbPath(self.getPath(), self.getObjectConfigFile())
    

    # throws Exception
    def getDataFilePath(self) -> AbPath:
        return AbPath(self.getPath(), self.getDataFile())
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker



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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.visual.transform.info.TransformInfoHttp import TransformInfoHttp
from org.allbinary.logic.visual.transform.info.TransformInfoHttpStoreInterface import TransformInfoHttpStoreInterface


@java_inherited_overloads
class TransformInfoHttpStore(*java_bases(TransformInfoHttp, TransformInfoHttpStoreInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 2:
            __class__._constructor2(self, *args)
        elif len(args) == 3:
            __class__.__jconstructor3(self, *args)

    def __jconstructor3(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and (args[2] is None or any(base.__name__ == "PageContext" for base in type(args[2]).__mro__)):
            __class__._constructor3_1(self, *args)
        else:
            __class__._constructor3_2(self, *args)
    

    def _constructor2(self, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__(propertiesHashMap, pageContext, True)
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, self.commonStrings.CONSTRUCTOR)
    

    def _constructor3_1(self, databaseHashMap: HashMap, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__(databaseHashMap, propertiesHashMap, pageContext)
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Database HashMap: ")
            stringBuffer.append(str(databaseHashMap))
            stringBuffer.append("\nProperties HashMap: ")
            stringBuffer.append(str(propertiesHashMap))
            self.logUtil.putF(str(stringBuffer), self, "Constructor(HashMap, HashMap , PageContext)")
        self.setStoreName(databaseHashMap.get(StoreFrontData.getInstance().NAME))
    

    def _constructor3_2(self, storeFrontInterface: StoreFrontInterface, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__(propertiesHashMap, pageContext)
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, self.commonStrings.CONSTRUCTOR)
        self.setStoreName(storeFrontInterface.getName())
    

    # throws Exception
    def getPath(self) -> str:
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(URLGLOBALS.getMainPath())
        stringBuffer.append(FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
        stringBuffer.append(self.getStoreName())
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        return str(stringBuffer)
    

    # throws Exception
    def getTemplateFilePath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return AbPath(self.getPath(), self.getTemplateFile())
    

    # throws Exception
    def getObjectConfigFilePath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return AbPath(self.getPath(), self.getObjectConfigFile())
    

    # throws Exception
    def getDataFilePath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return AbPath(self.getPath(), self.getDataFile())
    

    def setStoreName(self, value: str) -> None:
        java_super_call(super(), "setStoreName", value)
    

    def getStoreName(self) -> str:
        return java_super_call(super(), "getStoreName")
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



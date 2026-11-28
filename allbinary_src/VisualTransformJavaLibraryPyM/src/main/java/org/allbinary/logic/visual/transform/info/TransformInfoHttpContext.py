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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.visual.transform.info.TransformInfoHttp import TransformInfoHttp


@java_inherited_overloads
class TransformInfoHttpContext(TransformInfoHttp):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 3:
            __class__._constructor3(self, *args)
        elif len(args) == 2:
            __class__._constructor2(self, *args)
    

    def _constructor3(self, databaseHashMap: HashMap, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
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
            self.logUtil.putF(str(stringBuffer), self, self.commonStrings.CONSTRUCTOR)
        self.setStoreName(StringUtil.getInstance().EMPTY_STRING)
    

    def _constructor2(self, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__(propertiesHashMap, pageContext)
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, self.commonStrings.CONSTRUCTOR)
        self.setStoreName(StringUtil.getInstance().EMPTY_STRING)
    

    # throws Exception
    def getPath(self) -> str:
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(URLGLOBALS.getMainPath())
        stringBuffer.append(FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH)
        stringBuffer.append(FREEBLISKET_PATH_GLOBALS.getInstance().INSTALLPATH)
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
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



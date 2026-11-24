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

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface


class TransformInfoHttp(*java_bases(TransformInfo, TransformInfoHttpInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.business.context.AbContext import AbContext
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abContext: AbContext = None

    def __init__(self, *args) -> None:
        if len(args) == 3:
            self.__jconstructor3(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)

    def __jconstructor3(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and isinstance(args[2], bool):
            self._constructor3_1(*args)
        elif True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and not isinstance(args[2], (str, list, int, float)):
            self._constructor3_2(*args)
        else:
            self._constructor3_3(*args)
    

    def _constructor3_1(self, propertiesHashMap: HashMap, pageContext: PageContext, crud: bool) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.AbContext import AbContext
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        self._init_fields()
        self.abContext = AbContext(propertiesHashMap, pageContext)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, "Constructor(HashMap, PageContext, boolean)")
        self.override(propertiesHashMap)
    

    def _constructor3_2(self, request: HttpServletRequest, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.AbContext import AbContext
        from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        self._init_fields()
        self.abContext = AbContext(propertiesHashMap, pageContext)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, "Constructor(HttpServletRequest, HashMap, PageContext)")
        self.set(RequestParams(request).toHashMap())
        self.override(propertiesHashMap)
    

    def _constructor3_3(self, databaseHashMap: HashMap, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.AbContext import AbContext
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        self._init_fields()
        self.abContext = AbContext(propertiesHashMap, pageContext)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, "Constructor(HashMap, HashMap, PageContext)")
        self.set(databaseHashMap)
    

    def _constructor2(self, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.AbContext import AbContext
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        self._init_fields()
        self.abContext = AbContext(propertiesHashMap, pageContext)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, "Constructor(HashMap, PageContext)")
        self.set(propertiesHashMap)
    

    def _constructor1(self, parentViewOfThisTransformInfoInterface: TransformInfoHttp) -> None:
        from org.allbinary.business.context.AbContext import AbContext
        super().__init__()
        self._init_fields()
        self.abContext = AbContext(parentViewOfThisTransformInfoInterface.getPropertiesHashMap(), parentViewOfThisTransformInfoInterface.getPageContext())
    

    # throws Exception
    def set(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfig import TransformInfoObjectConfig
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(hashMap), self, "set()")
        transformInfoData: TransformInfoData = TransformInfoData.getInstance()
        self.setName(hashMap.get(transformInfoData.NAME))
        self.setStoreName(hashMap.get(StoreFrontData.getInstance().NAME))
        self.setObjectFile(hashMap.get(transformInfoData.OBJECTFILENAME))
        self.setObject(hashMap.get(transformInfoData.OBJECT))
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        objectConfigString: str = hashMap.get(transformInfoData.OBJECTCONFIG)
        if stringValidationUtil.isValidRequired(objectConfigString, 10, AbSqlData.MAXBLOB):
            self.setObjectConfig(objectConfigString)
        else:
            self.setObjectConfig(str(TransformInfoObjectConfig(self)))
        if not stringValidationUtil.isEmpty(hashMap.get(transformInfoData.OBJECTCONFIGFILENAME)):
            self.setObjectConfigFile(hashMap.get(transformInfoData.OBJECTCONFIGFILENAME))
        self.setTemplateFile(hashMap.get(transformInfoData.TEMPLATEFILENAME))
        self.setTemplate(hashMap.get(transformInfoData.TEMPLATE))
        self.setDataFile(hashMap.get(transformInfoData.DATAFILENAME))
        self.setData(hashMap.get(transformInfoData.DATA))
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
            self.logUtil.putF(self.log(), self, "set()")
    

    def getWeblisketSession(self) -> WeblisketSessionInterface:
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface
        return self.abContext.getWeblisketSession()
    

    def getPageContext(self) -> PageContext:
        return self.abContext.getPageContext()
    

    def getPropertiesHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        return self.abContext.getPropertiesHashMap()
    

    # throws Exception
    def getTemplateFilePath(self) -> AbPath:
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.path.AbPath import AbPath
        return AbPath(URLGLOBALS.getMainPath() + FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH, self.getTemplateFile())
    

    # throws Exception
    def getObjectConfigFilePath(self) -> AbPath:
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.path.AbPath import AbPath
        return AbPath(URLGLOBALS.getMainPath() + FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH, self.getObjectConfigFile())
    

    # throws Exception
    def getDataFilePath(self) -> AbPath:
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.path.AbPath import AbPath
        return AbPath(URLGLOBALS.getMainPath() + FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH, self.getDataFile())
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.context.AbContext import AbContext
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
# from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfig import TransformInfoObjectConfig
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



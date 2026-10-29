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

from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface


class TransformInfoHttp(TransformInfo, TransformInfoHttpInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abContext: AbContext = None

    def __init__(self, *args) -> None:
        if len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor3(self, propertiesHashMap: dict, pageContext: PageContext, crud: bool) -> None:
        super().__init__()
        self._init_fields()
        self.abContext = AbContext(propertiesHashMap, pageContext)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, "Constructor(HashMap, PageContext, boolean)")
        self.override(propertiesHashMap)
    

    def _constructor3(self, request: HttpServletRequest, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.abContext = AbContext(propertiesHashMap, pageContext)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, "Constructor(HttpServletRequest, HashMap, PageContext)")
        self.set(RequestParams(request).toHashMap())
        self.override(propertiesHashMap)
    

    def _constructor3(self, databaseHashMap: dict, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.abContext = AbContext(propertiesHashMap, pageContext)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, "Constructor(HashMap, HashMap, PageContext)")
        self.set(databaseHashMap)
    

    def _constructor2(self, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.abContext = AbContext(propertiesHashMap, pageContext)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, "Constructor(HashMap, PageContext)")
        self.set(propertiesHashMap)
    

    def _constructor1(self, parentViewOfThisTransformInfoInterface: TransformInfoHttp) -> None:
        super().__init__()
        self._init_fields()
        self.abContext = AbContext(parentViewOfThisTransformInfoInterface.getPropertiesHashMap(), parentViewOfThisTransformInfoInterface.getPageContext())
    

    # throws Exception
    def set(self, hashMap: dict) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
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
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORY):
            self.logUtil.putF(self.log(), self, "set()")
    

    def getWeblisketSession(self) -> WeblisketSessionInterface:
        return self.abContext.getWeblisketSession()
    

    def getPageContext(self) -> PageContext:
        return self.abContext.getPageContext()
    

    def getPropertiesHashMap(self) -> dict:
        return self.abContext.getPropertiesHashMap()
    

    # throws Exception
    def getTemplateFilePath(self) -> AbPath:
        return AbPath(self.URLGLOBALS.getMainPath() + self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH, self.getTemplateFile())
    

    # throws Exception
    def getObjectConfigFilePath(self) -> AbPath:
        return AbPath(self.URLGLOBALS.getMainPath() + self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH, self.getObjectConfigFile())
    

    # throws Exception
    def getDataFilePath(self) -> AbPath:
        return AbPath(self.URLGLOBALS.getMainPath() + self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH, self.getDataFile())
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.AbContext import AbContext
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfig import TransformInfoObjectConfig



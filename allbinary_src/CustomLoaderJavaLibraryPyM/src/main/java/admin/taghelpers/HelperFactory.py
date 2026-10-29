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
# package admin.taghelpers

from __future__ import annotations



class HelperFactory:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws LicensingException
    @staticmethod
    def getInstance(abeClientInformation: AbeClientInformationInterface, factoryName: str, className: str, hashMap: dict, httpServletRequest: HttpServletRequest) -> object:
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            params: list[object] = [None] * (2)
            classes: list[type] = [None] * (2)
            abeFactory: AbeFactory = AbeFactory.getInstance()
            classes[0] = type(hashMap)
            classes[1] = abeFactory.getClass(abeClientInformation, "javax.servlet.http.HttpServletRequest")
            params[0] = hashMap
            params[1] = httpServletRequest
            anyType: object = abeFactory.getInstance(abeClientInformation, className, classes, params)
            return anyType
        except LicensingException as e:
            error: str = "Failed To Get Instance Args: HashMap=" + str(hashMap) + " HttpServletRequest=" + str(httpServletRequest)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                logUtil.put(error, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            raise e
        except Exception as e:
            error: str = "Failed To Get Instance"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                logUtil.put(error, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            return None
    

    # throws LicensingException
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance(abeClientInformation: AbeClientInformationInterface, factoryName: str, className: str, hashMap: dict, pageContext: PageContext) -> object:
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            params: list[object] = [None] * (2)
            classes: list[type] = [None] * (2)
            abeFactory: AbeFactory = AbeFactory.getInstance()
            classes[0] = type(hashMap)
            classes[1] = abeFactory.getClass(abeClientInformation, "javax.servlet.jsp.PageContext")
            params[0] = hashMap
            params[1] = pageContext
            anyType: object = abeFactory.getInstance(abeClientInformation, className, classes, params)
            return anyType
        except LicensingException as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                error: str = "Failed To Get Instance Args: HashMap=" + str(hashMap) + " PageContext=" + str(pageContext)
                logUtil.put(error, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            return None
    

    # throws LicensingException
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance(abeClientInformation: AbeClientInformationInterface, factoryName: str, className: str, hashMap: dict, specialhashMap: dict, pageContext: PageContext) -> object:
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            params: list[object] = [None] * (3)
            classes: list[type] = [None] * (3)
            abeFactory: AbeFactory = AbeFactory.getInstance()
            classes[0] = type(hashMap)
            classes[1] = type(specialhashMap)
            classes[2] = abeFactory.getClass(abeClientInformation, "javax.servlet.jsp.PageContext")
            params[0] = hashMap
            params[1] = specialhashMap
            params[2] = pageContext
            anyType: object = abeFactory.getInstance(abeClientInformation, className, classes, params)
            return anyType
        except LicensingException as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                error: str = "Failed To Get Instance Args: HashMap=" + str(hashMap) + " PageContext=" + str(pageContext)
                logUtil.put(error, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            return None
    

    # throws LicensingException
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance(abeClientInformation: AbeClientInformationInterface, factoryName: str, className: str) -> object:
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            anyType: object = AbeFactory.getInstance().getInstance(abeClientInformation, className)
            return anyType
        except LicensingException as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            return None
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from org.allbinary.string.CommonStrings import CommonStrings



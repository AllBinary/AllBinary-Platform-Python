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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws LicensingException
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def getInstance_j5_1(abeClientInformation: AbeClientInformationInterface, factoryName: str, className: str, hashMap: HashMap, httpServletRequest: HttpServletRequest) -> object:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                logUtil.put(error, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            raise e
        except Exception as e:
            error: str = "Failed To Get Instance"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                logUtil.put(error, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            return None
    

    # throws LicensingException
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def getInstance_j5_2(abeClientInformation: AbeClientInformationInterface, factoryName: str, className: str, hashMap: HashMap, pageContext: PageContext) -> object:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                error: str = "Failed To Get Instance Args: HashMap=" + str(hashMap) + " PageContext=" + str(pageContext)
                logUtil.put(error, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            raise e
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            return None
    

    # throws LicensingException
    @staticmethod
    def getInstance_j6(abeClientInformation: AbeClientInformationInterface, factoryName: str, className: str, hashMap: HashMap, specialhashMap: HashMap, pageContext: PageContext) -> object:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                error: str = "Failed To Get Instance Args: HashMap=" + str(hashMap) + " PageContext=" + str(pageContext)
                logUtil.put(error, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            raise e
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            return None
    

    # throws LicensingException
    @staticmethod
    def getInstance_j3(abeClientInformation: AbeClientInformationInterface, factoryName: str, className: str) -> object:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            anyType: object = AbeFactory.getInstance().getInstance(abeClientInformation, className)
            return anyType
        except LicensingException as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            raise e
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, factoryName + "->HelperFactory", "getInstance(String, String, HashMap, PageContext)", e)
            return None

    @staticmethod
    def getInstance(*args):
        if len(args) == 5 and True and (args[0] is None or any(base.__name__ == "AbeClientInformationInterface" for base in type(args[0]).__mro__)) and (args[1] is None or isinstance(args[1], str)) and (args[2] is None or isinstance(args[2], str)) and not isinstance(args[3], (str, list, int, float)) and (args[4] is None or any(base.__name__ == "HttpServletRequest" for base in type(args[4]).__mro__)):
            return HelperFactory.getInstance_j5_1(*args)
        if len(args) == 5:
            return HelperFactory.getInstance_j5_2(*args)
        return getattr(HelperFactory, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



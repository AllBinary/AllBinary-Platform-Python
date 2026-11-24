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
# package org.allbinary.logic.control.workflow

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class DbWorkFlowFactory:
    instance: DbWorkFlowFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> DbWorkFlowFactory:
        return DbWorkFlowFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception, LicensingException
    def getInstance_j2(self, abeClientInformation: AbeClientInformationInterface, hashMap: HashMap) -> WorkFlowInterface:
        from java.util.HashMap import HashMap
        from org.allbinary.business.DynamicObjectData import DynamicObjectData
        from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            className: str = hashMap.get(DynamicObjectData.NAME)
            params: list[object] = [None] * (1)
            classes: list[type] = [None] * (1)
            classes[0] = type(hashMap)
            params[0] = hashMap
            anyType: object = AbeFactory.getInstance().getInstance(abeClientInformation, className, classes, params)
            return WorkFlowWrapper(anyType)
        except LicensingException as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "getInstance(HashMap)", e)
            raise e
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "getInstance(HashMap)", e)
            raise e

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.business.DynamicObjectData import DynamicObjectData
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _DbWorkFlowFactory_instance() -> object:
    return DbWorkFlowFactory()

lazy_static(DbWorkFlowFactory, "instance", _DbWorkFlowFactory_instance)


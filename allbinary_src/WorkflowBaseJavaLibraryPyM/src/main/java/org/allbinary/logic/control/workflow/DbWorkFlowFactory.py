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



class DbWorkFlowFactory:
    instance: DbWorkFlowFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> DbWorkFlowFactory:
        return DbWorkFlowFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception, LicensingException
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, abeClientInformation: AbeClientInformationInterface, hashMap: dict) -> WorkFlowInterface:
        from org.allbinary.logic.control.workflow.WorkFlowWrapper import WorkFlowWrapper
        try:
            className: str = hashMap.get(DynamicObjectData.NAME)
            params: list[object] = [None] * (1)
            classes: list[type] = [None] * (1)
            classes[0] = type(hashMap)
            params[0] = hashMap
            anyType: object = AbeFactory.getInstance().getInstance(abeClientInformation, className, classes, params)
            return WorkFlowWrapper(anyType)
        except LicensingException as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "getInstance(HashMap)", e)
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "getInstance(HashMap)", e)
            raise e
# from java.util.HashMap import HashMap
from org.allbinary.business.DynamicObjectData import DynamicObjectData
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.loader.AbeFactory import AbeFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from org.allbinary.string.CommonStrings import CommonStrings


DbWorkFlowFactory.instance = DbWorkFlowFactory()


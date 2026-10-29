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
# package views

from __future__ import annotations



#Replace when validation node is added
class ValidationOnlyTempUtil:
    instance: ValidationOnlyTempUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ValidationOnlyTempUtil:
        return ValidationOnlyTempUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def view(self, validationComponentInterface: ValidationComponentInterface) -> str:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("View Name: " + validationComponentInterface.getTransformInfoInterface().getName(), self, "view()")
            return StringUtil.getInstance().EMPTY_STRING
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, "view()", e)
            raise e
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


ValidationOnlyTempUtil.instance = ValidationOnlyTempUtil()


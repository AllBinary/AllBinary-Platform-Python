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

from java.lang.JavaRuntimeStatic import lazy_static


#Replace when validation node is added
class ValidationOnlyTempUtil:
    instance: ValidationOnlyTempUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ValidationOnlyTempUtil:
        return ValidationOnlyTempUtil.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    def view(self, validationComponentInterface: ValidationComponentInterface) -> str:
        from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("View Name: " + validationComponentInterface.getTransformInfoInterface().getName(), self, "view()")
            return StringUtil.getInstance().EMPTY_STRING
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, "view()", e)
            raise e
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _ValidationOnlyTempUtil_instance() -> object:
    return ValidationOnlyTempUtil()

lazy_static(ValidationOnlyTempUtil, "instance", _ValidationOnlyTempUtil_instance)


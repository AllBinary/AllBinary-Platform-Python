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
# package taghelpers

from __future__ import annotations



class OrderHistoryHelperFactory:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws LicensingException
    def getInstance(self, hashMap: dict, pageContext: PageContext) -> object:
        from taghelpers.OrderHistoryHelper import OrderHistoryHelper
        try:
            return OrderHistoryHelper(hashMap, pageContext)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return None
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from org.allbinary.string.CommonStrings import CommonStrings



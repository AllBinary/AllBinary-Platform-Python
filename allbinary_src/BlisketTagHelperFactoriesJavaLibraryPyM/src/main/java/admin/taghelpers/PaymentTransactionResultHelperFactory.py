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

from admin.taghelpers.TagHelperFactory import TagHelperFactory


class PaymentTransactionResultHelperFactory(TagHelperFactory):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws LicensingException
    def getInstance(self, hashMap: HashMap, pageContext: PageContext) -> object:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return PaymentTransactionResultHelper(hashMap, pageContext)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.GET_INSTANCE, e)
            return None
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



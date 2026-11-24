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
# package views.admin.inventory.listings

from __future__ import annotations



class InventoryViewFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws LicensingException
    @staticmethod
    def getInstance(searchRequest: SearchRequest) -> InventoryViewSearchInterface:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.control.search.SearchRequest import SearchRequest
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.string.CommonStrings import CommonStrings
        from views.generic.inventory.InventorySearch import InventorySearch
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            return InventorySearch(searchRequest)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, "InventoryViewFactory", "getInstance(SearchRequest)", e)
            return None
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.search.SearchRequest import SearchRequest
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.string.CommonStrings import CommonStrings
# from views.generic.inventory.InventorySearch import InventorySearch
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



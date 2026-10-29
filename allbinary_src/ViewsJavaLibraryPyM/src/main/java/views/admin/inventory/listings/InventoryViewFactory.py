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
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            return InventorySearch(searchRequest)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, "InventoryViewFactory", "getInstance(SearchRequest)", e)
            return None
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.search.SearchRequest import SearchRequest
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from org.allbinary.string.CommonStrings import CommonStrings
from views.generic.inventory.InventorySearch import InventorySearch



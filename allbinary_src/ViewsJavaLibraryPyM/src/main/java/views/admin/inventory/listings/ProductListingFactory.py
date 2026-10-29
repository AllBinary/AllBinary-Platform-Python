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



class ProductListingFactory:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance(searchRequest: SearchRequest) -> ProductListingInterface:
        from views.admin.inventory.listings.ProductListing import ProductListing
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            return ProductListing(searchRequest)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().FACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, "ProductListingFactory", commonStrings.GET_INSTANCE, e)
            return None
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.search.SearchRequest import SearchRequest
from org.allbinary.string.CommonStrings import CommonStrings



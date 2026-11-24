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
# package org.allbinary.business.advertisement.search

from __future__ import annotations



# Java interface
class AdvertisementSearchInterface:
    

    def getWebSite(self) -> AdvertisementWebsiteInterface:
        from org.allbinary.business.advertisement.search.website.AdvertisementWebsiteInterface import AdvertisementWebsiteInterface
        raise NotImplementedError()
    

    def getCategory(self) -> AdvertisementCategoryInterface:
        from org.allbinary.business.advertisement.search.category.AdvertisementCategoryInterface import AdvertisementCategoryInterface
        raise NotImplementedError()
    

    def getSizeConstraints(self) -> TwoDimensionalConstraintInterface:
        from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface
        raise NotImplementedError()
    

    def getPricingConstraints(self) -> PriceConstraintInterface:
        from org.allbinary.logic.control.contraints.price.PriceConstraintInterface import PriceConstraintInterface
        raise NotImplementedError()
    

    def getPageNumber(self) -> int:
        raise NotImplementedError()
    

    def getProductsPerPage(self) -> int:
        raise NotImplementedError()
    

    def getSearchParams(self) -> HashMap:
        from java.util.HashMap import HashMap
        raise NotImplementedError()
    

    def setCategory(self, advertisementCategoryInterface: AdvertisementCategoryInterface) -> None:
        from org.allbinary.business.advertisement.search.category.AdvertisementCategoryInterface import AdvertisementCategoryInterface
        raise NotImplementedError()
    

    def setSizeConstraints(self, twoDimensionConstraintsInterface: TwoDimensionalConstraintInterface) -> None:
        from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface
        raise NotImplementedError()
    

    def setPricingConstraints(self, priceConstraintInterface: PriceConstraintInterface) -> None:
        from org.allbinary.logic.control.contraints.price.PriceConstraintInterface import PriceConstraintInterface
        raise NotImplementedError()
    

    def setPageNumber(self, pageNumber: int) -> None:
        raise NotImplementedError()
    

    def setProductsPerPage(self, productsPerPage: int) -> None:
        raise NotImplementedError()
    

    def setSearchParams(self, columnAndKeywordHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        raise NotImplementedError()
# from java.util.HashMap import HashMap
# from org.allbinary.business.advertisement.search.category.AdvertisementCategoryInterface import AdvertisementCategoryInterface
# from org.allbinary.business.advertisement.search.website.AdvertisementWebsiteInterface import AdvertisementWebsiteInterface
# from org.allbinary.logic.control.contraints.price.PriceConstraintInterface import PriceConstraintInterface
# from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface



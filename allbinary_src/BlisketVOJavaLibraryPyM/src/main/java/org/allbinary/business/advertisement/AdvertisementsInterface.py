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
# package org.allbinary.business.advertisement

from __future__ import annotations



# Java interface
class AdvertisementsInterface:
    

    def add(self, advertisementInterface: AdvertisementInterface) -> None:
        raise NotImplementedError()
    

    def get(self, index: int) -> AdvertisementInterface:
        raise NotImplementedError()
    

    def getCurrentPageNum(self) -> int:
        raise NotImplementedError()
    

    def getErrorDescription(self) -> str:
        raise NotImplementedError()
    

    def getErrorNum(self) -> str:
        raise NotImplementedError()
    

    def getNumberOfPosters(self) -> int:
        raise NotImplementedError()
    

    def getNumberOfProductsInPage(self) -> int:
        raise NotImplementedError()
    

    def getStatusCode(self) -> int:
        raise NotImplementedError()
    

    def getTotalNumberOfProducts(self) -> int:
        raise NotImplementedError()
    

    def isSearchValid(self) -> bool:
        raise NotImplementedError()
    

    def setCurrentPageNum(self, currentPageNum: int) -> None:
        raise NotImplementedError()
    

    def setErrorDescription(self, errorDescription: str) -> None:
        raise NotImplementedError()
    

    def setErrorNum(self, errorNum: str) -> None:
        raise NotImplementedError()
    

    def setNumberOfProductsInPage(self, numberOfProductsInPage: int) -> None:
        raise NotImplementedError()
    

    def setStatusCode(self, statusCode: int) -> None:
        raise NotImplementedError()
    

    def setTotalNumberOfProducts(self, totalNumberOfProducts: int) -> None:
        raise NotImplementedError()
    

    def toString(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.toString()



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
# package org.allbinary.business.user.commerce.inventory.item

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface


# Java interface
class ItemInterface(TableMappingInterface):
    

    def setId(self, itemId: str) -> None:
        raise NotImplementedError()
    

    def setNumber(self, number: str) -> None:
        raise NotImplementedError()
    

    def setInBaskets(self, value: str) -> None:
        raise NotImplementedError()
    

    def setWeight(self, value: str) -> None:
        raise NotImplementedError()
    

    def setEnabled(self, value: str) -> None:
        raise NotImplementedError()
    

    def setNewOrUsed(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSummary(self, value: str) -> None:
        raise NotImplementedError()
    

    def setDistributor(self, value: str) -> None:
        raise NotImplementedError()
    

    def setIdUsedByDistributor(self, value: str) -> None:
        raise NotImplementedError()
    

    def setProducedBy(self, value: str) -> None:
        raise NotImplementedError()
    

    def setProductionDate(self, value: str) -> None:
        raise NotImplementedError()
    

    def setStartProductionDate(self, value: str) -> None:
        raise NotImplementedError()
    

    def setDescription(self, value: str) -> None:
        raise NotImplementedError()
    

    def setKeywords(self, value: str) -> None:
        raise NotImplementedError()
    

    def setCategory(self, value: str) -> None:
        raise NotImplementedError()
    

    def setType(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSmallImage(self, value: str) -> None:
        raise NotImplementedError()
    

    def setMediumImage(self, value: str) -> None:
        raise NotImplementedError()
    

    def setLargeImage(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTimeEntered(self, value: str) -> None:
        raise NotImplementedError()
    

    def setLastModified(self, value: str) -> None:
        raise NotImplementedError()
    

    def setPrice(self, value: Money) -> None:
        raise NotImplementedError()
    

    def setComment(self, value: str) -> None:
        raise NotImplementedError()
    

    def setCustoms(self, value: str) -> None:
        raise NotImplementedError()
    

    def setDownloads(self, value: str) -> None:
        raise NotImplementedError()
    

    def setGroups(self, value: str) -> None:
        raise NotImplementedError()
    

    def setOptions(self, value: str) -> None:
        raise NotImplementedError()
    

    def setPermissions(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSpecials(self, value: str) -> None:
        raise NotImplementedError()
    

    def getId(self) -> str:
        raise NotImplementedError()
    

    def getNumber(self) -> str:
        raise NotImplementedError()
    

    def getInBaskets(self) -> str:
        raise NotImplementedError()
    

    def getWeight(self) -> str:
        raise NotImplementedError()
    

    def getEnabled(self) -> str:
        raise NotImplementedError()
    

    def getNewOrUsed(self) -> str:
        raise NotImplementedError()
    

    def getSummary(self) -> str:
        raise NotImplementedError()
    

    def getDistributor(self) -> str:
        raise NotImplementedError()
    

    def getIdUsedByDistributor(self) -> str:
        raise NotImplementedError()
    

    def getProducedBy(self) -> str:
        raise NotImplementedError()
    

    def getProductionDate(self) -> str:
        raise NotImplementedError()
    

    def getStartProductionDate(self) -> str:
        raise NotImplementedError()
    

    def getDescription(self) -> str:
        raise NotImplementedError()
    

    def getKeywords(self) -> str:
        raise NotImplementedError()
    

    def getCategory(self) -> str:
        raise NotImplementedError()
    

    def getType(self) -> str:
        raise NotImplementedError()
    

    def getSmallImage(self) -> str:
        raise NotImplementedError()
    

    def getMediumImage(self) -> str:
        raise NotImplementedError()
    

    def getLargeImage(self) -> str:
        raise NotImplementedError()
    

    def getTimeEntered(self) -> str:
        raise NotImplementedError()
    

    def getLastModified(self) -> str:
        raise NotImplementedError()
    

    def getPrice(self) -> Money:
        raise NotImplementedError()
    

    def getComment(self) -> str:
        raise NotImplementedError()
    

    def getCustoms(self) -> str:
        raise NotImplementedError()
    

    def getDownloads(self) -> str:
        raise NotImplementedError()
    

    def getGroups(self) -> str:
        raise NotImplementedError()
    

    def getOptions(self) -> str:
        raise NotImplementedError()
    

    def getPermissions(self) -> str:
        raise NotImplementedError()
    

    def getSpecials(self) -> str:
        raise NotImplementedError()
    

    def getTotal(self) -> Money:
        raise NotImplementedError()
from org.allbinary.business.user.commerce.money.Money import Money



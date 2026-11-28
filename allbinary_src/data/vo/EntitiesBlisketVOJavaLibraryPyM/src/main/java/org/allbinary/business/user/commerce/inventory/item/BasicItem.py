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

from java.lang.JavaRuntimeStatic import java_predicate
import datetime
from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface


class BasicItem(ItemInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        if "itemId" not in vars(self): self.itemId: str = None
        if "number" not in vars(self): self.number: str = None
        if "inBaskets" not in vars(self): self.inBaskets: str = None
        if "weight" not in vars(self): self.weight: str = None
        if "enabled" not in vars(self): self.enabled: str = None
        if "newOrUsed" not in vars(self): self.newOrUsed: str = None
        if "summary" not in vars(self): self.summary: str = None
        if "distributor" not in vars(self): self.distributor: str = None
        if "idUsedByDistributor" not in vars(self): self.idUsedByDistributor: str = None
        if "producedBy" not in vars(self): self.producedBy: str = None
        if "productionDate" not in vars(self): self.productionDate: str = None
        if "startProductionDate" not in vars(self): self.startProductionDate: str = None
        if "description" not in vars(self): self.description: str = None
        if "keywords" not in vars(self): self.keywords: str = None
        if "category" not in vars(self): self.category: str = None
        if "type_" not in vars(self): self.type_: str = None
        if "smallImage" not in vars(self): self.smallImage: str = None
        if "mediumImage" not in vars(self): self.mediumImage: str = None
        if "largeImage" not in vars(self): self.largeImage: str = None
        if "price" not in vars(self): self.price: Money = None
        if "comment" not in vars(self): self.comment: str = None
        if "customs" not in vars(self): self.customs: str = None
        if "downloads" not in vars(self): self.downloads: str = None
        if "groups" not in vars(self): self.groups: str = None
        if "options" not in vars(self): self.options: str = None
        if "permissions" not in vars(self): self.permissions: str = None
        if "specials" not in vars(self): self.specials: str = None
        if "downloadable" not in vars(self): self.downloadable: bool = False
        if "timeEntered" not in vars(self): self.timeEntered: str = None
        if "lastModified" not in vars(self): self.lastModified: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 0:
            __class__._constructor0(self, *args)
    

    def _constructor1(self, itemHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.commerce.money.Money import Money
        from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGING):
            self.logUtil.putF(self.commonStrings.START, self, "Constructor(HashMap)")
        self.itemId = itemHashMap.get(self.basicItemData.ID)
        self.number = itemHashMap.get(self.basicItemData.NUMBER)
        self.inBaskets = itemHashMap.get(self.basicItemData.INBASKETS)
        self.weight = itemHashMap.get(self.basicItemData.WEIGHT)
        self.enabled = itemHashMap.get(EntryData.getInstance().ENABLE)
        self.newOrUsed = itemHashMap.get(self.basicItemData.NEWORUSED)
        self.summary = itemHashMap.get(self.basicItemData.SUMMARY)
        self.distributor = itemHashMap.get(self.basicItemData.DISTRIBUTOR)
        self.idUsedByDistributor = itemHashMap.get(self.basicItemData.IDUSEDBYDISTRIBUTOR)
        self.producedBy = itemHashMap.get(self.basicItemData.PRODUCEDBY)
        self.productionDate = itemHashMap.get(self.basicItemData.PRODUCTIONDATE)
        self.startProductionDate = itemHashMap.get(self.basicItemData.STARTPRODUCTIONDATE)
        self.description = itemHashMap.get(self.basicItemData.DESCRIPTION)
        self.keywords = itemHashMap.get(self.basicItemData.KEYWORDS)
        self.category = itemHashMap.get(self.basicItemData.CATEGORY)
        self.type_ = itemHashMap.get(self.basicItemData.TYPE)
        self.smallImage = itemHashMap.get(self.basicItemData.SMALLIMAGE)
        self.mediumImage = itemHashMap.get(self.basicItemData.MEDIUMIMAGE)
        self.largeImage = itemHashMap.get(self.basicItemData.LARGEIMAGE)
        self.timeEntered = itemHashMap.get(EntryData.getInstance().TIMECREATED)
        self.lastModified = itemHashMap.get(EntryData.getInstance().LASTMODIFIED)
        self.price = Money(itemHashMap.get(self.basicItemData.PRICE))
        self.comment = itemHashMap.get(self.basicItemData.COMMENT)
        self.customs = itemHashMap.get(self.basicItemData.CUSTOMS)
        self.setDownloads(itemHashMap.get(self.basicItemData.DOWNLOADS))
        self.groups = itemHashMap.get(self.basicItemData.GROUPS)
        self.options = itemHashMap.get(self.basicItemData.OPTIONS)
        self.permissions = itemHashMap.get(self.basicItemData.PERMISSIONS)
        self.specials = itemHashMap.get(self.basicItemData.SPECIALS)
    

    def _constructor0(self) -> None:
        from org.allbinary.business.user.commerce.money.Money import Money
        from org.allbinary.data.generator.ProductIdGenerator import ProductIdGenerator
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGING):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
        EMPTY: str = StringUtil.getInstance().EMPTY_STRING
        self.itemId = ProductIdGenerator().getNext()
        self.number = CommonPhoneStrings.getInstance().ZERO
        self.inBaskets = EMPTY
        self.weight = EMPTY
        self.enabled = EMPTY
        self.newOrUsed = EMPTY
        self.summary = EMPTY
        self.distributor = EMPTY
        self.idUsedByDistributor = EMPTY
        self.producedBy = EMPTY
        self.productionDate = EMPTY
        self.startProductionDate = EMPTY
        self.description = EMPTY
        self.keywords = EMPTY
        self.category = EMPTY
        self.type_ = EMPTY
        self.smallImage = EMPTY
        self.mediumImage = EMPTY
        self.largeImage = EMPTY
        self.timeEntered = EMPTY
        self.lastModified = EMPTY
        self.price = Money()
        self.comment = EMPTY
        self.customs = EMPTY
        self.setDownloads(EMPTY)
        self.groups = EMPTY
        self.options = EMPTY
        self.permissions = EMPTY
        self.specials = EMPTY
    

    def setId(self, itemId: str) -> None:
        self.itemId = itemId
    

    def setNumber(self, number: str) -> None:
        self.number = number
    

    def setInBaskets(self, value: str) -> None:
        self.inBaskets = value
    

    def setWeight(self, value: str) -> None:
        self.weight = value
    

    def setNewOrUsed(self, value: str) -> None:
        self.newOrUsed = value
    

    def setSummary(self, value: str) -> None:
        self.summary = value
    

    def setDistributor(self, value: str) -> None:
        self.distributor = value
    

    def setIdUsedByDistributor(self, value: str) -> None:
        self.idUsedByDistributor = value
    

    def setProducedBy(self, value: str) -> None:
        self.producedBy = value
    

    def setProductionDate(self, value: str) -> None:
        self.productionDate = value
    

    def setStartProductionDate(self, value: str) -> None:
        self.startProductionDate = value
    

    def setDescription(self, value: str) -> None:
        self.description = value
    

    def setKeywords(self, value: str) -> None:
        self.keywords = value
    

    def setCategory(self, value: str) -> None:
        self.category = value
    

    def setType(self, value: str) -> None:
        self.type_ = value
    

    def setSmallImage(self, value: str) -> None:
        self.smallImage = value
    

    def setMediumImage(self, value: str) -> None:
        self.mediumImage = value
    

    def setLargeImage(self, value: str) -> None:
        self.largeImage = value
    

    def setTimeEntered(self, value: str) -> None:
        self.timeEntered = value
    

    def setLastModified(self, value: str) -> None:
        self.lastModified = value
    

    def setPrice(self, value: Money) -> None:
        from org.allbinary.business.user.commerce.money.Money import Money
        self.price = value
    

    def setComment(self, value: str) -> None:
        self.comment = value
    

    def setCustoms(self, value: str) -> None:
        self.customs = value
    

    def setDownloads(self, value: str) -> None:
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        self.downloads = value
        if not (StringValidationUtil.getInstance().isEmpty(self.downloads)):
            downloadInteger: int = str(self.downloads)
            if int(downloadInteger) != 0:
                self.setDownloadable(True)
    

    def setGroups(self, value: str) -> None:
        self.groups = value
    

    def setOptions(self, value: str) -> None:
        self.options = value
    

    def setPermissions(self, value: str) -> None:
        self.permissions = value
    

    def setSpecials(self, value: str) -> None:
        self.specials = value
    

    def setEnabled(self, value: str) -> None:
        self.enabled = value
    

    def getId(self) -> str:
        return self.itemId
    

    def getNumber(self) -> str:
        return self.number
    

    def getInBaskets(self) -> str:
        return self.inBaskets
    

    def getWeight(self) -> str:
        return self.weight
    

    def getNewOrUsed(self) -> str:
        return self.newOrUsed
    

    def getSummary(self) -> str:
        return self.summary
    

    def getDistributor(self) -> str:
        return self.distributor
    

    def getIdUsedByDistributor(self) -> str:
        return self.idUsedByDistributor
    

    def getProducedBy(self) -> str:
        return self.producedBy
    

    def getProductionDate(self) -> str:
        return self.productionDate
    

    def getStartProductionDate(self) -> str:
        return self.startProductionDate
    

    def getDescription(self) -> str:
        return self.description
    

    def getKeywords(self) -> str:
        return self.keywords
    

    def getCategory(self) -> str:
        return self.category
    

    def getType(self) -> str:
        return self.type_
    

    def getSmallImage(self) -> str:
        return self.smallImage
    

    def getMediumImage(self) -> str:
        return self.mediumImage
    

    def getLargeImage(self) -> str:
        return self.largeImage
    

    def getTimeEntered(self) -> str:
        return self.timeEntered
    

    def getLastModified(self) -> str:
        return self.lastModified
    

    def getPrice(self) -> Money:
        from org.allbinary.business.user.commerce.money.Money import Money
        return self.price
    

    def getComment(self) -> str:
        return self.comment
    

    def getCustoms(self) -> str:
        return self.customs
    

    def getDownloads(self) -> str:
        return self.downloads
    

    def getGroups(self) -> str:
        return self.groups
    

    def getOptions(self) -> str:
        return self.options
    

    def getPermissions(self) -> str:
        return self.permissions
    

    def getSpecials(self) -> str:
        return self.specials
    

    def setDownloadable(self, downloadable: bool) -> None:
        self.downloadable = downloadable
    

    def isDownloadable(self) -> bool:
        return self.downloadable
    

    def getEnabled(self) -> str:
        return self.enabled
    

    def getTotal(self) -> Money:
        from org.allbinary.business.user.commerce.money.Money import Money
        itemTotal: Money = Money(self.price)
        itemTotal.multiply(int(int(self.number)))
        return itemTotal
    

    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGING):
            self.logUtil.putF(self.commonStrings.START, self, "toHashMap")
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.put(self.basicItemData.ID, self.itemId)
        hashMap.put(self.basicItemData.NUMBER, self.number)
        hashMap.put(self.basicItemData.INBASKETS, self.inBaskets)
        hashMap.put(self.basicItemData.WEIGHT, self.weight)
        hashMap.put(EntryData.getInstance().ENABLE, self.enabled)
        hashMap.put(self.basicItemData.NEWORUSED, self.newOrUsed)
        hashMap.put(self.basicItemData.SUMMARY, self.summary)
        hashMap.put(self.basicItemData.DISTRIBUTOR, self.distributor)
        hashMap.put(self.basicItemData.IDUSEDBYDISTRIBUTOR, self.idUsedByDistributor)
        hashMap.put(self.basicItemData.PRODUCEDBY, self.producedBy)
        hashMap.put(self.basicItemData.PRODUCTIONDATE, self.productionDate)
        hashMap.put(self.basicItemData.STARTPRODUCTIONDATE, self.startProductionDate)
        hashMap.put(self.basicItemData.DESCRIPTION, self.description)
        hashMap.put(self.basicItemData.KEYWORDS, self.keywords)
        hashMap.put(self.basicItemData.CATEGORY, self.category)
        hashMap.put(self.basicItemData.TYPE, self.type_)
        hashMap.put(self.basicItemData.SMALLIMAGE, self.smallImage)
        hashMap.put(self.basicItemData.MEDIUMIMAGE, self.mediumImage)
        hashMap.put(self.basicItemData.LARGEIMAGE, self.largeImage)
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(int(calendar.getTimeInMillis()))
        hashMap.put(EntryData.getInstance().LASTMODIFIED, time)
        hashMap.put(self.basicItemData.PRICE, str(self.price))
        hashMap.put(self.basicItemData.COMMENT, self.comment)
        hashMap.put(self.basicItemData.CUSTOMS, self.customs)
        hashMap.put(self.basicItemData.DOWNLOADS, self.getDownloads())
        hashMap.put(self.basicItemData.GROUPS, self.groups)
        hashMap.put(self.basicItemData.OPTIONS, self.options)
        hashMap.put(self.basicItemData.PERMISSIONS, self.permissions)
        hashMap.put(self.basicItemData.SPECIALS, self.specials)
        return hashMap
    

    def toVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGING):
            self.logUtil.putF(self.commonStrings.START, self, "toVector")
        values: BasicArrayList = BasicArrayListD()
        values.add(self.itemId)
        values.add(self.number)
        values.add(self.inBaskets)
        values.add(self.weight)
        values.add(self.enabled)
        values.add(self.newOrUsed)
        values.add(self.summary)
        values.add(self.distributor)
        values.add(self.idUsedByDistributor)
        values.add(self.producedBy)
        values.add(self.productionDate)
        values.add(self.startProductionDate)
        values.add(self.description)
        values.add(self.keywords)
        values.add(self.category)
        values.add(self.type_)
        values.add(self.getSmallImage())
        values.add(self.getMediumImage())
        values.add(self.getLargeImage())
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(int(calendar.getTimeInMillis()))
        values.add(time)
        values.add(time)
        values.add(str(self.price))
        values.add(self.comment)
        values.add(self.customs)
        values.add(self.getDownloads())
        values.add(self.groups)
        values.add(self.options)
        values.add(self.permissions)
        values.add(self.specials)
        return values
    

    # throws Exception
    def getKey(self) -> object:
        return self.getId()
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.user.commerce.money.Money import Money
# from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
# from org.allbinary.data.generator.ProductIdGenerator import ProductIdGenerator
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData



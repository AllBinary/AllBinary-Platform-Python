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

from views.admin.inventory.listings.ProductListingInterface import ProductListingInterface


class ProductListing(ProductListingInterface):

    def _init_fields(self) -> None:
        from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.io.file.directory.Directory import Directory
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.directory: Directory = Directory.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        if "storeFronts" not in vars(self): self.storeFronts: StoreFrontsEntity = None
        if "staticPages" not in vars(self): self.staticPages: StaticPagesEntity = None
        if "inventory" not in vars(self): self.inventory: InventoryEntity = None
        if "searchRequest" not in vars(self): self.searchRequest: SearchRequest = None
        self.INVENTORY: str = ".InventoryView"
    

    def __init__(self, searchRequest: SearchRequest) -> None:
        from org.allbinary.data.tables.context.module.storefronts.StoreFrontsEntity import StoreFrontsEntity
        from org.allbinary.data.tables.staticpages.StaticPagesEntity import StaticPagesEntity
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
        from org.allbinary.logic.control.search.SearchRequest import SearchRequest
        __class__._init_fields(self)
        self.searchRequest = searchRequest
        self.storeFronts = StoreFrontsEntity()
        self.staticPages = StaticPagesEntity()
        self.inventory = InventoryEntity()
    

    # throws Exception
    def getHashSet(self, storeFront: StoreFrontInterface) -> HashSet:
        from java.util.HashSet import HashSet
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.tokens.UniqueTokens import UniqueTokens
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from views.generic.inventory.InventoryColumnUtil import InventoryColumnUtil
        inventoryColumnUtil: InventoryColumnUtil = InventoryColumnUtil.getInstance()
        keywords: BasicArrayList = inventoryColumnUtil.getColumnWhereLike(self.inventory, storeFront.getCategoryPath(), self.basicItemData.KEYWORDS)
        subStoreVector: BasicArrayList = storeFront.getSubStores()
        size: int = subStoreVector.size()
        for index in range(0, size):
            subStore: str = subStoreVector.get(index)
            substoreKeywords: BasicArrayList = inventoryColumnUtil.getColumnWhereLike(self.inventory, str(AbPathData.getInstance().SEPARATOR) + subStore, self.basicItemData.CATEGORY)
            keywords.addAllList(substoreKeywords)
        uniqueTokens: UniqueTokens = UniqueTokens()
        keywordHashSet: HashSet = uniqueTokens.getWhithoutDashesAndSkipNumberOnlyTokens(keywords)
        return keywordHashSet
    

    # throws Exception
    def savePage(self, file: str, data: str) -> None:
        from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
        from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
        from org.allbinary.logic.io.StreamUtil import StreamUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().STATICPAGEGENERATIONLOGGING):
            self.logUtil.putF("Creating File: " + file, self, "generateAll()")
        newFile: AbFile = AbFile.createAbFile(file)
        if newFile.exists():
            newFile.delete()
        newFile.createNewFile()
        if newFile.exists():
            idOutData: AbDataOutputStream = DataOutputStreamFactory.getInstance().getInstanceForAbFile(newFile)
            idOutData.writeBytes(data)
            idOutData.flush()
            StreamUtil.getInstance().close(idOutData)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().STATICPAGEGENERATIONLOGGING):
                self.logUtil.putF("Wrote Total Bytes: " + str(newFile.length()), self, "generateAll()")
        else:
            raise Exception("Could Not Create: " + file)
    

    # throws Exception
    def create(self, keywordData: str, keywordFilenameHashMap: HashMap, vector: BasicArrayList, staticPath: AbPath) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.control.search.SearchParams import SearchParams
        from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.SpecialCharacterUtil import SpecialCharacterUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.string.regex.replace.Replace import Replace
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
        from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from views.generic.inventory.InventorySearchUtil import InventorySearchUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        hashMap: HashMap = SpecialCharacterUtil.getHashMap()
        hashMap.put(CommonSeps.getInstance().SPACE, StringUtil.getInstance().EMPTY_STRING)
        pageName: str = Replace(hashMap).all(keywordData)
        searchParams: SearchParams = self.searchRequest.getParams()
        searchParams.add(self.basicItemData.KEYWORDS, keywordData)
        searchParams.setStartPage(CommonPhoneStrings.getInstance().ZERO)
        self.searchRequest.setParams(searchParams)
        self.searchRequest.setFileBaseName(pageName)
        abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        inventorySearchUtil: InventorySearchUtil = InventorySearchUtil.getInstance()
        productListingPages: list[str] = inventorySearchUtil.search(abeClientInformation, self.searchRequest, vector)
        for index in range(0, len(productListingPages)):
            if productListingPages[index] is None:
                break
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().STATICPAGEGENERATIONLOGGING):
                self.logUtil.putF("Saving Listing: " + str(index), self, "generateAll()")
            indexStr: str = StringUtil.getInstance().EMPTY_STRING
            if index > 0:
                indexStr = str(int(index))
            keywordFilenameHashMap.put(keywordData, pageName + indexStr)
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(str(staticPath))
            stringBuffer.append(pageName)
            stringBuffer.append(indexStr)
            stringBuffer.append(AbPathData.getInstance().EXTENSION_SEP)
            stringBuffer.append(InputOutputTypeData.getInstance().DEFAULT)
            file: str = str(stringBuffer)
            if not (self.directory.create(staticPath)):
                raise Exception("Could Not Create Directory: " + str(staticPath))
            self.savePage(file, productListingPages[index])
    

    def addStaticPageInfoToDatabase(self, storeFront: StoreFrontInterface, keywordFilenameHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.util.BasicArrayList import BasicArrayList
        keywordHashSet: Set = keywordFilenameHashMap.keySet()
        keywordArray: list[object] = keywordHashSet.toArray()
        size: int = len(keywordArray)
        for index in range(0, size):
            insertVector: BasicArrayList = BasicArrayListD()
            keywordData: str = keywordArray[index]
            fileName: str = keywordFilenameHashMap.get(keywordData)
            insertVector.add(storeFront.getName())
            insertVector.add(keywordData)
            insertVector.add(fileName)
            self.staticPages.insert(insertVector)
    

    # throws Exception
    def generateAll_j0(self) -> str:
        from java.util.HashMap import HashMap
        from java.util.HashSet import HashSet
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from views.generic.inventory.InventorySearchUtil import InventorySearchUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            storeFront: StoreFrontInterface = self.searchRequest.getStoreFront()
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(URLGLOBALS.getWebappPath())
            stringBuffer.append(storeFront.getName())
            stringBuffer.append(AbPathData.getInstance().SEPARATOR)
            stringBuffer.append(storeFront.getStaticPath())
            staticPath: AbPath = AbPath(str(stringBuffer), StringUtil.getInstance().EMPTY_STRING)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().STATICPAGEGENERATIONLOGGING):
                self.logUtil.putF("Store Static Pages Path: " + str(staticPath), self, "generateAll()")
            keywordHashSet: HashSet = self.getHashSet(storeFront)
            keywordArray: list[object] = keywordHashSet.toArray()
            size: int = len(keywordArray)
            keywordFilenameHashMap: HashMap = StdUtil.getInstance().createHashMap()
            if size == 0:
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append("Products For ")
                stringBuffer.append(storeFront.getName())
                stringBuffer.append(" Store Not Found")
                return str(stringBuffer)
            inventorySearchUtil: InventorySearchUtil = InventorySearchUtil.getInstance()
            vector: BasicArrayList = inventorySearchUtil.getBasicItemIdColumn(self.searchRequest)
            for index in range(0, size):
                keywordData: str = keywordArray[index]
                if len(keywordData) > 1:
                    self.create(keywordData, keywordFilenameHashMap, vector, staticPath)
            self.addStaticPageInfoToDatabase(storeFront, keywordFilenameHashMap)
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append("Static Files Generated Successfully For ")
            stringBuffer.append(storeFront.getName())
            stringBuffer.append(" it used packages ")
            stringBuffer.append(storeFront.getPackageLocation())
            stringBuffer.append(self.INVENTORY)
            return str(stringBuffer)
        except Exception as e:
            raise e
    

    # throws Exception
    def generateAll_j1(self, storeName: str) -> str:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.util.BasicArrayList import BasicArrayList
        try:
            stringBuffer: StringMaker = StringMaker()
            if storeName is not None:
                if ((storeName > GLOBALS2.GENERATEALLSTORES) - (storeName < GLOBALS2.GENERATEALLSTORES)) != 0:
                    self.searchRequest.setStoreFront(self.storeFronts.getStoreFrontInterface(storeName))
                    stringBuffer.append(self.generateAll())
                    stringBuffer.append("<br />")
                else:
                    storeFrontVector: BasicArrayList = self.storeFronts.getStoreFrontNames()
                    size: int = storeFrontVector.size()
                    for index in range(0, size):
                        storeName = storeFrontVector.get(index)
                        self.searchRequest.setStoreFront(self.storeFronts.getStoreFrontInterface(storeName))
                        stringBuffer.append(self.generateAll())
                        stringBuffer.append("<br />")
            else:
                return "Generation Failed No Store Specified<br/>"
            stringBuffer.append("All Static Pages Generated<br/>")
            return str(stringBuffer)
        except Exception as e:
            raise e

    def generateAll(self, *args):
        implementation = __class__.__dict__.get("generateAll_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().generateAll(*args)
# from java.util.HashMap import HashMap
# from java.util.HashSet import HashSet
# from java.util.Set import Set
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
# from org.allbinary.data.tables.context.module.storefronts.StoreFrontsEntity import StoreFrontsEntity
# from org.allbinary.data.tables.staticpages.StaticPagesEntity import StaticPagesEntity
# from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
# from org.allbinary.globals.GLOBALS2 import GLOBALS2
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.search.SearchParams import SearchParams
# from org.allbinary.logic.control.search.SearchRequest import SearchRequest
# from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
# from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
# from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
# from org.allbinary.logic.io.StreamUtil import StreamUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.directory.Directory import Directory
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.string.SpecialCharacterUtil import SpecialCharacterUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.regex.replace.Replace import Replace
# from org.allbinary.logic.string.tokens.UniqueTokens import UniqueTokens
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
# from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from views.generic.inventory.InventoryColumnUtil import InventoryColumnUtil
# from views.generic.inventory.InventorySearchUtil import InventorySearchUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



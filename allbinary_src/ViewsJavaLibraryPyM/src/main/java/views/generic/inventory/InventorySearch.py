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
# package views.generic.inventory

from __future__ import annotations

from views.admin.inventory.listings.InventoryViewSearchInterface import InventoryViewSearchInterface


class InventorySearch(InventoryViewSearchInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        self.searchRequest: SearchRequest = None
    

    def __init__(self, searchRequest: SearchRequest) -> None:
        super().__init__()
        self._init_fields()
        self.searchRequest = searchRequest
    

    # throws Exception
    def searchSingleStaticPage(self) -> str:
        try:
            storeFront: StoreFrontInterface = self.searchRequest.getStoreFront()
            searchParams: SearchParams = self.searchRequest.getParams()
            columnValueHashMap: dict = searchParams.get()
            file: str = StaticPagesEntity().getFile(storeFront.getName(), Replace("-", CommonSeps.getInstance().SPACE).all(columnValueHashMap.get(self.basicItemData.KEYWORDS)))
            if StringValidationUtil.getInstance().isEmpty(file):
                return None
            else:
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append(storeFront.getCurrentHostName())
                stringBuffer.append(storeFront.getCurrentHostNamePath())
                stringBuffer.append(storeFront.getStaticPath())
                stringBuffer.append(file)
                stringBuffer.append(self.searchRequest.getParams().getEndPage())
                stringBuffer.append(AbPathData.getInstance().EXTENSION_SEP)
                stringBuffer.append(InputOutputTypeData.getInstance().DEFAULT)
                filePath: str = Replace(CommonSeps.getInstance().SPACE, "%20").all(str(stringBuffer))
                return filePath
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "searchSingleStaticPage", e)
            raise Exception("Failed retrieve Single Product Page Static")
    

    # throws Exception
    def searchSingleDynamicPage(self) -> str:
        try:
            str_: list[str] = self.search()
            return str_[int(self.searchRequest.getParams().getStartPageInt())]
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "searchSingleDynamicPage", e)
            raise Exception("Failed retrieve Single Product Page Dynamically")
    

    # throws Exception
    def search(self) -> list[str]:
        from views.generic.inventory.InventorySearchUtil import InventorySearchUtil
        abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        inventorySearchUtil: InventorySearchUtil = InventorySearchUtil.getInstance()
        vector: BasicArrayList = inventorySearchUtil.getBasicItemIdColumn(self.searchRequest)
        return inventorySearchUtil.search(abeClientInformation, self.searchRequest, vector)
    

    # throws Exception
    def getProduct(self, product: str) -> str:
        from views.generic.inventory.InventorySearchProductUtil import InventorySearchProductUtil
        abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        return InventorySearchProductUtil.getInstance().getProduct(abeClientInformation, self.searchRequest, product)
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.data.tables.staticpages.StaticPagesEntity import StaticPagesEntity
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.search.SearchParams import SearchParams
from org.allbinary.logic.control.search.SearchRequest import SearchRequest
from org.allbinary.logic.io.InputOutputTypeData import InputOutputTypeData
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.string.regex.replace.Replace import Replace
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings



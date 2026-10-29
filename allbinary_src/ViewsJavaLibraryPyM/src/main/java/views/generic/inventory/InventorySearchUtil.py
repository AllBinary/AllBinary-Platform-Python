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



class InventorySearchUtil:
    instance: InventorySearchUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonPhoneStrings: CommonPhoneStrings = CommonPhoneStrings.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> InventorySearchUtil:
        return InventorySearchUtil.instance
    

    # throws Exception
    def getBasicItemIdColumn(self, searchRequest: SearchRequest) -> BasicArrayList:
        from views.generic.inventory.InventoryColumnUtil import InventoryColumnUtil
        inventoryEntityInterface: InventoryEntity = InventoryEntityFactory.getInstance().getInventoryEntityInstance()
        storeFrontInterface: StoreFrontInterface = searchRequest.getStoreFront()
        inventorySearchUtil: InventoryColumnUtil = InventoryColumnUtil.getInstance()
        column: BasicArrayList = inventorySearchUtil.getColumnWhereLike(inventoryEntityInterface, storeFrontInterface.getCategoryPath(), self.basicItemData.ID)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGING):
            self.logUtil.putF("Number Of Items Found: " + str(column.size()), self, "search")
        subStoreVector: BasicArrayList = storeFrontInterface.getSubStores()
        size: int = subStoreVector.size()
        for index in range(0, size):
            subStore: str = subStoreVector.get(index)
            substoreIdColumn: BasicArrayList = inventorySearchUtil.getColumnWhereLike(inventoryEntityInterface, subStore, self.basicItemData.ID)
            column.addAllList(substoreIdColumn)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGING):
            self.logUtil.putF("Number Of Items Found Including SubStores: " + str(column.size()), self, "search")
        return column
    

    # throws Exception
    def getNoResults(self, viewDocumentInterface: TransformDocumentInterface, inventoryNode: Node) -> str:
        inventoryNode.appendChild(ModDomHelper.createNameValueNodes(viewDocumentInterface.getDoc(), SearchData.TOTAL_NUMBER_PAGES, self.commonPhoneStrings.ZERO))
        inventoryNode.appendChild(ModDomHelper.createNameValueNodes(viewDocumentInterface.getDoc(), SearchData.TOTAL_NUMBER_ITEMS, self.commonPhoneStrings.ZERO))
        success: str = XmlDocumentHelper.toString(viewDocumentInterface.getDoc())
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGING):
            self.logUtil.putF("No Results Xml: " + success, self, "search")
        return success
    

    def search(self, abeClientInformation: AbeClientInformationInterface, searchRequest: SearchRequest, column: BasicArrayList) -> list[str]:
        try:
            inventoryEntityInterface: InventoryEntity = InventoryEntityFactory.getInstance().getInventoryEntityInstance()
            searchParams: SearchParams = searchRequest.getParams()
            startPage: int = int(searchParams.getStartPageInt())
            endPage: int = int(searchParams.getEndPageInt())
            pageLength: int = int(searchParams.getLengthInt())
            savedPagesInRange: int = 0
            columnValueHashMap: dict = searchParams.get()
            keyword: str = Replace("-", CommonSeps.getInstance().SPACE).all(columnValueHashMap.get(self.basicItemData.KEYWORDS))
            if StringValidationUtil.getInstance().isEmpty(keyword):
                return None
            stringBuffer: StringMaker = StringMaker()
            if startPage >= 0:
                if pageLength == 0:
                    pageLength = SearchData.DEFAULT_PAGE_LENGTH
                MAXPAGES: int = 100
                productListingPages: list[str] = [None] * (MAXPAGES)
                documents: list[Document] = [None] * (MAXPAGES)
                inventoryNodes: list[Node] = [None] * (MAXPAGES)
                keyword = keyword.upper()
                lastPage: int = -1
                numberOfResultsOnCurrentPage: int = 0
                numberOfResults: int = 0
                viewDocumentInterface: TransformDocumentInterface = TransformStoreDocumentFactory.getInstance(searchRequest)
                inventoryNode: Node = viewDocumentInterface.getDoc().createElement(InventoryData.INVENTORY)
                viewDocumentInterface.getBaseNode().appendChild(inventoryNode)
                inventoryNode.appendChild(ModDomHelper.createNameValueNodes(viewDocumentInterface.getDoc(), SearchData.PAGE, str(int(startPage))))
                if searchRequest.getFileBaseName() is not None:
                    inventoryNode.appendChild(searchRequest.getFileBaseNameNode(viewDocumentInterface.getDoc()))
                currentPage: int = -1
                size: int = column.size()
                for index in range(0, size):
                    product: str = str(column.get(index))
                    itemInterface: ItemInterface = inventoryEntityInterface.getItem(product)
                    keywords: str = itemInterface.getKeywords()
                    keywords = keywords.upper()
                    if keywords.find(keyword) != -1:
                        if currentPage + 1 >= startPage and currentPage + 1 <= endPage:
                            itemNode: Node = BasicItemView(itemInterface, BasicArrayListD()).toXmlNode(viewDocumentInterface.getDoc())
                            itemNode.appendChild(ModDomHelper.createNameValueNodes(viewDocumentInterface.getDoc(), BasketData.ITEMTOTALINBASKET, self.commonPhoneStrings.ONE))
                            inventoryNode.appendChild(itemNode.cloneNode(True))
                        currentPage = (int((numberOfResults + 1) / pageLength)) - 1
                        numberOfResultsOnCurrentPage += 1
                        if lastPage < currentPage:
                            if currentPage >= startPage and currentPage <= endPage:
                                inventoryNode.appendChild(ModDomHelper.createNameValueNodes(viewDocumentInterface.getDoc(), SearchData.TOTAL_NUMBER_ITEMS_ON_THIS_PAGE, str(int(numberOfResultsOnCurrentPage))))
                                documents[currentPage] = viewDocumentInterface.getDoc()
                                inventoryNodes[currentPage] = inventoryNode
                                savedPagesInRange += 1
                                viewDocumentInterface = TransformStoreDocumentFactory.getInstance(searchRequest)
                                inventoryNode = viewDocumentInterface.getDoc().createElement(InventoryData.INVENTORY)
                                viewDocumentInterface.getBaseNode().appendChild(inventoryNode)
                                inventoryNode.appendChild(ModDomHelper.createNameValueNodes(viewDocumentInterface.getDoc(), SearchData.PAGE, str(int(currentPage + 1))))
                                if searchRequest.getFileBaseName() is not None:
                                    inventoryNode.appendChild(searchRequest.getFileBaseNameNode(viewDocumentInterface.getDoc()))
                            lastPage = currentPage
                            numberOfResultsOnCurrentPage = 0
                        numberOfResults += 1
                        if lastPage >= MAXPAGES - 1:
                            break
                if numberOfResultsOnCurrentPage > 0 and (currentPage + 1 >= startPage and currentPage + 1 <= endPage):
                    inventoryNode.appendChild(ModDomHelper.createNameValueNodes(viewDocumentInterface.getDoc(), SearchData.TOTAL_NUMBER_ITEMS_ON_THIS_PAGE, str(int(numberOfResultsOnCurrentPage - 1))))
                    documents[lastPage + 1] = viewDocumentInterface.getDoc()
                    inventoryNodes[lastPage + 1] = inventoryNode
                    savedPagesInRange += 1
                if numberOfResultsOnCurrentPage > 0:
                    lastPage += 1
                if endPage > MAXPAGES - 1:
                    endPage = MAXPAGES - 1
                for index in range(startPage, endPage + 1):
                    if index <= lastPage:
                        tempDocument: Document = documents[index]
                        inventoryNodes[index].appendChild(ModDomHelper.createNameValueNodes(tempDocument, SearchData.TOTAL_NUMBER_PAGES, str(int(lastPage + 1))))
                        inventoryNodes[index].appendChild(ModDomHelper.createNameValueNodes(tempDocument, SearchData.TOTAL_NUMBER_ITEMS, str(int(numberOfResults))))
                        for pageIndex in range(0, lastPage + 1):
                            stringBuffer.delete(0, stringBuffer.length())
                            stringBuffer.append(searchRequest.getFileBaseName())
                            if stringBuffer.length() > 0:
                                if pageIndex != 0:
                                    stringBuffer.append(str(pageIndex))
                                inventoryNodes[index].appendChild(ModDomHelper.createNameValueNodes(tempDocument, SearchData.PAGE_INFO, str(pageIndex), str(stringBuffer)))
                            else:
                                inventoryNodes[index].appendChild(ModDomHelper.createNameValueNodes(tempDocument, SearchData.PAGE_INFO, str(pageIndex), SearchData.SEARCH))
                        success: str = XmlDocumentHelper.toString(tempDocument)
                        productListingPages[index] = StoreTransformer(abeClientInformation, TransformInfoHttpSearch(searchRequest)).translate(success)
                if savedPagesInRange == 0:
                    result: str = self.getNoResults(viewDocumentInterface, inventoryNode)
                    productListingPages[0] = StoreTransformer(abeClientInformation, TransformInfoHttpSearch(searchRequest)).translate(result)
                return productListingPages
            else:
                return None
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "search", e)
            return None
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.inventory.InventoryData import InventoryData
from org.allbinary.business.user.commerce.inventory.basket.BasketData import BasketData
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.business.user.commerce.inventory.item.BasicItemView import BasicItemView
from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.search.SearchData import SearchData
from org.allbinary.logic.control.search.SearchParams import SearchParams
from org.allbinary.logic.control.search.SearchRequest import SearchRequest
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.string.regex.replace.Replace import Replace
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.StoreTransformer import StoreTransformer
from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
from org.allbinary.logic.visual.transform.data.TransformStoreDocumentFactory import TransformStoreDocumentFactory
from org.allbinary.logic.visual.transform.info.TransformInfoHttpSearch import TransformInfoHttpSearch
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


InventorySearchUtil.instance = InventorySearchUtil()


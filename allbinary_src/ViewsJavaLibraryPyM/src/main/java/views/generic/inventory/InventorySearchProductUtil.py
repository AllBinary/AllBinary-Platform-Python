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

from java.lang.JavaRuntimeStatic import lazy_static


class InventorySearchProductUtil:
    instance: InventorySearchProductUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.ITEM_NOT_FOUND: str = "Item Not Found."

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> InventorySearchProductUtil:
        return InventorySearchProductUtil.instance
    

    # throws Exception
    def getProduct(self, abeClientInformation: AbeClientInformationInterface, searchRequest: SearchRequest, product: str) -> str:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.user.commerce.inventory.item.BasicItemView import BasicItemView
        from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        from org.allbinary.logic.control.search.SearchRequest import SearchRequest
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.StoreTransformer import StoreTransformer
        from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
        from org.allbinary.logic.visual.transform.data.TransformStoreDocumentFactory import TransformStoreDocumentFactory
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpSearch import TransformInfoHttpSearch
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            inventoryEntityInterface: InventoryEntity = InventoryEntityFactory.getInstance().getInventoryEntityInstance()
            itemInterface: ItemInterface = inventoryEntityInterface.getItem(product)
            if itemInterface is not None:
                viewDocumentInterface: TransformDocumentInterface = TransformStoreDocumentFactory.getInstance(searchRequest)
                viewDocumentInterface.getBaseNode().appendChild(BasicItemView(itemInterface, BasicArrayListD()).toXmlNode(viewDocumentInterface.getDoc()))
                success: str = XmlDocumentHelper.toString(viewDocumentInterface.getDoc())
                outputStr: str = StoreTransformer(abeClientInformation, TransformInfoHttpSearch(searchRequest)).translate(success)
                return outputStr
            else:
                return self.ITEM_NOT_FOUND
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "getProduct", e)
            raise Exception("Failed to getProduct")
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.user.commerce.inventory.item.BasicItemView import BasicItemView
# from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
# from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
# from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
# from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.search.SearchRequest import SearchRequest
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.visual.transform.StoreTransformer import StoreTransformer
# from org.allbinary.logic.visual.transform.data.TransformDocumentInterface import TransformDocumentInterface
# from org.allbinary.logic.visual.transform.data.TransformStoreDocumentFactory import TransformStoreDocumentFactory
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpSearch import TransformInfoHttpSearch
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _InventorySearchProductUtil_instance() -> object:
    return InventorySearchProductUtil()

lazy_static(InventorySearchProductUtil, "instance", _InventorySearchProductUtil_instance)


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

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class InventoryView(HttpStoreComponentView, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Starting", self, "toXmlNode")
            inventoryEntityInterface: InventoryEntity = InventoryEntityFactory.getInstance().getInventoryEntityInstance()
            inventoryNode: Node = document.createElement(InventoryData.INVENTORY)
            itemVector: BasicArrayList = inventoryEntityInterface.getItems(StoreFrontFactory.getInstance(self.getTransformInfoInterface().getStoreName()))
            inventoryNode.appendChild(ModDomHelper.createNameValueNodes(document, SearchData.TOTAL_NUMBER_ITEMS_ON_THIS_PAGE, str(int(itemVector.size()))))
            size: int = itemVector.size()
            for index in range(0, size):
                itemInterface: ItemInterface = itemVector.get(index)
                if itemInterface is not None:
                    node: Node = BasicItemView(itemInterface, BasicArrayListD()).toXmlNode(document)
                    inventoryNode.appendChild(node)
                else:
                    self.logUtil.putF("Inventory", self, "toXmlNode")
            return inventoryNode
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            raise e
    

    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self)
    

    def view(self) -> str:
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            error: str = "Failed to view Inventory"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            return error
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.user.commerce.inventory.InventoryData import InventoryData
from org.allbinary.business.user.commerce.inventory.item.BasicItemView import BasicItemView
from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.search.SearchData import SearchData
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



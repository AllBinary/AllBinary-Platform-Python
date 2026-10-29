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
# package views.generic.basket.mini

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class MiniBasketView(HttpStoreComponentView, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        try:
            basketInterface: BasketInterface = self.getWeblisketSession().getOrder().getBasket()
            basketNode: Node = document.createElement(BasketData.BASKET)
            totalNumberNode: Node = document.createElement(SearchData.TOTAL_NUMBER_ITEMS)
            totalNumberTextNode: Node = document.createTextNode(str(basketInterface.getNumberOfItems()))
            totalNumberNode.appendChild(totalNumberTextNode)
            totalWeightNode: Node = document.createElement(BasketData.TOTALWEIGHT)
            totalWeightTextNode: Node = document.createTextNode(str(basketInterface.getTotalWeight()))
            totalWeightNode.appendChild(totalWeightTextNode)
            subTotalNode: Node = document.createElement(BasketData.SUBTOTAL)
            subTotalTextNode: Node = document.createTextNode(str(basketInterface.getSubTotal()))
            subTotalNode.appendChild(subTotalTextNode)
            basketNode.appendChild(totalNumberNode)
            basketNode.appendChild(totalWeightNode)
            basketNode.appendChild(subTotalNode)
            return basketNode
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            raise e
    

    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self)
    

    # throws Exception
    def view(self) -> str:
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
from org.allbinary.business.user.commerce.inventory.basket.BasketData import BasketData
from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.search.SearchData import SearchData
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



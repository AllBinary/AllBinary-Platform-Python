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
# package views.generic.shipping

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class ShippingMethodsView(HttpStoreComponentView, DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.shippingMethods: ShippingMethods = None
        self.storeFrontInterface: StoreFrontInterface = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.storeFrontInterface = StoreFrontFactory.getInstance(self.getTransformInfoInterface().getStoreName())
        self.shippingMethods = ShippingMethods(self.abeClientInformation, self.storeFrontInterface)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        try:
            shippingMethodsNode: Node = document.createElement(ShippingMethodsData.SHIPPINGMETHODSORDERSUMMARIES)
            order: OrderInterface = self.getWeblisketSession().getOrder()
            basket: BasketInterface = self.getWeblisketSession().getOrder().getBasket()
            shippingAddressesEntityInterface: StreetAddressesEntityInterface = ShippingAddressesEntityFactory.getInstance().getInstance(self.getWeblisketSession().getUserName())
            streetAddress: StreetAddress = shippingAddressesEntityInterface.getDefault()
            shippingVector: BasicArrayList = self.shippingMethods.get()
            size: int = shippingVector.size()
            for index in range(0, size):
                shippingMethodNode: Node = document.createElement(ShippingMethodsData.SHIPPINGMETHODORDERSUMMARY)
                shipping: ShippingInterface = shippingVector.get(index)
                shippingView: DomNodeInterface = shipping
                shippingMethodNode.appendChild(shippingView.toXmlNode(document))
                shippingCost: Money = shipping.getCost(order)
                subTotal: Money = basket.getSubTotal()
                taxRate: float = TaxFactory.getInstance().getInstance(self.abeClientInformation, self.storeFrontInterface).getTaxRate(streetAddress, self.storeFrontInterface)
                tax: Money = Money()
                total: Money = Money()
                total.add(str(shippingCost))
                total.add(str(subTotal))
                tax.add(str(total))
                tax.multiply(taxRate)
                total.add(str(tax))
                shippingMethodNode.appendChild(ModDomHelper.createNameValueNodes(document, ShippingMethodsData.SHIPPINGCOST, str(shippingCost)))
                shippingMethodNode.appendChild(ModDomHelper.createNameValueNodes(document, ShippingMethodsData.TAXRATE, str(taxRate)))
                shippingMethodNode.appendChild(ModDomHelper.createNameValueNodes(document, ShippingMethodsData.SUBTOTAL, str(subTotal)))
                shippingMethodNode.appendChild(ModDomHelper.createNameValueNodes(document, ShippingMethodsData.TAX, str(tax)))
                shippingMethodNode.appendChild(ModDomHelper.createNameValueNodes(document, ShippingMethodsData.TOTAL, str(total)))
                shippingMethodNode.appendChild(ModDomHelper.createNameValueNodes(document, EntryData.getInstance().DEFAULT, self.shippingMethods.getDefault().getName()))
                shippingMethodsNode.appendChild(shippingMethodNode)
            return shippingMethodsNode
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().XSLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "toXmlNode", e)
            raise e
    

    def addDomNodeInterfaces(self) -> None:
        self.addDomNodeInterface(self)
    

    def view(self) -> str:
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            error: str = "Failed to view ShippingMethods"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            return error
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.user.address.StreetAddress import StreetAddress
from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface
from org.allbinary.business.user.commerce.money.Money import Money
from org.allbinary.business.user.commerce.money.tax.TaxFactory import TaxFactory
from org.allbinary.business.user.commerce.shipping.ShippingMethods import ShippingMethods
from org.allbinary.business.user.commerce.shipping.ShippingMethodsData import ShippingMethodsData
from org.allbinary.business.user.commerce.shipping.modules.ShippingInterface import ShippingInterface
from org.allbinary.data.tables.user.address.StreetAddressesEntityInterface import StreetAddressesEntityInterface
from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntityFactory import ShippingAddressesEntityFactory
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



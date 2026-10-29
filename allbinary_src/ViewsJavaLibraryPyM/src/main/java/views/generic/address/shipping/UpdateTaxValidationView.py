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
# package views.generic.address.shipping

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.generic.address.shipping.ShippingAddressView import ShippingAddressView


class UpdateTaxValidationView(ShippingAddressView, ValidationComponentInterface):
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
    

    # throws Exception
    def isValid(self) -> bool:
        self.streetAddress = StreetAddress(self.getRequest())
        storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.getTransformInfoInterface().getStoreName())
        if TaxFactory.getInstance().getInstance(self.abeClientInformation, storeFrontInterface).isValid(self.streetAddress, storeFrontInterface) == False:
            return False
        billingAddressesEntity: ShippingAddressesEntity = ShippingAddressesEntity(self.getWeblisketSession().getUserName())
        streetAddressList: BasicArrayList = billingAddressesEntity.get()
        if streetAddressList is None:
            return False
        count: int = 0
        size: int = streetAddressList.size()
        for index in range(0, size):
            aStreetAddress: StreetAddress = streetAddressList.get(index)
            if aStreetAddress.getName().compareTo(ShippingAddressData.TAX) == 0:
                count += 1
        if count != 1:
            return False
        return True
    

    def validationInfo(self) -> str:
        return "Unable to update tax location."
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
from org.allbinary.business.user.address.StreetAddress import StreetAddress
from org.allbinary.business.user.commerce.money.tax.TaxFactory import TaxFactory
from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntity import ShippingAddressesEntity
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



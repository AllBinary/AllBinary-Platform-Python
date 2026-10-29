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


class TaxValidationView(ShippingAddressView, ValidationComponentInterface):
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
    

    def isValid(self) -> bool:
        billingAddressesEntity: ShippingAddressesEntity = ShippingAddressesEntity(self.getWeblisketSession().getUserName())
        streetAddressList: BasicArrayList = billingAddressesEntity.get()
        if streetAddressList is None:
            return False
        size: int = streetAddressList.size()
        for index in range(0, size):
            aStreetAddress: StreetAddress = streetAddressList.get(index)
            if aStreetAddress.getName().compareTo(ShippingAddressData.TAX) == 0:
                self.streetAddress = aStreetAddress
                return True
        return False
    

    def validationInfo(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
from org.allbinary.business.user.address.StreetAddress import StreetAddress
from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntity import ShippingAddressesEntity
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



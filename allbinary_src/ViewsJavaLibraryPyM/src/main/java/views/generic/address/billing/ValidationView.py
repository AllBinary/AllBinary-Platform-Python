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
# package views.generic.address.billing

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.generic.address.billing.BillingAddressesView import BillingAddressesView


class ValidationView(BillingAddressesView, ValidationComponentInterface):
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
    

    def isValid(self) -> bool:
        billingAddressesEntity: BillingAddressesEntity = BillingAddressesEntity(self.getWeblisketSession().getUserName())
        self.streetAddresses = billingAddressesEntity.get()
        if self.streetAddresses is None:
            return False
        if self.streetAddresses.size() < 1:
            return False
        return True
    

    def validationInfo(self) -> str:
        return "No Billing Addresses to display.<br />"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
from org.allbinary.data.tables.user.address.billing.BillingAddressesEntity import BillingAddressesEntity
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



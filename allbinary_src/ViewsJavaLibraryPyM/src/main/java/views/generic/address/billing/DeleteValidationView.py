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
from views.generic.address.billing.BillingAddressView import BillingAddressView


class DeleteValidationView(BillingAddressView, ValidationComponentInterface):

    def _init_fields(self) -> None:
        self.value: str = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        httpTransformInfoInterface: TransformInfoHttpInterface = self.getTransformInfoInterface()
        self.value = httpTransformInfoInterface.getPageContext().getRequest().getParameter(StreetAddressData.ID)
    

    def isValid(self) -> bool:
        if self.getWeblisketSession().getUserName() is not None:
            return False
        billingAddressesEntity: BillingAddressesEntity = BillingAddressesEntity(self.getWeblisketSession().getUserName())
        self.streetAddress = billingAddressesEntity.get(int(self.value))
        if self.streetAddress is None:
            return False
        return self.streetAddress.isValid()
    

    def validationInfo(self) -> str:
        return self.streetAddress.validationInfo()
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
from org.allbinary.data.tables.user.address.billing.BillingAddressesEntity import BillingAddressesEntity
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.generic.address.shipping.ShippingAddressView import ShippingAddressView


@java_inherited_overloads
class DeleteValidationView(*java_bases(ShippingAddressView, ValidationComponentInterface)):
    def _java_defaults(self):
        vars(self).setdefault("value", None)

    def _init_fields(self) -> None:
        if "value" not in vars(self): self.value: str = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface)
        __class__._init_fields(self)
        httpTransformInfoInterface: TransformInfoHttpInterface = self.getTransformInfoInterface()
        self.value = httpTransformInfoInterface.getPageContext().getRequest().getParameter(StreetAddressData.ID)
    

    def isValid(self) -> bool:
        from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntity import ShippingAddressesEntity
        if self.getWeblisketSession().getUserName() is not None:
            return False
        billingAddressesEntity: ShippingAddressesEntity = ShippingAddressesEntity(self.getWeblisketSession().getUserName())
        self.streetAddress = billingAddressesEntity.get(int(self.value))
        if self.streetAddress is None:
            return False
        return java_predicate(self.streetAddress, "isValid")
    

    def validationInfo(self) -> str:
        return self.streetAddress.validationInfo()
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return java_super_call(super(), "getTransformInfoInterface")
# from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
# from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntity import ShippingAddressesEntity
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node



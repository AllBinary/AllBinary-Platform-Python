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
# package views.admin.payment.gateway

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class GatewayValidationView(HttpStoreComponentView, ValidationComponentInterface):
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
    

    def isValid(self) -> bool:
        return True
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def validationInfo(self) -> str:
        raise Exception("validationInfo")
    

    def toXmlDoc(self) -> Document:
        return None
    

    def toXmlNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def view(self) -> str:
        from views.admin.payment.gateway.GatewayView import GatewayView
        return GatewayView(self.getTransformInfoInterface()).view()
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



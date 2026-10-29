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
# package views.generic.order

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.generic.order.OrderView import OrderView


class ValidationView(OrderView, ValidationComponentInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
    

    def isValid(self) -> bool:
        try:
            valid: bool = True
            if self.order.isIdValid() == False:
                return False
            else:
                self.orderHistory = OrderHistoryFactory.getInstance(self.order.getId())
                if self.orderHistory is None or self.orderHistory.isValid() == False:
                    return False
                orderItems: OrderItemsEntity = OrderItemsEntity()
                self.basketReview = orderItems.getBasketReview(self.order.getId())
                if self.basketReview is None or self.basketReview.isValid() == False:
                    return False
            return valid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            if self.order.isIdValid() == False:
                stringBuffer.append(self.order.getIdValidationInfo())
            else:
                self.orderHistory = OrderHistoryFactory.getInstance(self.order.getId())
                if self.orderHistory is None or self.orderHistory.isValid() == False:
                    stringBuffer.append("Order History data error for: ")
                    stringBuffer.append(self.order.getId())
                    stringBuffer.append("<br />")
                orderItems: OrderItemsEntity = OrderItemsEntity()
                self.basketReview = orderItems.getBasketReview(self.order.getId())
                if self.basketReview is None:
                    stringBuffer.append("Order Items data error - does not exist for: ")
                    stringBuffer.append(self.order.getId())
                    stringBuffer.append("<br />")
                elif self.basketReview.isValid() == False:
                    stringBuffer.append("Order Items data error - not valid for: ")
                    stringBuffer.append(self.order.getId())
                    stringBuffer.append("<br />")
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryFactory import OrderHistoryFactory
from org.allbinary.data.tables.user.commerce.inventory.order.OrderItemsEntity import OrderItemsEntity
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node



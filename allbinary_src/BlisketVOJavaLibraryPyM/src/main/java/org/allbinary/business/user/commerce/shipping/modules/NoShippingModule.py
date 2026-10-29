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
# package org.allbinary.business.user.commerce.shipping.modules

from __future__ import annotations

from org.allbinary.business.user.commerce.shipping.modules.ShippingInterface import ShippingInterface


class NoShippingModule(ShippingInterface):

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.name: str = "No Shipping"
        self.description: str = "This shipping method is for items that are not shipped."
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getCost(self, order: OrderInterface) -> Money:
        return Money()
    

    def getDescription(self) -> str:
        return self.description
    

    def getName(self) -> str:
        return self.name
from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface
from org.allbinary.business.user.commerce.money.Money import Money
from org.allbinary.string.CommonStrings import CommonStrings



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
# package org.allbinary.business.user.commerce.money.payment.gateway.transaction

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


# Java interface
class PaymentTransactionInterface(TableMappingInterface, DomNodeInterface):
    

    def getOrderHistory(self) -> OrderHistory:
        raise NotImplementedError()
from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory



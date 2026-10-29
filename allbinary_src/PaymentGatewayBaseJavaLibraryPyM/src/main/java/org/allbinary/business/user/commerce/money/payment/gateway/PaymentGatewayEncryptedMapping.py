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
# package org.allbinary.business.user.commerce.money.payment.gateway

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface


class PaymentGatewayEncryptedMapping(TableMappingInterface):

    def _init_fields(self) -> None:
        self.paymentGatewayInterface: PaymentGatewayInterface = None
    

    def __init__(self, paymentGatewayInterface: PaymentGatewayInterface) -> None:
        self._init_fields()
        self.paymentGatewayInterface = paymentGatewayInterface
    

    # throws Exception
    def toHashMap(self) -> dict:
        return self.paymentGatewayInterface.toHashMap(True)
    

    def toVector(self) -> BasicArrayList:
        return self.paymentGatewayInterface.toVector(True)
    

    # throws Exception
    def getKey(self) -> object:
        return self.paymentGatewayInterface.getKey()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD



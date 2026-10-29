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
# package org.allbinary.business.user.commerce.inventory.item

from __future__ import annotations



class ItemFactoryUnused:
    

    def __init__(self) -> None:
        pass
    

    # throws MoneyException
    @staticmethod
    def getInstance(hashMap: dict) -> TableMappingInterface:
        from org.allbinary.business.user.commerce.inventory.item.Item import Item
        return Item(hashMap)
    

    # throws Exception, MoneyException
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance(request: HttpServletRequest) -> TableMappingInterface:
        from org.allbinary.business.user.commerce.inventory.item.Item import Item
        return Item(RequestParams(request).toHashMap())
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams



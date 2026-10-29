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
# package org.allbinary.data.tables.user.quoterequest

from __future__ import annotations

from org.allbinary.data.tables.BasicDataTableInterface import BasicDataTableInterface


# Java interface
class QuoteRequestEntityInterface(BasicDataTableInterface):
    

    # throws Exception
    def get(self, userName: str, id: int) -> QuoteRequest:
        raise NotImplementedError()
    

    def getIds(self, userName: str) -> BasicArrayList:
        raise NotImplementedError()
    

    def deleteWhere(self, key: str, value: str) -> None:
        raise NotImplementedError()
    

    def insert(self, values: BasicArrayList) -> None:
        raise NotImplementedError()
    

    def update(self, userName: str, updatedValues: dict) -> None:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.quoterequest.QuoteRequest import QuoteRequest



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
# package org.allbinary.logic.communication.smtp.configuration.user.event

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface


class UserEmailEventsConfigurationMapping(TableMappingInterface):

    def _init_fields(self) -> None:
        self.userEmailEventsConfigurationInterface: UserEmailEventsConfigurationInterface = None
    

    def __init__(self, userEmailEventsConfigurationInterface: UserEmailEventsConfigurationInterface) -> None:
        self._init_fields()
        self.userEmailEventsConfigurationInterface = userEmailEventsConfigurationInterface
    

    def toHashMap(self) -> dict:
        hashMap: dict = StdUtil.getInstance().createHashMap()
        return hashMap
    

    # throws Exception
    def getKey(self) -> object:
        from org.allbinary.logic.communication.smtp.configuration.user.event.UserEmailEventsConfigurationData import UserEmailEventsConfigurationData
        return UserEmailEventsConfigurationData.NAME
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        vector: BasicArrayList = BasicArrayListD()
        return vector
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil



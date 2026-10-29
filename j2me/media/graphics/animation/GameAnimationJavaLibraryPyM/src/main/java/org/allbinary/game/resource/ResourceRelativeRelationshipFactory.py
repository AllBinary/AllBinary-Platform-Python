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
# package org.allbinary.game.resource

from __future__ import annotations

from org.allbinary.game.resource.ResourceRelativeRelationshipFactoryInterface import ResourceRelativeRelationshipFactoryInterface


class ResourceRelativeRelationshipFactory(ResourceRelativeRelationshipFactoryInterface):

    def _init_fields(self) -> None:
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        self.initialized: bool = False

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def init(self, level: int) -> None:
        self.setInitialized(True)
    

    # throws Exception
    def getResourceRelativeRelationshipList(self, resource: str) -> BasicArrayList:
        listCanBeNull: object = self.hashtable.get(resource)
        if listCanBeNull is None:
            return self.basicArrayListUtil.getImmutableInstance()
        return listCanBeNull
    

    # throws Exception
    def addResourceRelativeRelationship(self, resource: str, hardPoint: RelativeRelationship) -> None:
        list_: BasicArrayList = self.getResourceRelativeRelationshipList(resource)
        if list_ == self.basicArrayListUtil.getImmutableInstance():
            list_ = BasicArrayListD()
        list_.add(hardPoint)
        self.hashtable.put(resource, list_)
    

    def isLoadingLevel(self, level: int) -> bool:
        return False
    

    def isFeature(self) -> bool:
        return False
    

    def setInitialized(self, initialized: bool) -> None:
        self.initialized = initialized
    

    def isInitialized(self) -> bool:
        return self.initialized
from org.allbinary.graphics.RelativeRelationship import RelativeRelationship
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil



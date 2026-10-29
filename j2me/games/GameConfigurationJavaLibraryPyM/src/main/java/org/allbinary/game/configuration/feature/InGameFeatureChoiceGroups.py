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
# package org.allbinary.game.configuration.feature

from __future__ import annotations



class InGameFeatureChoiceGroups:
    gameFeatureChoiceGroupsExclusive: InGameFeatureChoiceGroups = None
    gameFeatureChoiceGroupsMultiple: InGameFeatureChoiceGroups = None

    def _init_fields(self) -> None:
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getExclusiveInstance() -> InGameFeatureChoiceGroups:
        return InGameFeatureChoiceGroups.gameFeatureChoiceGroupsExclusive
    

    @staticmethod
    def getMultipleInstance() -> InGameFeatureChoiceGroups:
        return InGameFeatureChoiceGroups.gameFeatureChoiceGroupsMultiple
    

    def get(self) -> ABHashtable[object, object]:
        return self.hashtable
    

    def add(self, name: str, list_: BasicArrayList) -> None:
        self.hashtable.put(name, list_)
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList


InGameFeatureChoiceGroups.gameFeatureChoiceGroupsExclusive = InGameFeatureChoiceGroups()

InGameFeatureChoiceGroups.gameFeatureChoiceGroupsMultiple = InGameFeatureChoiceGroups()


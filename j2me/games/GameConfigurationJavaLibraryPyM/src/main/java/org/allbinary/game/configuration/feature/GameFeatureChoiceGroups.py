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

from java.lang.JavaRuntimeStatic import lazy_static


class GameFeatureChoiceGroups:
    gameFeatureChoiceGroupsExclusive: GameFeatureChoiceGroups = None
    gameFeatureChoiceGroupsMultiple: GameFeatureChoiceGroups = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.util.ABHashtable import ABHashtable
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getExclusiveInstance() -> GameFeatureChoiceGroups:
        return GameFeatureChoiceGroups.gameFeatureChoiceGroupsExclusive
    

    @staticmethod
    def getMultipleInstance() -> GameFeatureChoiceGroups:
        return GameFeatureChoiceGroups.gameFeatureChoiceGroupsMultiple
    

    def get(self) -> ABHashtable[object, object]:
        from org.allbinary.util.ABHashtable import ABHashtable
        return self.hashtable
    

    def add(self, name: str, list_: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.hashtable.put(name, list_)
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.util.ABHashtable import ABHashtable
# from org.allbinary.util.BasicArrayList import BasicArrayList


def _GameFeatureChoiceGroups_gameFeatureChoiceGroupsExclusive() -> object:
    return GameFeatureChoiceGroups()

lazy_static(GameFeatureChoiceGroups, "gameFeatureChoiceGroupsExclusive", _GameFeatureChoiceGroups_gameFeatureChoiceGroupsExclusive)

def _GameFeatureChoiceGroups_gameFeatureChoiceGroupsMultiple() -> object:
    return GameFeatureChoiceGroups()

lazy_static(GameFeatureChoiceGroups, "gameFeatureChoiceGroupsMultiple", _GameFeatureChoiceGroups_gameFeatureChoiceGroupsMultiple)


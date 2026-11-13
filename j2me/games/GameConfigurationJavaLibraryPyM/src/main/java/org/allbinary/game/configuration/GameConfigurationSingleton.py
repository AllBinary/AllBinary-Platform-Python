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
# package org.allbinary.game.configuration

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class GameConfigurationSingleton:
    SINGLETON: GameConfigurationSingleton = None

    def _init_fields(self) -> None:
        from org.allbinary.util.ABHashtable import ABHashtable
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.list_: BasicArrayList = None
        self.hashtable: ABHashtable[object, object] = None
    

    @staticmethod
    def getInstance() -> GameConfigurationSingleton:
        return GameConfigurationSingleton.SINGLETON
    

    def __init__(self) -> None:
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self._init_fields()
        self.list_ = BasicArrayListD()
        self.hashtable = StdUtil.getInstance().createHashtable()
    

    def getInstanceByName(self, name: str) -> GameConfiguration:
        return self.hashtable.get(name)
    

    def getOptionsBasicArrayList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.list_
    

    def add(self, gameConfiguration: GameConfiguration) -> None:
        self.list_.add(gameConfiguration)
    

    def getHashtable(self) -> ABHashtable[object, object]:
        from org.allbinary.util.ABHashtable import ABHashtable
        return self.hashtable
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.util.ABHashtable import ABHashtable
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _GameConfigurationSingleton_SINGLETON() -> object:
    return GameConfigurationSingleton()

lazy_static(GameConfigurationSingleton, "SINGLETON", _GameConfigurationSingleton_SINGLETON)


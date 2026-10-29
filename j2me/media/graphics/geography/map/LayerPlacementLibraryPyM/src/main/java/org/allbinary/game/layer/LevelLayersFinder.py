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
# package org.allbinary.game.layer

from __future__ import annotations



class LevelLayersFinder:
    instance: LevelLayersFinder = None

    def _init_fields(self) -> None:
        self.enumerationUtil: EnumerationUtil = EnumerationUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> LevelLayersFinder:
        return LevelLayersFinder.instance
    

    def get(self, hashtable: ABHashtable[object, object]) -> BasicArrayList:
        smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        list_: BasicArrayList = BasicArrayListD()
        enumeration: Enumeration = hashtable.keys()
        layerHashtableCanBeNull: ABHashtable[object, object] = None
        integerCanBeNull: int = None
        cachedIntegerCanBeNull: int = None
        while self.enumerationUtil.hasMoreElements(enumeration):
            layerHashtableCanBeNull = hashtable.get(self.enumerationUtil.nextElement(enumeration))
            integerCanBeNull = layerHashtableCanBeNull.get(Layer.ID)
            cachedIntegerCanBeNull = smallIntegerSingletonFactory.getAt(int(integerCanBeNull))
            if not list_.contains(cachedIntegerCanBeNull):
                list_.add(cachedIntegerCanBeNull)
        return list_
# from java.util.Enumeration import Enumeration
from org.allbinary.layer.Layer import Layer
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.EnumerationUtil import EnumerationUtil


LevelLayersFinder.instance = LevelLayersFinder()


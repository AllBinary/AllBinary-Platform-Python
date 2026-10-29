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

from org.allbinary.logic.StdUtil import StdUtil


class Feature:
    hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()

    def _init_fields(self) -> None:
        self.name: str = None
    

    def __init__(self, name: str) -> None:
        self._init_fields()
        self.name = name
        Feature.add(name, self)
        ChangedGameFeatureListener.getInstance().add(self)
    

    @staticmethod
    def getInstance(name: str) -> Feature:
        return Feature.hashtable.get(name)
    

    @staticmethod
    def add(name: str, gameFeature: Feature) -> None:
        Feature.hashtable.put(name, gameFeature)
    

    def toString(self) -> str:
        return self.getName()

    def __str__(self) -> str:
        return self.toString()
    

    def getName(self) -> str:
        return self.name
from org.allbinary.game.configuration.event.ChangedGameFeatureListener import ChangedGameFeatureListener
from org.allbinary.util.ABHashtable import ABHashtable



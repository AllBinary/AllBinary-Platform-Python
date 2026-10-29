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
# package org.allbinary.game.ai

from __future__ import annotations



class ArtificialIntelligenceInterfaceFactoryInterfaceFactory:
    SINGLETON: ArtificialIntelligenceInterfaceFactoryInterfaceFactory = None

    def _init_fields(self) -> None:
        self.list_: BasicArrayList = BasicArrayListUtil.getInstance().getImmutableInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    def clear(self) -> None:
        self.list_ = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> ArtificialIntelligenceInterfaceFactoryInterfaceFactory:
        return ArtificialIntelligenceInterfaceFactoryInterfaceFactory.SINGLETON
    

    def getInstanceFromCollection(self, hashtable: ABHashtable[object, object]) -> ArtificialIntelligenceInterfaceFactoryInterface:
        from org.allbinary.game.ai.BasicAI import BasicAI
        typeInteger: int = hashtable.get(BasicAI.ID)
        type_: int = int(typeInteger)
        artificialIntelligenceInterfaceFactoryInterface: ArtificialIntelligenceInterfaceFactoryInterface = self.list_.objectArray[type_ - 1]
        return artificialIntelligenceInterfaceFactoryInterface
    

    def add(self, artificialIntelligenceInterfaceFactoryInterface: ArtificialIntelligenceInterfaceFactoryInterface) -> None:
        self.list_.add(artificialIntelligenceInterfaceFactoryInterface)
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


ArtificialIntelligenceInterfaceFactoryInterfaceFactory.SINGLETON = ArtificialIntelligenceInterfaceFactoryInterfaceFactory()


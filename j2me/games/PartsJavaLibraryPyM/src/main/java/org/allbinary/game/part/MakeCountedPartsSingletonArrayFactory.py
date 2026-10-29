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
# package org.allbinary.game.part

from __future__ import annotations



class MakeCountedPartsSingletonArrayFactory:
    instance: MakeCountedPartsSingletonArrayFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.list_: BasicArrayList = BasicArrayListUtil.getInstance().getImmutableInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> MakeCountedPartsSingletonArrayFactory:
        return MakeCountedPartsSingletonArrayFactory.instance
    

    # throws Exception
    def getUpdated(self, partInterfaceArray: list[PartInterface]) -> list[PartInterface]:
        from org.allbinary.game.part.CountedLayerInterfaceFactoryPart import CountedLayerInterfaceFactoryPart
        self.list_ = BasicArrayListD()
        for index in range(0, len(partInterfaceArray)):
            self.list_.add(partInterfaceArray[index])
        countedBasicArrayList: BasicArrayList = CountedPickedUpLayerInterfaceFactoryPool.getInstance().getList()
        layerInterfaceFactoryInterface: CountedPickedUpLayerInterfaceFactory = None
        size: int = countedBasicArrayList.size()
        for index in range(0, size):
            layerInterfaceFactoryInterface = countedBasicArrayList.objectArray[index]
            self.list_.add(CountedLayerInterfaceFactoryPart(0, layerInterfaceFactoryInterface))
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Total Parts: ")
        stringBuffer.appendint(self.list_.size())
        stringBuffer.append(" Counted: ")
        stringBuffer.appendint(countedBasicArrayList.size())
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF(str(stringBuffer), self, commonStrings.GET_INSTANCE)
        newPartInterfaceArray: list[PartInterface] = [None] * (self.list_.size())
        newSize: int = len(newPartInterfaceArray)
        for index in range(0, newSize):
            newPartInterfaceArray[index] = self.list_.get(index)
        return newPartInterfaceArray
from org.allbinary.game.layer.pickup.CountedPickedUpLayerInterfaceFactory import CountedPickedUpLayerInterfaceFactory
from org.allbinary.game.layer.pickup.CountedPickedUpLayerInterfaceFactoryPool import CountedPickedUpLayerInterfaceFactoryPool
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


MakeCountedPartsSingletonArrayFactory.instance = MakeCountedPartsSingletonArrayFactory()


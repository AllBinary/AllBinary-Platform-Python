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
# package org.allbinary.layer

from __future__ import annotations



class LayerInterfaceFactory:
    SINGLETON: LayerInterfaceFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.list_: BasicArrayList = BasicArrayListUtil.getInstance().getImmutableInstance()
        self.HASHTABLE_LABEL: str = "Hashtable: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> LayerInterfaceFactory:
        return LayerInterfaceFactory.SINGLETON
    

    def init(self) -> None:
        self.list_ = BasicArrayListD()
    

    # throws Exception
    def getNexInstance(self, hashtable: ABHashtable[object, object], x: int, y: int, z: int) -> AllBinaryLayer:
        from org.allbinary.layer.Layer import Layer
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF(str(StringMaker().append(self.HASHTABLE_LABEL).append(StringUtil.getInstance().toString(hashtable))), self, commonStrings.GET_INSTANCE)
        typeInteger: int = hashtable.get(Layer.ID)
        layerInterfaceFactoryInterface: LayerInterfaceFactoryInterface = self.list_.objectArray[int(typeInteger) - 1]
        return layerInterfaceFactoryInterface.getNextInstance(hashtable, x, y, z)
    

    def add(self, layerInterfaceFactoryInterface: LayerInterfaceFactoryInterface) -> None:
        self.list_.add(layerInterfaceFactoryInterface)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


LayerInterfaceFactory.SINGLETON = LayerInterfaceFactory()


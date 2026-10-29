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
# package org.allbinary.media.graphics.geography.map

from __future__ import annotations

from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionBaseFactory import GeographicMapCellPositionBaseFactory


class GeographicMapCellPositionFactory(GeographicMapCellPositionBaseFactory):
    hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws Exception
    def getInstance(self, geographicMapInterface: BasicGeographicMap) -> BasicGeographicMapCellPositionFactory:
        from org.allbinary.media.graphics.geography.map.BasicGeographicMapCellPositionFactory import BasicGeographicMapCellPositionFactory
        commonStrings: CommonStrings = CommonStrings.getInstance()
        allBinaryTiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
        geographicMapCellPositionFactoryCanBeNull: object = GeographicMapCellPositionFactory.hashtable.get(allBinaryTiledLayer.getDataId())
        if geographicMapCellPositionFactoryCanBeNull is None:
            self.logUtil.putF(str(StringMaker().append("Creating GeographicMapCellPositionFactory for TileLayer: ").appendint(int(int(allBinaryTiledLayer.getDataId())))), self, commonStrings.GET_INSTANCE)
            geographicMapCellPositionFactoryCanBeNull = BasicGeographicMapCellPositionFactory(geographicMapInterface)
            GeographicMapCellPositionFactory.hashtable.put(allBinaryTiledLayer.getDataId(), geographicMapCellPositionFactoryCanBeNull)
            return geographicMapCellPositionFactoryCanBeNull
        else:
            self.logUtil.putF(str(StringMaker().append("Reusing GeographicMapCellPositionFactory for TileLayer: ").appendint(int(int(allBinaryTiledLayer.getDataId())))), self, commonStrings.GET_INSTANCE)
            return geographicMapCellPositionFactoryCanBeNull
    

    @staticmethod
    def getHashtable() -> ABHashtable[object, object]:
        return GeographicMapCellPositionFactory.hashtable
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.util.ABHashtable import ABHashtable



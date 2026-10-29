# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.input.form

from __future__ import annotations



class RTSFormInput:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.groupCommonFactory: GroupCommonFactory = GroupCommonFactory.getInstance()
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        self.newUnconstructedRTSLayerInterfaceArray: list[CollidableDestroyableDamageableLayer] = [None] * (7)
        self.groupInterfaceArray: list[Group] = None
        self.selectedGeographicCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
        self.stickyItemSelected: bool = False
        self.selectedStickyItemIndex: int = 0
        self.selectedStickyItem: ABCustomItem = ABCustomItem.getNullInstance()
    

    def __init__(self, groupInterfaceArray: list[Group]) -> None:
        self._init_fields()
        size: int = len(self.newUnconstructedRTSLayerInterfaceArray)
        for index in range(0, size):
            self.newUnconstructedRTSLayerInterfaceArray[index] = CollidableDestroyableDamageableLayer.getNullInstance()
        self.groupInterfaceArray = groupInterfaceArray
        self.hashtable.put(DirectionFactory.getInstance().NAME, DirectionFactory.getInstance().DOWN)
        if groupInterfaceArray is not None:
            self.hashtable.put(self.groupCommonFactory.ID, groupInterfaceArray)
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        pass
    

    # throws Exception
    def processAtPoint(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, point: GPoint) -> None:
        index: int = self.getIndexAt(rtsPlayerLayerInterface, point)
        if index < 0:
            return
        scrollSelectionForm: ScrollSelectionForm = rtsPlayerLayerInterface.getCurrentScrollSelectionForm()
        item: ABCustomItem = scrollSelectionForm.get(index)
        if item is None:
            return
        self.processGameSpecific(associatedRtsLayer, rtsPlayerLayerInterface, layerManager, item, index)
    

    # throws Exception
    def process(self, layerManager: AllBinaryLayerManager) -> None:
        self.setAllBinaryGameLayerManager(layerManager)
    

    # throws Exception
    def processGameSpecific(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, item: ABCustomItem, index: int) -> None:
        pass
    

    # throws Exception
    def processSticky(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, point: GPoint) -> bool:
        index: int = self.getIndexAt(rtsPlayerLayerInterface, point)
        if index < 0:
            return False
        scrollSelectionForm: ScrollSelectionForm = rtsPlayerLayerInterface.getCurrentScrollSelectionForm()
        item: ABCustomItem = scrollSelectionForm.get(index)
        if item is None:
            return False
        self.processStickyGameSpecific(associatedRtsLayer, rtsPlayerLayerInterface, layerManager, item, index)
        return True
    

    # throws Exception
    def processStickyGameSpecific(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, item: ABCustomItem, index: int) -> None:
        pass
    

    # throws Exception
    def getItemAt(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface, point: GPoint) -> ABCustomItem:
        self.logUtil.putF(str(StringMaker().append("Point: ").append(StringUtil.getInstance().toString(point))), self, "getItemAt")
        scrollSelectionForm: ScrollSelectionForm = rtsPlayerLayerInterface.getCurrentScrollSelectionForm()
        return scrollSelectionForm.getSelectedItem(point)
    

    # throws Exception
    def getIndexAt(self, rtsPlayerLayerInterface: RTSPlayerLayerInterface, point: GPoint) -> int:
        self.logUtil.putF(str(StringMaker().append("Point: ").append(StringUtil.getInstance().toString(point))), self, "getItemAt")
        scrollSelectionForm: ScrollSelectionForm = rtsPlayerLayerInterface.getCurrentScrollSelectionForm()
        return scrollSelectionForm.getSelectedIndexForPoint(point)
    

    # throws Exception
    def getInstance(self, layerManager: AllBinaryLayerManager, aItem: ABCustomItem, geographicMapCellPosition: GeographicMapCellPosition) -> CollidableDestroyableDamageableLayer:
        item: LayerInterfaceFactoryImageItem = aItem
        layerInterfaceFactoryInterface: LayerInterfaceFactoryInterface = item.getLayerInterfaceFactoryInterface()
        cellPoint: GPoint = geographicMapCellPosition.getPoint()
        if layerInterfaceFactoryInterface is not None:
            self.hashtable.put(AllBinaryGameLayerManager.ID, layerManager)
            return layerInterfaceFactoryInterface.getNextInstance(self.getHashtable(), cellPoint.getX(), cellPoint.getY(), cellPoint.getZ())
        return CollidableDestroyableDamageableLayer.getNullInstance()
    

    def getSelectedGeographicCellPosition(self) -> GeographicMapCellPosition:
        return self.selectedGeographicCellPosition
    

    def setSelectedGeographicCellPosition(self, selectedGeographicCellPosition: GeographicMapCellPosition) -> None:
        self.logUtil.putF(str(StringMaker().append("Selected GeographicMapCellPosition: ").append(str(selectedGeographicCellPosition))), self, "setSelectedGeographicCellPosition")
        self.selectedGeographicCellPosition = selectedGeographicCellPosition
    

    def isStickyItemSelected(self) -> bool:
        return self.stickyItemSelected
    

    def setStickyItemSelected(self, stickyItemSelected: bool) -> None:
        self.stickyItemSelected = stickyItemSelected
    

    def getSelectedStickyItem(self) -> ABCustomItem:
        return self.selectedStickyItem
    

    def setSelectedStickyItem(self, selectedStickyItem: ABCustomItem) -> None:
        self.selectedStickyItem = selectedStickyItem
    

    def getSelectedStickyItemIndex(self) -> int:
        return self.selectedStickyItemIndex
    

    def setSelectedStickyItemIndex(self, selectedStickyItemIndex: int) -> None:
        self.selectedStickyItemIndex = selectedStickyItemIndex
    

    def getHashtable(self) -> ABHashtable[object, object]:
        return self.hashtable
from org.allbinary.game.identification.GroupCommonFactory import GroupCommonFactory
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.game.layer.item.LayerInterfaceFactoryImageItem import LayerInterfaceFactoryImageItem
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.direction.DirectionFactory import DirectionFactory
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.layer.LayerInterfaceFactoryInterface import LayerInterfaceFactoryInterface
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
from org.allbinary.util.ABHashtable import ABHashtable



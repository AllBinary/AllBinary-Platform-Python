# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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

from org.allbinary.game.input.form.RTSFormInput import RTSFormInput


class CompositeRTSFormInput(RTSFormInput):

    def _init_fields(self) -> None:
        self.rtsFormInputArray: list[RTSFormInput] = None
        self.itemIndex: list[int] = None
        self.isPrimaryWaypointCreator: bool = None
    

    def __init__(self, groupInterface: list[Group], isPrimaryWaypointCreator: bool, itemIndex: list[int]) -> None:
        from org.allbinary.game.input.form.WaypointRTSFormInput import WaypointRTSFormInput
        from org.allbinary.game.input.form.UnitRTSFormInput import UnitRTSFormInput
        super().__init__(groupInterface)
        self._init_fields()
        self.itemIndex = itemIndex
        self.isPrimaryWaypointCreator = isPrimaryWaypointCreator
        self.rtsFormInputArray = [None] * (2)
        self.rtsFormInputArray[0] = WaypointRTSFormInput(self.groupInterfaceArray, isPrimaryWaypointCreator)
        self.rtsFormInputArray[1] = UnitRTSFormInput(self.groupInterfaceArray)
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        super().setAllBinaryGameLayerManager(allBinaryGameLayerManager)
        geographicMapCompositeInterface: GeographicMapCompositeInterface = allBinaryGameLayerManager
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        size: int = len(self.rtsFormInputArray)
        for index in range(0, size):
            self.rtsFormInputArray[index].setAllBinaryGameLayerManager(allBinaryGameLayerManager)
    

    # throws Exception
    def processAtPoint(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, point: GPoint) -> None:
        scrollSelectionForm: ScrollSelectionForm = rtsPlayerLayerInterface.getCurrentScrollSelectionForm()
        index: int = scrollSelectionForm.getSelectedIndexForPoint(point)
        if self.isStickyItemSelected() and associatedRtsLayer == CollidableDestroyableDamageableLayer.getNullInstance():
            if self.getSelectedStickyItemIndex() <= self.itemIndex[0]:
                self.rtsFormInputArray[0].processAtPoint(associatedRtsLayer, rtsPlayerLayerInterface, layerManager, point)
        elif index > self.itemIndex[0]:
            self.rtsFormInputArray[1].processAtPoint(associatedRtsLayer, rtsPlayerLayerInterface, layerManager, point)
    

    # throws Exception
    def processGameSpecific(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, item: ABCustomItem, index: int) -> None:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF(str(CommonLabels.getInstance().INDEX_LABEL + index) + " > " + str(self.itemIndex[0]), self, commonStrings.PROCESS)
        if self.isStickyItemSelected() and associatedRtsLayer == CollidableDestroyableDamageableLayer.getNullInstance():
            if self.getSelectedStickyItemIndex() <= self.itemIndex[0]:
                self.rtsFormInputArray[0].processGameSpecific(associatedRtsLayer, rtsPlayerLayerInterface, layerManager, item, index)
        elif index > self.itemIndex[0]:
            self.rtsFormInputArray[1].processGameSpecific(associatedRtsLayer, rtsPlayerLayerInterface, layerManager, item, index)
    

    # throws Exception
    def processSticky(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, point: GPoint) -> bool:
        return self.rtsFormInputArray[0].processSticky(associatedRtsLayer, rtsPlayerLayerInterface, layerManager, point)
    

    # throws Exception
    def processStickyGameSpecific(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, item: ABCustomItem, index: int) -> None:
        self.rtsFormInputArray[0].processStickyGameSpecific(associatedRtsLayer, rtsPlayerLayerInterface, layerManager, item, index)
    

    def getSelectedStickyItemIndex(self) -> int:
        return self.rtsFormInputArray[0].getSelectedStickyItemIndex()
    

    def isStickyItemSelected(self) -> bool:
        return self.rtsFormInputArray[0].isStickyItemSelected()
    

    def setStickyItemSelected(self, stickyItemSelected: bool) -> None:
        self.rtsFormInputArray[0].setStickyItemSelected(stickyItemSelected)
    

    def getSelectedStickyItem(self) -> ABCustomItem:
        return self.rtsFormInputArray[0].getSelectedStickyItem()
    

    def setSelectedStickyItem(self, selectedStickyItem: ABCustomItem) -> None:
        self.rtsFormInputArray[0].setSelectedStickyItem(selectedStickyItem)
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.string.CommonLabels import CommonLabels



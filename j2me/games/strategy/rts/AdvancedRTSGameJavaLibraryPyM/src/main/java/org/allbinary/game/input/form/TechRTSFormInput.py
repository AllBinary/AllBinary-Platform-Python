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


class TechRTSFormInput(RTSFormInput):

    def _init_fields(self) -> None:
        self.EVENT: AllBinaryEventObject = AllBinaryEventObject(self)
        self.noMoneyGameNotificationEvent: GameNotificationEvent = None
    

    def __init__(self, groupInterface: list[Group]) -> None:
        super().__init__(groupInterface)
        self._init_fields()
        basicColorFactory: BasicColorFactory = BasicColorFactory.getInstance()
        self.noMoneyGameNotificationEvent = GameNotificationEvent(self, RTSGameStrings.getInstance().NO_MONEY, SmallIntegerSingletonFactory.getInstance().getAt(2), basicColorFactory.WHITE, BooleanFactory.getInstance().FALSE)
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        super().setAllBinaryGameLayerManager(allBinaryGameLayerManager)
        geographicMapCompositeInterface: GeographicMapCompositeInterface = allBinaryGameLayerManager
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        self.noMoneyGameNotificationEvent.setBasicColorP(geographicMapInterface.getForegroundBasicColor())
    

    # throws Exception
    def processGameSpecific(self, associatedRtsLayer: CollidableDestroyableDamageableLayer, rtsPlayerLayerInterface: RTSPlayerLayerInterface, layerManager: AllBinaryLayerManager, item: ABCustomItem, itemIndex: int) -> None:
        super().process(layerManager)
        commonStrings: CommonStrings = CommonStrings.getInstance()
        stringMaker: StringMaker = StringMaker()
        technologyRTSInterfaceImageItem: TechnologyRTSInterfaceImageItem = item
        rtsInterface: RTSInterface = technologyRTSInterfaceImageItem.getRtsInterface()
        self.logUtil.putF(str(stringMaker.append("isUpgradeable: ").appendboolean(rtsInterface.isUpgradeable())), self, commonStrings.PROCESS)
        if rtsInterface.isUpgradeable():
            cost: int = rtsInterface.getUpgradeCost()
            capital: Capital = rtsPlayerLayerInterface.getCapital()
            stringMaker.delete(0, stringMaker.length())
            self.logUtil.putF(str(stringMaker.appendint(cost).append("<=").appendint(int(capital.getTotalMoney()))), self, commonStrings.PROCESS)
            if cost <= capital.getTotalMoney():
                rtsPlayerLayerInterface.add(BuildingSound.getInstance())
                capital.removeMoney(cost)
                rtsInterface.upgrade()
                technologyRTSInterfaceImageItem.update()
                TechEventHandler.getInstance().fireEvent(self.EVENT)
            else:
                rtsPlayerLayerInterface.add(ErrorSound.getInstance())
                if not rtsPlayerLayerInterface.implmentsArtificialIntelligenceCompositeInterface():
                    GameNotificationEventHandler.getInstance().fireEvent(self.noMoneyGameNotificationEvent)
from org.allbinary.game.layer.RTSGameStrings import RTSGameStrings
from org.allbinary.game.layer.RTSInterface import RTSInterface
from org.allbinary.game.layer.RTSPlayerLayerInterface import RTSPlayerLayerInterface
from org.allbinary.game.layer.TechnologyRTSInterfaceImageItem import TechnologyRTSInterfaceImageItem
from org.allbinary.game.layer.capital.Capital import Capital
from org.allbinary.game.rts.technology.event.TechEventHandler import TechEventHandler
from org.allbinary.graphics.form.item.ABCustomItem import ABCustomItem
from org.allbinary.media.audio.BuildingSound import BuildingSound
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.hud.event.GameNotificationEvent import GameNotificationEvent
from org.allbinary.game.layer.hud.event.GameNotificationEventHandler import GameNotificationEventHandler
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.audio.ErrorSound import ErrorSound
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface



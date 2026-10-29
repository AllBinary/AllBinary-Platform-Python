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



class GameConfigurationUtil:
    instance: GameConfigurationUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.GAUGE_UPDATE: str = "Gauge Update: "
        self.FROM: str = " from: "
        self.TO: str = " to: "
        self.COMPETITION_VALUE: int = 1

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GameConfigurationUtil:
        return GameConfigurationUtil.instance
    

    # throws Exception
    def change(self, gameOptionsForm: GameOptionsForm, gauge: GameConfigurationGauge) -> None:
        from org.allbinary.game.configuration.GameConfigurationSingleton import GameConfigurationSingleton
        self.update(gauge)
        gameConfigurationSingleton: GameConfigurationSingleton = GameConfigurationSingleton.getInstance()
        gameConfiguration: GameConfiguration = gameConfigurationSingleton.getInstanceByName(gauge.getLabel())
        self.updateChallange(gameOptionsForm, gameConfiguration)
    

    # throws Exception
    def update(self, gauge: GameConfigurationGauge) -> None:
        from org.allbinary.game.configuration.GameConfigurationSingleton import GameConfigurationSingleton
        gameConfigurationSingleton: GameConfigurationSingleton = GameConfigurationSingleton.getInstance()
        gameConfiguration: GameConfiguration = gameConfigurationSingleton.getInstanceByName(gauge.getLabel())
        smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        value: int = smallIntegerSingletonFactory.getAt(gauge.getValue() + int(gameConfiguration.getMinValue()))
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.GAUGE_UPDATE)
        stringBuffer.append(gameConfiguration.getName())
        stringBuffer.append(self.FROM)
        stringBuffer.appendint(int(int(gameConfiguration.getValue())))
        stringBuffer.append(self.TO)
        stringBuffer.appendint(int(int(value)))
        self.logUtil.putF(str(stringBuffer), self, self.commonStrings.UPDATE)
        gameConfiguration.setValue(value)
    

    # throws Exception
    def setDefault(self, gauge: GameConfigurationGauge) -> None:
        from org.allbinary.game.configuration.GameConfigurationSingleton import GameConfigurationSingleton
        gameConfigurationSingleton: GameConfigurationSingleton = GameConfigurationSingleton.getInstance()
        gameConfiguration: GameConfiguration = gameConfigurationSingleton.getInstanceByName(gauge.getLabel())
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Gauge Default: ")
        stringBuffer.append(gameConfiguration.getName())
        stringBuffer.append(self.TO)
        stringBuffer.appendint(int(int(gameConfiguration.getDefaultValue())))
        self.logUtil.putF(str(stringBuffer), self, "setDefault")
        gauge.setValue(int(gameConfiguration.getDefaultValue()) - int(gameConfiguration.getMinValue()))
        gameConfiguration.setValue(gameConfiguration.getDefaultValue())
    

    # throws Exception
    def updateChallange(self, gameOptionsForm: GameOptionsForm, gameConfiguration: GameConfiguration) -> None:
        from org.allbinary.game.configuration.GameConfigurationSingleton import GameConfigurationSingleton
        from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
        gameConfigurationSingleton: GameConfigurationSingleton = GameConfigurationSingleton.getInstance()
        gameConfigurationCentral: GameConfigurationCentral = GameConfigurationCentral.getInstance()
        if gameConfiguration == gameConfigurationCentral.CHALLENGE_LEVEL:
            self.logUtil.putF(self.commonStrings.START, self, "updateChallange")
            gameConfigurationCentral.COLLIDE_DAMAGE.setValue(gameConfiguration.getValue())
            gameConfigurationCentral.ATTACK_CHALLENGE_LEVEL.setValue(gameConfiguration.getValue())
            gameConfigurationCentral.DURABILITY_CHALLENGE_LEVEL.setValue(gameConfiguration.getValue())
            gameConfigurationCentral.SPEED_CHALLENGE_LEVEL.setValue(gameConfiguration.getValue())
            size: int = gameOptionsForm.size()
            for index in range(0, size):
                item: Item = gameOptionsForm.get(index)
                if isinstance(item, GameConfigurationGauge):
                    gauge: GameConfigurationGauge = item
                    name: str = item.getLabel()
                    nextGameConfiguration: GameConfiguration = gameConfigurationSingleton.getInstanceByName(name)
                    if nextGameConfiguration == gameConfigurationCentral.COLLIDE_DAMAGE:
                        gauge.setValue(int(gameConfigurationCentral.COLLIDE_DAMAGE.getValue()) - int(gameConfiguration.getMinValue()))
                    elif nextGameConfiguration == gameConfigurationCentral.DURABILITY_CHALLENGE_LEVEL:
                        gauge.setValue(int(gameConfigurationCentral.DURABILITY_CHALLENGE_LEVEL.getValue()) - int(gameConfiguration.getMinValue()))
                    elif nextGameConfiguration == gameConfigurationCentral.ATTACK_CHALLENGE_LEVEL:
                        gauge.setValue(int(gameConfigurationCentral.ATTACK_CHALLENGE_LEVEL.getValue()) - int(gameConfiguration.getMinValue()))
                    elif nextGameConfiguration == gameConfigurationCentral.SPEED_CHALLENGE_LEVEL:
                        gauge.setValue(int(gameConfigurationCentral.SPEED_CHALLENGE_LEVEL.getValue()) - int(gameConfiguration.getMinValue()))
    

    def updateCompetitionValue(self) -> None:
        from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
        self.logUtil.putF(self.commonStrings.START, self, "updateCompetitionValue")
        gameConfigurationCentral: GameConfigurationCentral = GameConfigurationCentral.getInstance()
        self.COMPETITION_VALUE = int(gameConfigurationCentral.COLLIDE_DAMAGE.getValue()) + int(gameConfigurationCentral.ATTACK_CHALLENGE_LEVEL.getValue()) + int(gameConfigurationCentral.DURABILITY_CHALLENGE_LEVEL.getValue()) + int(gameConfigurationCentral.SPEED_CHALLENGE_LEVEL.getValue())
        self.COMPETITION_VALUE = (self.COMPETITION_VALUE >> 2)
    

    def getCompetitionValue(self) -> int:
        return self.COMPETITION_VALUE
# from javax.microedition.lcdui.Item import Item
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings


GameConfigurationUtil.instance = GameConfigurationUtil()


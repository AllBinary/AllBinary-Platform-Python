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

from org.allbinary.logic.NullUtil import NullUtil


class GameConfigurationCentral:
    SINGLETON: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.SCALE: GameConfiguration = None
        self.ORIENTATION: GameConfiguration = None
        self.SENSOR_UPDATE_RATE: GameConfiguration = None
        self.VIBRATION: GameConfiguration = None
        self.CHALLENGE_LEVEL: GameConfiguration = None
        self.COLLIDE_DAMAGE: GameConfiguration = None
        self.DURABILITY_CHALLENGE_LEVEL: GameConfiguration = None
        self.SPEED_CHALLENGE_LEVEL: GameConfiguration = None
        self.ATTACK_CHALLENGE_LEVEL: GameConfiguration = None
        self.CONTROL_LEVEL: GameConfiguration = None
        self.PLAYER_INPUT_WAIT: GameConfiguration = None
        self.SPEED: GameConfiguration = None
        self.SOUND_VOLUME: GameConfiguration = None
        self.MAX_GAME_OBJECTS: GameConfiguration = None
        self.MAX_LAYERS: GameConfiguration = None
        self.gameControlFidelity: int = 36
    

    @staticmethod
    def getInstance() -> GameConfigurationCentral:
        if GameConfigurationCentral.SINGLETON == NullUtil.getInstance().NULL_OBJECT:
            GameConfigurationCentral.SINGLETON = GameConfigurationCentral()
        return GameConfigurationCentral.SINGLETON
    

    def __init__(self) -> None:
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        self._init_fields()
        smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        self.SCALE = GameConfiguration("Scale", smallIntegerSingletonFactory.getAt(2), smallIntegerSingletonFactory.getAt(2), smallIntegerSingletonFactory.getAt(3))
        self.ORIENTATION = GameConfiguration("Orientation", smallIntegerSingletonFactory.getAt(0), smallIntegerSingletonFactory.getAt(0), smallIntegerSingletonFactory.getAt(8))
        self.SENSOR_UPDATE_RATE = GameConfiguration("Sensor Update Rate", smallIntegerSingletonFactory.getAt(0), smallIntegerSingletonFactory.getAt(0), smallIntegerSingletonFactory.getAt(3))
        self.VIBRATION = GameConfiguration("Vibration", smallIntegerSingletonFactory.getAt(0), smallIntegerSingletonFactory.getAt(0), smallIntegerSingletonFactory.getAt(3))
        self.CHALLENGE_LEVEL = GameConfiguration("Global Challenge Level", smallIntegerSingletonFactory.getAt(3), smallIntegerSingletonFactory.getAt(1), smallIntegerSingletonFactory.getAt(10))
        self.COLLIDE_DAMAGE = GameConfiguration("Collide Damage Challenge Level", smallIntegerSingletonFactory.getAt(3), smallIntegerSingletonFactory.getAt(1), smallIntegerSingletonFactory.getAt(10))
        self.DURABILITY_CHALLENGE_LEVEL = GameConfiguration("Enemy Durability Challenge Level", smallIntegerSingletonFactory.getAt(3), smallIntegerSingletonFactory.getAt(1), smallIntegerSingletonFactory.getAt(10))
        self.SPEED_CHALLENGE_LEVEL = GameConfiguration("Enemy Speed Challenge Level", smallIntegerSingletonFactory.getAt(3), smallIntegerSingletonFactory.getAt(1), smallIntegerSingletonFactory.getAt(10))
        self.ATTACK_CHALLENGE_LEVEL = GameConfiguration("Enemy Attack Challenge Level", smallIntegerSingletonFactory.getAt(3), smallIntegerSingletonFactory.getAt(1), smallIntegerSingletonFactory.getAt(10))
        self.CONTROL_LEVEL = GameConfiguration("Control Fidelity", smallIntegerSingletonFactory.getAt(5), smallIntegerSingletonFactory.getAt(1), smallIntegerSingletonFactory.getAt(10))
        self.PLAYER_INPUT_WAIT = GameConfiguration("Input Wait", smallIntegerSingletonFactory.getAt(5), smallIntegerSingletonFactory.getAt(1), smallIntegerSingletonFactory.getAt(10))
        self.SPEED = GameConfiguration("Game Speed (Device Specific)", smallIntegerSingletonFactory.getAt(5), smallIntegerSingletonFactory.getAt(1), smallIntegerSingletonFactory.getAt(10))
        self.SOUND_VOLUME = GameConfiguration("Sound Volume", smallIntegerSingletonFactory.getAt(6), smallIntegerSingletonFactory.getAt(0), smallIntegerSingletonFactory.getAt(10))
        self.MAX_GAME_OBJECTS = GameConfiguration("Max Game Objects", smallIntegerSingletonFactory.getAt(20), smallIntegerSingletonFactory.getAt(1), smallIntegerSingletonFactory.getAt(50))
        self.MAX_LAYERS = GameConfiguration("Max Layers", smallIntegerSingletonFactory.getAt(20), smallIntegerSingletonFactory.getAt(1), smallIntegerSingletonFactory.getAt(50))
    

    def load(self, abeClientInformation: AbeClientInformationInterface) -> None:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
            keyValuePersistance: KeyValuePersistance = GameConfigurationPersistanceSingleton.getInstance()
            keyValuePersistance.clear()
            keyValuePersistance.loadAll(abeClientInformation)
            list_: BasicArrayList = keyValuePersistance.getIds()
            if list_.size() > 0:
                hashtable: ABHashtable[object, object] = keyValuePersistance.get(0)
                anyType: object = self.SCALE.getName()
                value: str = hashtable.get(anyType)
                self.SCALE.setValue(smallIntegerSingletonFactory.getAt(int(str(value))))
            else:
                self.logUtil.putF("No Game Configuration To Load", self, commonStrings.LOAD)
        except Exception as e:
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.LOAD, e)
    

    def setGameControlFidelity(self, gameControlFidelity: int) -> None:
        self.gameControlFidelity = gameControlFidelity
    

    def getGameControlFidelity(self) -> int:
        return self.gameControlFidelity
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        commonStrings: CommonSeps = CommonSeps.getInstance()
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.SCALE.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.SCALE.getValue())))
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.ORIENTATION.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.ORIENTATION.getValue())))
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.SENSOR_UPDATE_RATE.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.SENSOR_UPDATE_RATE.getValue())))
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.VIBRATION.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.VIBRATION.getValue())))
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.CHALLENGE_LEVEL.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.CHALLENGE_LEVEL.getValue())))
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.COLLIDE_DAMAGE.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.COLLIDE_DAMAGE.getValue())))
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.DURABILITY_CHALLENGE_LEVEL.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.DURABILITY_CHALLENGE_LEVEL.getValue())))
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.SPEED_CHALLENGE_LEVEL.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.SPEED_CHALLENGE_LEVEL.getValue())))
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.ATTACK_CHALLENGE_LEVEL.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.ATTACK_CHALLENGE_LEVEL.getValue())))
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.CONTROL_LEVEL.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.CONTROL_LEVEL.getValue())))
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.SPEED.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.SPEED.getValue())))
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.MAX_GAME_OBJECTS.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.MAX_GAME_OBJECTS.getValue())))
        stringBuffer.append(commonStrings.COMMA_SEP)
        stringBuffer.append(self.MAX_LAYERS.getName())
        stringBuffer.append(commonStrings.EQUALS)
        stringBuffer.appendint(int(int(self.MAX_LAYERS.getValue())))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.game.configuration.persistance.GameConfigurationPersistanceSingleton import GameConfigurationPersistanceSingleton
from org.allbinary.game.configuration.persistance.KeyValuePersistance import KeyValuePersistance
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList



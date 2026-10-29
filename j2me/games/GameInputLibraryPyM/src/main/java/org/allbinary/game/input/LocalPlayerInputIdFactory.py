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
# package org.allbinary.game.input

from __future__ import annotations



class LocalPlayerInputIdFactory:
    instance: LocalPlayerInputIdFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.MAX_NUMBER_OF_PLAYERS: int = 6
        self.MAX_FAST_DEVICEID: int = 65
        self.deviceIdToplayerId: list[int] = [0] * (self.MAX_FAST_DEVICEID)
        self.playerIdToDeviceId: list[int] = [0] * (self.MAX_NUMBER_OF_PLAYERS)
        self.playersInPlay: list[bool] = [False] * (self.MAX_NUMBER_OF_PLAYERS)
        self.totalDevicesMapped: int = 0
    

    def __init__(self) -> None:
        self._init_fields()
        for index in range(len(self.deviceIdToplayerId) - 1, 0 - 1, -1):
            self.deviceIdToplayerId[index] = -1
    

    @staticmethod
    def getInstance() -> LocalPlayerInputIdFactory:
        return LocalPlayerInputIdFactory.instance
    

    def getDeviceId(self, playerInputId: int) -> int:
        return self.playerIdToDeviceId[playerInputId]
    

    def getPlayerForDevice(self, deviceId: int) -> int:
        index: int = 0
        if deviceId < self.MAX_FAST_DEVICEID:
            playerInputId: int = self.deviceIdToplayerId[deviceId]
            if playerInputId != -1:
                return playerInputId
        else:
            for index in range(self.totalDevicesMapped - 1, 0 - 1, -1):
                if self.playerIdToDeviceId[index] == deviceId:
                    return index
        index = self.totalDevicesMapped
        if deviceId < self.MAX_FAST_DEVICEID:
            self.deviceIdToplayerId[deviceId] = index
        else:
            self.logUtil.putF(str(StringMaker().append("Added DeviceId: ").appendint(deviceId).append(" beyond fast Id list")), self, "getPlayerForDevice")
        self.playerIdToDeviceId[index] = deviceId
        AnalogLocationInputFactory.getInstance().addPlayer(self.totalDevicesMapped)
        self.totalDevicesMapped += 1
        self.logUtil.putF(str(StringMaker().append("Added DeviceId: ").appendint(deviceId).append(" at: ").appendint(index).append(" Total: ").appendint(self.totalDevicesMapped)), self, "getPlayerForDevice")
        return index
    

    def getTotalDevicesInPlay(self) -> int:
        total: int = 0
        for index in range(self.totalDevicesMapped - 1, 0 - 1, -1):
            if self.playersInPlay[index] == True:
                total += 1
        return total
    

    def isPlayerInPlay(self, playerInputId: int) -> bool:
        return self.playersInPlay[playerInputId]
    

    def setPlayerInPlay(self, playerInputId: int) -> None:
        self.logUtil.putF(str(StringMaker().append("Setting PlayerInPlay with playerInputId: ").appendint(playerInputId)), self, "setPlayerInPlay")
        self.playersInPlay[playerInputId] = True
    

    def setPlayerOutOfPlay(self, playerInputId: int) -> None:
        self.logUtil.putF(str(StringMaker().append("Setting PlayerOutOfPlay with playerInputId: ").appendint(playerInputId)), self, "setPlayerOutOfPlay")
        self.playersInPlay[playerInputId] = False
    

    def getPlayersInPlay(self) -> list[bool]:
        return self.playersInPlay
from org.allbinary.game.input.analog.AnalogLocationInputFactory import AnalogLocationInputFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker


LocalPlayerInputIdFactory.instance = LocalPlayerInputIdFactory()


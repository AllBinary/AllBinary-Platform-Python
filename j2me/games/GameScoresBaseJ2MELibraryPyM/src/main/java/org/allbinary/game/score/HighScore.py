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
# package org.allbinary.game.score

from __future__ import annotations



class HighScore:

    def _init_fields(self) -> None:
        self.id: int = None
        self.name: str = None
        self.gameInfo: GameInfo = None
        self.score: int = None
        self.scoreString: str = None
    

    def __init__(self, id: int, name: str, gameInfo: GameInfo, score: int) -> None:
        self._init_fields()
        self.id = id
        self.name = name
        self.gameInfo = gameInfo
        self.score = score
        self.scoreString = str(self.score)
    

    def getId(self) -> int:
        return self.id
    

    def getName(self) -> str:
        return self.name
    

    def getScore(self) -> int:
        return self.score
    

    # throws Exception
    def getAsBytes(self) -> list[int]:
        byteArrayOutputStream: ByteArrayOutputStream = ByteArrayOutputStream()
        outputStream: DataOutputStream = DataOutputStream(byteArrayOutputStream)
        outputStream.writeUTF(self.getName())
        outputStream.writeLong(self.getScore())
        return byteArrayOutputStream.toByteArray()
    

    def getGameInfo(self) -> GameInfo:
        return self.gameInfo
    

    def getScoreString(self) -> str:
        return self.scoreString
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def toString(self) -> str:
        commonSeps: CommonSeps = CommonSeps.getInstance()
        return str(StringMaker().append(self.name).append(commonSeps.COLON).appendlong(self.score).append(commonSeps.FORWARD_SLASH).append(self.scoreString))

    def __str__(self) -> str:
        return self.toString()
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.DataOutputStream import DataOutputStream
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps



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
# package org.allbinary.input.automation.module.game.skill

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class GameSkill:
    hashMap: HashMap = None

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.gameSkillType: GameSkillType = None
        self.extra: str = None
        self.time: int = 0
        self.vector: BasicArrayList = None
        self.GAME_SKILL_LABEL: str = "GameSkill: "
        self.EXTRA_LABEL: str = "Extra: "
        self.TIME_LABEL: str = "Time: "
    

    def __init__(self, gameSkillType: GameSkillType, extra: str, time: int) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        self._init_fields()
        self.setGameSkillType(gameSkillType)
        self.setExtra(extra)
        self.setTime(time)
        self.vector = BasicArrayListD()
        GameSkill.hashMap.put(str(StringMaker().append(self.getGameSkillType().getName()).append(CommonSeps.getInstance().SPACE).append(extra)), self)
    

    def getGameSkillType(self) -> GameSkillType:
        return self.gameSkillType
    

    def setGameSkillType(self, gameSkillType: GameSkillType) -> None:
        self.gameSkillType = gameSkillType
    

    def getExtra(self) -> str:
        return self.extra
    

    def setExtra(self, extra: str) -> None:
        self.extra = extra
    

    def getTime(self) -> int:
        return self.time
    

    def setTime(self, time: int) -> None:
        self.time = time
    

    def addProperty(self, gameSkillPropertyInterface: GameSkillPropertyInterface) -> None:
        self.vector.add(gameSkillPropertyInterface)
    

    def getProperties(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.vector
    

    @staticmethod
    def getInstance(gameSkillType: GameSkillType, extra: str) -> GameSkill:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        return GameSkill.hashMap.get(str(StringMaker().append(gameSkillType.getName()).append(CommonSeps.getInstance().SPACE).append(extra)))
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        commonSeps: CommonSeps = CommonSeps.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.GAME_SKILL_LABEL)
        stringBuffer.append(str(self.getGameSkillType()))
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(self.EXTRA_LABEL)
        stringBuffer.append(self.getExtra())
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(self.TIME_LABEL)
        stringBuffer.appendlong(self.getTime())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps


def _GameSkill_hashMap() -> object:
    from java.util.HashMap import HashMap
    from org.allbinary.logic.StdUtil import StdUtil
    return StdUtil.getInstance().createHashMap()

lazy_static(GameSkill, "hashMap", _GameSkill_hashMap)


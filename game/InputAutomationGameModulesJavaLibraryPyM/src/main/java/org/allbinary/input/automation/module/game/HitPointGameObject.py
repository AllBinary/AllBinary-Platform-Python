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
# package org.allbinary.input.automation.module.game

from __future__ import annotations

from org.allbinary.input.automation.module.game.MeteredGameObject import MeteredGameObject
from org.allbinary.input.automation.module.game.HitPointGameObjectInterface import HitPointGameObjectInterface


class HitPointGameObject(MeteredGameObject, HitPointGameObjectInterface):

    def _init_fields(self) -> None:
        self.damaged: bool = False
        self.closeDeath: bool = False
        self.HP_LABEL: str = "HP: "
        self.IS_DAMAGED_LABEL: str = "isDamaged: "
        self.IS_CLOSE_DEATH_LABEL: str = "isCloseDeath: "
    

    def __init__(self, bufferedImage: list[BufferedImage], minX: int, maxX: int, y: int) -> None:
        super().__init__(bufferedImage, minX, maxX, y)
        self._init_fields()
        if float(self.getRatios()[len(bufferedImage) - 1]) < 1.0:
            self.setDamaged(True)
        else:
            self.setDamaged(False)
        if float(self.getRatios()[len(bufferedImage) - 1]) > 0.25:
            self.closeDeath = False
        else:
            self.closeDeath = True
    

    def isMoreThan(self, aFloat: float) -> bool:
        if float(self.getRatios()[len(self.getRatios()) - 1]) > aFloat:
            return True
        else:
            return False
    

    def isCloseDeath(self) -> bool:
        return self.closeDeath
    

    def setCloseDeath(self, closeDeath: bool) -> None:
        self.closeDeath = closeDeath
    

    def isDamaged(self) -> bool:
        return self.damaged
    

    def setDamaged(self, damaged: bool) -> None:
        self.damaged = damaged
    

    def toString(self) -> str:
        commonSeps: CommonSeps = CommonSeps.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.HP_LABEL)
        stringBuffer.append(str(super()))
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(self.IS_DAMAGED_LABEL)
        stringBuffer.appendboolean(self.isDamaged())
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(self.IS_CLOSE_DEATH_LABEL)
        stringBuffer.appendboolean(self.isCloseDeath())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps



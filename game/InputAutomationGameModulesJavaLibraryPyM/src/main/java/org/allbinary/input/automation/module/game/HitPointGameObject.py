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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.input.automation.module.game.MeteredGameObject import MeteredGameObject
from org.allbinary.input.automation.module.game.HitPointGameObjectInterface import HitPointGameObjectInterface


@java_inherited_overloads
class HitPointGameObject(*java_bases(MeteredGameObject, HitPointGameObjectInterface)):
    def _java_defaults(self):
        vars(self).setdefault("damaged", False)
        vars(self).setdefault("closeDeath", False)
        vars(self).setdefault("HP_LABEL", None)
        vars(self).setdefault("IS_DAMAGED_LABEL", None)
        vars(self).setdefault("IS_CLOSE_DEATH_LABEL", None)

    def _init_fields(self) -> None:
        self.damaged: bool = False
        self.closeDeath: bool = False
        self.HP_LABEL: str = "HP: "
        self.IS_DAMAGED_LABEL: str = "isDamaged: "
        self.IS_CLOSE_DEATH_LABEL: str = "isCloseDeath: "
    

    def __init__(self, bufferedImage: list[BufferedImage], minX: int, maxX: int, y: int) -> None:
        __class__._java_defaults(self)
        super().__init__(bufferedImage, minX, maxX, y)
        __class__._init_fields(self)
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
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        commonSeps: CommonSeps = CommonSeps.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.HP_LABEL)
        stringBuffer.append(java_super_call(super(), "toString"))
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(self.IS_DAMAGED_LABEL)
        stringBuffer.appendboolean(java_predicate(self, "isDamaged"))
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(self.IS_CLOSE_DEATH_LABEL)
        stringBuffer.appendboolean(java_predicate(self, "isCloseDeath"))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from java.awt.image.BufferedImage import BufferedImage
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps



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
from org.allbinary.input.automation.module.game.MagicGameObjectInterface import MagicGameObjectInterface


class MagicGameObject(MeteredGameObject, MagicGameObjectInterface):

    def _init_fields(self) -> None:
        self.MP_LABEL: str = "MP:"
    

    def __init__(self, bufferedImage: list[BufferedImage], minX: int, maxX: int, y: int) -> None:
        super().__init__(bufferedImage, minX, maxX, y)
        self._init_fields()
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        stringBuffer.append(self.MP_LABEL)
        stringBuffer.append(str(super()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps



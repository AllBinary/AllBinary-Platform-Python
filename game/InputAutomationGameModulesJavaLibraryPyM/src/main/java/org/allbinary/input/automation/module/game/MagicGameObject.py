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
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.input.automation.module.game.MeteredGameObject import MeteredGameObject
from org.allbinary.input.automation.module.game.MagicGameObjectInterface import MagicGameObjectInterface


@java_inherited_overloads
class MagicGameObject(*java_bases(MeteredGameObject, MagicGameObjectInterface)):
    def _java_defaults(self):
        vars(self).setdefault("MP_LABEL", None)

    def _init_fields(self) -> None:
        self.MP_LABEL: str = "MP:"
    

    def __init__(self, bufferedImage: list[BufferedImage], minX: int, maxX: int, y: int) -> None:
        __class__._java_defaults(self)
        super().__init__(bufferedImage, minX, maxX, y)
        __class__._init_fields(self)
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
        stringBuffer.append(self.MP_LABEL)
        stringBuffer.append(java_super_call(super(), "toString"))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from java.awt.image.BufferedImage import BufferedImage
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps



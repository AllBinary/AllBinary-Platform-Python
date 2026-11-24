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
# package org.allbinary.game.paint.help

from __future__ import annotations



class UpdateMyFontProperties:

    def _init_fields(self) -> None:
        from org.allbinary.logic.NullUtil import NullUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.actionStringArray: list[str] = StringUtil.getInstance().getArrayInstance()
        self.keymappingBeginWidthArray: list[int] = NullUtil.getInstance().NULL_INT_ARRAY
        self.actionStringDeltaXArray: list[int] = NullUtil.getInstance().NULL_INT_ARRAY
        self.inputDeltaXArray: list[list[int]] = NullUtil.getInstance().NULL_INT_ARRAY_ARRAY
        self.sepArray: list[list[str]] = StringUtil.getInstance().ONE_EMPTY_STRING_ARRAY_OF_ARRAYS
        self.sepWidthArray: list[list[int]] = NullUtil.getInstance().NULL_INT_ARRAY_ARRAY
        self.charHeight: int = 0

    def __init__(self) -> None:
        self._init_fields()
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.string.StringUtil import StringUtil



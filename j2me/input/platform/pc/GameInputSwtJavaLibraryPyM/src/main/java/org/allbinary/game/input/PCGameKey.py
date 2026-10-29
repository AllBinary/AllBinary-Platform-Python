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

from org.allbinary.game.input.Input import Input


class PCGameKey(Input):
    

    def __init__(self, keyCode: int, name: str) -> None:
        from org.allbinary.game.input.InputFactory import InputFactory
        super().__init__(keyCode, name)
        id: int = self.getId()
        if id >= 0:
            InputFactory.getInstance().add(id, self)
    

    def toString(self) -> str:
        return "PCGameKey: " + str(super())

    def __str__(self) -> str:
        return self.toString()
    

    @staticmethod
    def getString(keyCode: int) -> str:
        from org.allbinary.game.input.InputFactory import InputFactory
        input: Input = InputFactory.getInstance().getInstanceById(keyCode)
        if input is not None:
            return input.getName()
        else:
            return StringUtil.getInstance().EMPTY_STRING
from org.allbinary.logic.string.StringUtil import StringUtil



# Generated Code Do Not Modify
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.game.input.Input import Input


class AndroidGameKey(Input):
    

    def __init__(self, keyCode: int, name: str) -> None:
        from org.allbinary.game.input.InputFactory import InputFactory
        super().__init__(keyCode, name)
        inputFactory: InputFactory = InputFactory.getInstance()
        inputFactory.inputIntegerArray[self.getId()] = self
    

    def toString(self) -> str:
        return "AndroidGameKey: " + str(super())

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



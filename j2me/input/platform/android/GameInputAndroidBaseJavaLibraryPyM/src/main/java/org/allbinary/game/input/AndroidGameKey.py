# Generated Code Do Not Modify
# package org.allbinary.game.input

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.input.Input import Input


@java_inherited_overloads
class AndroidGameKey(Input):
    

    def __init__(self, keyCode: int, name: str) -> None:
        from org.allbinary.game.input.InputFactory import InputFactory
        super().__init__(keyCode, name)
        inputFactory: InputFactory = InputFactory.getInstance()
        inputFactory.inputIntegerArray[self.getId()] = self
    

    def toString(self) -> str:
        return "AndroidGameKey: " + java_super_call(super(), "toString")

    def __str__(self) -> str:
        return self.toString()
    

    @staticmethod
    def getString(keyCode: int) -> str:
        from org.allbinary.game.input.InputFactory import InputFactory
        from org.allbinary.logic.string.StringUtil import StringUtil
        input: Input = InputFactory.getInstance().getInstanceById(keyCode)
        if input is not None:
            return input.getName()
        else:
            return StringUtil.getInstance().EMPTY_STRING
# from org.allbinary.logic.string.StringUtil import StringUtil



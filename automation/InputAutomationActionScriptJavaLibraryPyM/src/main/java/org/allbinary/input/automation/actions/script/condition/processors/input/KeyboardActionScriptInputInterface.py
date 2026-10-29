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
# package org.allbinary.input.automation.actions.script.condition.processors.input

from __future__ import annotations

from org.allbinary.input.automation.actions.script.condition.processors.input.ProfileActionScriptInputInterface import ProfileActionScriptInputInterface


# Java interface
class KeyboardActionScriptInputInterface(ProfileActionScriptInputInterface):
    

    def getDelayBetweenKeys(self) -> int:
        raise NotImplementedError()
    

    def getKeyArray(self) -> list[int]:
        raise NotImplementedError()
    

    def isPress(self) -> bool:
        raise NotImplementedError()
    

    def isRelease(self) -> bool:
        raise NotImplementedError()
    

    def isNormal(self) -> bool:
        raise NotImplementedError()
    

    def setPress(self, press: bool) -> None:
        raise NotImplementedError()
    

    def setRelease(self, release: bool) -> None:
        raise NotImplementedError()
    

    def setNormal(self) -> None:
        raise NotImplementedError()
    

    def getText(self) -> str:
        raise NotImplementedError()
    

    def setText(self, text: str) -> None:
        raise NotImplementedError()
    

    def log(self) -> None:
        raise NotImplementedError()



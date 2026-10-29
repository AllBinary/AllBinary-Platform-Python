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
class MouseActionScriptInputInterface(ProfileActionScriptInputInterface):
    

    def setPoint(self, point: Point) -> None:
        raise NotImplementedError()
    

    def getPoint(self) -> Point:
        raise NotImplementedError()
    

    def getButtonClicks(self) -> int:
        raise NotImplementedError()
    

    def setButtonClicks(self, buttons: int) -> None:
        raise NotImplementedError()
    

    def log(self) -> None:
        raise NotImplementedError()
# from java.awt import *



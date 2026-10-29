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

from org.allbinary.game.input.TestInputInterface import TestInputInterface


class TestInputExample(TestInputInterface):

    def _init_fields(self) -> None:
        self.testValue: int = 0

    def __init__(self) -> None:
        self._init_fields()
    

    def up(self) -> None:
        pass
    

    def down(self) -> None:
        pass
    

    def left(self) -> None:
        self.testValue += 1
    

    def right(self) -> None:
        self.testValue -= 1
    

    def strafeLeft(self) -> None:
        pass
    

    def strafeRight(self) -> None:
        pass
    

    def paint(self, graphics: Graphics) -> None:
        pass
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics



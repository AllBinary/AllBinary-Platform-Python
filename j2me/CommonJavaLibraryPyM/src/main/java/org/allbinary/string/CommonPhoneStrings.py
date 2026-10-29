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
# package org.allbinary.string

from __future__ import annotations



class CommonPhoneStrings:
    instance: CommonPhoneStrings = None

    def _init_fields(self) -> None:
        self.UP: str = "UP"
        self.DOWN: str = "DOWN"
        self.LEFT: str = "LEFT"
        self.RIGHT: str = "RIGHT"
        self.ZERO: str = "0"
        self.ONE: str = "1"
        self.TWO: str = "2"
        self.THREE: str = "3"
        self.FOUR: str = "4"
        self.FIVE: str = "5"
        self.SIX: str = "6"
        self.SEVEN: str = "7"
        self.EIGHT: str = "8"
        self.NINE: str = "9"
        self.POUND: str = "#"
        self.STAR: str = "*"
        self.FIRE: str = "FIRE"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CommonPhoneStrings:
        return CommonPhoneStrings.instance
from jsinterop.annotations.JsType import JsType


CommonPhoneStrings.instance = CommonPhoneStrings()


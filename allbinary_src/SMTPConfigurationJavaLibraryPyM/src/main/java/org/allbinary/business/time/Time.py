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
# package org.allbinary.business.time

from __future__ import annotations



class Time:

    def _init_fields(self) -> None:
        self.timeLong: int = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, time: str) -> None:
        self._init_fields()
        self.timeLong = int(time)
    

    def _constructor1(self, time: int) -> None:
        self._init_fields()
        self.timeLong = int(time)
    

    def getLong(self) -> int:
        return self.timeLong
    

    def getlong(self) -> int:
        return int(self.timeLong)
    

    def toString(self) -> str:
        return str(self.getLong())

    def __str__(self) -> str:
        return self.toString()



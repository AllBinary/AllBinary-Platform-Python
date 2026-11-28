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
        if "timeLong" not in vars(self): self.timeLong: int = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or isinstance(args[0], str)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor1_1(self, time: str) -> None:
        __class__._init_fields(self)
        self.timeLong = int(time)
    

    def _constructor1_2(self, time: int) -> None:
        __class__._init_fields(self)
        self.timeLong = int(time)
    

    def getLong(self) -> int:
        return self.timeLong
    

    def getlong(self) -> int:
        return int(self.timeLong)
    

    def toString(self) -> str:
        return str(self.getLong())

    def __str__(self) -> str:
        return self.toString()



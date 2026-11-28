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
# package org.allbinary.canvas

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.canvas.AndroidGameStatistics import AndroidGameStatistics


#ActualPlatform
@java_inherited_overloads
class GameStatisticsFactory(AndroidGameStatistics):
    SINGLETON: AndroidGameStatistics = None
    def _java_defaults(self):
        vars(self).setdefault("stringBuffer", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.stringBuffer: StringMaker = StringMaker()

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> AndroidGameStatistics:
        return GameStatisticsFactory.SINGLETON
    

    def add(self, string: str) -> None:
        if self.stringBuffer.length() > 12000:
            self.stringBuffer.delete(0, self.stringBuffer.length())
            self.stringBuffer.append("Old Stats Cleared")
        self.stringBuffer.append(string)
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        return str(StringMaker().append(java_super_call(super(), "toString")).append(str(self.stringBuffer)))

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.logic.string.StringMaker import StringMaker


def _GameStatisticsFactory_SINGLETON() -> object:
    return GameStatisticsFactory()

lazy_static(GameStatisticsFactory, "SINGLETON", _GameStatisticsFactory_SINGLETON)


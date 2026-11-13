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
# package org.allbinary.game.ag.ai

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class InputProbability:
    INPUT_PROBABILITY: int = None

    def _init_fields(self) -> None:
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.likelyhoodIntegerArray: list[list[int]] = None
        self.repeatLikelyhoodIntegerArray: list[int] = None
        self.max: int = None
        self.timeDelayHelper: TimeDelayHelper = None
    

    def __init__(self, likelyhoodIntegerArray: list[list[int]], repeatLikelyhoodIntegerArray: list[int], max: int, timeDelayHelper: TimeDelayHelper) -> None:
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self._init_fields()
        self.likelyhoodIntegerArray = likelyhoodIntegerArray
        self.repeatLikelyhoodIntegerArray = repeatLikelyhoodIntegerArray
        self.max = max
        self.timeDelayHelper = timeDelayHelper
    

    def getLikelyhoodIntegerArray(self) -> list[list[int]]:
        return self.likelyhoodIntegerArray
    

    def getRepeatLikelyhoodIntegerArray(self) -> list[int]:
        return self.repeatLikelyhoodIntegerArray
    

    def getMax(self) -> int:
        return self.max
    

    def getTimeDelayHelper(self) -> TimeDelayHelper:
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        return self.timeDelayHelper
    

    def toHashtable(self) -> ABHashtable[object, object]:
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.util.ABHashtable import ABHashtable
        hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        hashtable.put(InputProbability.INPUT_PROBABILITY, self)
        return hashtable
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
# from org.allbinary.util.ABHashtable import ABHashtable


def _InputProbability_INPUT_PROBABILITY() -> object:
    from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
    return SmallIntegerSingletonFactory.getInstance().getAt(0)

lazy_static(InputProbability, "INPUT_PROBABILITY", _InputProbability_INPUT_PROBABILITY)


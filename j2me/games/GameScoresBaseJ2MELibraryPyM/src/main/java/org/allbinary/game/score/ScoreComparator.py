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
# package org.allbinary.game.score

from __future__ import annotations

# from javax.microedition.rms.RecordComparator import RecordComparator


class ScoreComparator(RecordComparator):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.isHighestBest: bool = None
    

    def __init__(self, isHighestBest: bool) -> None:
        self._init_fields()
        self.isHighestBest = isHighestBest
    

    def getBestScore(self) -> int:
        return (9223372036854775807 if self.isHighestBest else 0)
    

    def compare(self, recordOne: list[int], recordTwo: list[int]) -> int:
        byteArrayInputStreamOne: ByteArrayInputStream = ByteArrayInputStream(recordOne)
        inputStreamOne: DataInputStream = DataInputStream(byteArrayInputStreamOne)
        byteArrayInputStreamTwo: ByteArrayInputStream = ByteArrayInputStream(recordTwo)
        inputStreamTwo: DataInputStream = DataInputStream(byteArrayInputStreamTwo)
        scoreOne: int = 0
        scoreTwo: int = 0
        try:
            inputStreamOne.readUTF()
            inputStreamTwo.readUTF()
            scoreOne = inputStreamOne.readLong()
            scoreTwo = inputStreamTwo.readLong()
        except EOFException as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "compare", e)
        except OSError as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "compare", e)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "compare", e)
        if self.isHighestBest:
            return self.getHighTooLow(scoreOne, scoreTwo)
        else:
            return self.getLowTooHigh(scoreOne, scoreTwo)
    

    def getHighTooLow(self, scoreOne: int, scoreTwo: int) -> int:
        if scoreOne > scoreTwo:
            return RecordComparator.PRECEDES
        elif scoreOne < scoreTwo:
            return RecordComparator.FOLLOWS
        else:
            return RecordComparator.EQUIVALENT
    

    def getLowTooHigh(self, scoreOne: int, scoreTwo: int) -> int:
        if scoreOne < scoreTwo:
            return RecordComparator.PRECEDES
        elif scoreOne > scoreTwo:
            return RecordComparator.FOLLOWS
        else:
            return RecordComparator.EQUIVALENT
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.io.DataInputStream import DataInputStream
# from java.io.EOFException import EOFException
# from java.io.IOException import IOException
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings



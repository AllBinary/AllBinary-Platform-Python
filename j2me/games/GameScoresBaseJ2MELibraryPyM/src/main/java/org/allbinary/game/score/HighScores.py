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

from org.allbinary.game.score.HighScoresInterface import HighScoresInterface


class HighScores(HighScoresInterface):

    def _init_fields(self) -> None:
        self.orderedHighScoresList: BasicArrayList = BasicArrayListD()
        self.name: str = None
        self.heading: str = None
        self.columnOneHeading: str = "Name"
        self.columnTwoHeading: str = None
    

    def __init__(self, name: str, heading: str, columnTwoHeading: str) -> None:
        self._init_fields()
        self.name = name
        self.heading = heading
        self.columnTwoHeading = columnTwoHeading
    

    def setList(self, orderedHighScoresList: BasicArrayList) -> None:
        self.orderedHighScoresList = orderedHighScoresList
    

    def getList(self) -> BasicArrayList:
        return self.orderedHighScoresList
    

    def getName(self) -> str:
        return self.name
    

    def getTotal(self) -> int:
        return self.getList().size()
    

    def addHighScore(self, newHighScore: HighScore) -> None:
        self.orderedHighScoresList.add(newHighScore)
    

    def getHeading(self) -> str:
        return self.heading
    

    def getColumnOneHeading(self) -> str:
        return self.columnOneHeading
    

    def getColumnTwoHeading(self) -> str:
        return self.columnTwoHeading
    

    # throws Exception
    def isBestScore(self, newHighScore: HighScore) -> bool:
        return False
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("HighScores: ")
        stringBuffer.append(self.heading)
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(CommonLabels.getInstance().TOTAL_LABEL)
        stringBuffer.appendint(self.orderedHighScoresList.size())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD



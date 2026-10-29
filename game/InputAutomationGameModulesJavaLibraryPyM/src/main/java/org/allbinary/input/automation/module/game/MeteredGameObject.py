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
# package org.allbinary.input.automation.module.game

from __future__ import annotations

from org.allbinary.input.automation.module.game.MeteredGameObjectInterface import MeteredGameObjectInterface


class MeteredGameObject(MeteredGameObjectInterface):

    def _init_fields(self) -> None:
        self.ratios: list[float] = None
        self.good: bool = False
        self.dropping: bool = False
        self.minX: int = None
        self.maxX: int = None
        self.y: int = None
        self.size: int = None
        self.RATIOS_LABEL: str = "Ratios: "
        self.IS_GOOD_LABEL: str = "isGood: "
        self.IS_DROPPPING_LABEL: str = "isDropping: "
    

    def __init__(self, bufferedImage: list[BufferedImage], minX: int, maxX: int, y: int) -> None:
        from org.allbinary.input.automation.module.game.GraphicsAnalysisUtil import GraphicsAnalysisUtil
        self._init_fields()
        self.setRatios([None] * (len(bufferedImage)))
        self.setMinX(minX)
        self.setMaxX(maxX)
        self.setY(y)
        self.setSize(maxX - minX)
        for index in range(0, len(bufferedImage)):
            nominator: float = GraphicsAnalysisUtil.getNominator(bufferedImage[index], self.getMinX(), self.getMaxX(), self.getY())
            self.getRatios()[index] = float(nominator / self.getSize())
        if float(self.getRatios()[len(bufferedImage) - 1]) > 0.93:
            self.setGood(True)
        else:
            self.setGood(False)
        if float(self.getRatios()[len(bufferedImage) - 1]) < float(self.getRatios()[0]):
            self.setDropping(True)
        else:
            self.setDropping(False)
    

    def isGood(self) -> bool:
        return self.good
    

    def setGood(self, good: bool) -> None:
        self.good = good
    

    def isDropping(self) -> bool:
        return self.dropping
    

    def setDropping(self, dropping: bool) -> None:
        self.dropping = dropping
    

    def getRatios(self) -> list[float]:
        return self.ratios
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(self.RATIOS_LABEL)
        for index in range(0, len(self.getRatios())):
            stringBuffer.append(str(self.getRatios()[index]))
            if index < len(self.getRatios()) - 1:
                stringBuffer.append(commonSeps.COMMA_SEP)
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(self.IS_GOOD_LABEL)
        stringBuffer.appendboolean(self.isGood())
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(self.IS_DROPPPING_LABEL)
        stringBuffer.appendboolean(self.isDropping())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def setRatios(self, ratios: list[float]) -> None:
        self.ratios = ratios
    

    def getMinX(self) -> int:
        return self.minX
    

    def setMinX(self, minX: int) -> None:
        self.minX = minX
    

    def getMaxX(self) -> int:
        return self.maxX
    

    def setMaxX(self, maxX: int) -> None:
        self.maxX = maxX
    

    def getY(self) -> int:
        return self.y
    

    def setY(self, y: int) -> None:
        self.y = y
    

    def getSize(self) -> int:
        return self.size
    

    def setSize(self, size: int) -> None:
        self.size = size
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps



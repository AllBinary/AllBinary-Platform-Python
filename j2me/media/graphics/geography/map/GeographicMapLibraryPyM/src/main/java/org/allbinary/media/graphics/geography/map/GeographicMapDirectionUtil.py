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
# package org.allbinary.media.graphics.geography.map

from __future__ import annotations



class GeographicMapDirectionUtil:
    instance: GeographicMapDirectionUtil = None

    def _init_fields(self) -> None:
        self.MESSAGE: str = "Cell Position should have been cached!!!"
        self.ERROR: str = "Error: "
        self.EQUAL: str = " == "
    

    @staticmethod
    def getInstance() -> GeographicMapDirectionUtil:
        return GeographicMapDirectionUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getDirectionFromCellPositionToAdjacentCellPosition(self, fromGeographicMapCellPosition: GeographicMapCellPosition, toGeographicMapCellPosition: GeographicMapCellPosition) -> Direction:
        fromColumn: int = fromGeographicMapCellPosition.getColumn()
        fromRow: int = fromGeographicMapCellPosition.getRow()
        goColumn: int = toGeographicMapCellPosition.getColumn()
        goRow: int = toGeographicMapCellPosition.getRow()
        directionFactory: DirectionFactory = DirectionFactory.getInstance()
        if fromColumn - 1 == goColumn:
            return directionFactory.LEFT
        elif fromColumn + 1 == goColumn:
            return directionFactory.RIGHT
        elif fromRow - 1 == goRow:
            return directionFactory.UP
        elif fromRow + 1 == goRow:
            return directionFactory.DOWN
        elif fromGeographicMapCellPosition == toGeographicMapCellPosition:
            return directionFactory.NO_DIRECTION
        elif fromRow == goRow and fromColumn == goColumn:
            raise Exception(self.MESSAGE)
        return directionFactory.NOT_BORDERED_WITH
    

    # throws Exception
    def getEightDirectionFromCellPositionToAdjacentCellPosition(self, fromGeographicMapCellPosition: GeographicMapCellPosition, toGeographicMapCellPosition: GeographicMapCellPosition) -> Direction:
        fromColumn: int = fromGeographicMapCellPosition.getColumn()
        fromRow: int = fromGeographicMapCellPosition.getRow()
        goColumn: int = toGeographicMapCellPosition.getColumn()
        goRow: int = toGeographicMapCellPosition.getRow()
        directionFactory: DirectionFactory = DirectionFactory.getInstance()
        if fromRow == goRow:
            if fromColumn - 1 == goColumn:
                return directionFactory.LEFT
            elif fromColumn + 1 == goColumn:
                return directionFactory.RIGHT
        elif fromRow - 1 == goRow:
            if fromColumn == goColumn:
                return directionFactory.UP
            if fromColumn - 1 == goColumn:
                return directionFactory.UP_LEFT
            elif fromColumn + 1 == goColumn:
                return directionFactory.UP_RIGHT
        elif fromRow + 1 == goRow:
            if fromColumn == goColumn:
                return directionFactory.DOWN
            if fromColumn - 1 == goColumn:
                return directionFactory.DOWN_LEFT
            elif fromColumn + 1 == goColumn:
                return directionFactory.DOWN_RIGHT
        elif fromGeographicMapCellPosition == toGeographicMapCellPosition:
            return directionFactory.NO_DIRECTION
        elif fromRow == goRow and fromColumn == goColumn:
            raise Exception(self.MESSAGE)
        return directionFactory.NOT_BORDERED_WITH
    

    # throws Exception
    def getDirectionFromCellPositionToCellPosition(self, fromGeographicMapCellPosition: GeographicMapCellPosition, toGeographicMapCellPosition: GeographicMapCellPosition) -> Direction:
        fromColumn: int = fromGeographicMapCellPosition.getColumn()
        fromRow: int = fromGeographicMapCellPosition.getRow()
        goColumn: int = toGeographicMapCellPosition.getColumn()
        goRow: int = toGeographicMapCellPosition.getRow()
        directionFactory: DirectionFactory = DirectionFactory.getInstance()
        if fromColumn > goColumn:
            return directionFactory.LEFT
        elif fromColumn < goColumn:
            return directionFactory.RIGHT
        elif fromRow > goRow:
            return directionFactory.UP
        elif fromRow < goRow:
            return directionFactory.DOWN
        stringMaker: StringMaker = StringMaker()
        string: str = str(stringMaker.append(CellPosition.toStringCellPosition(fromGeographicMapCellPosition)).append(" == ").append(CellPosition.toStringCellPosition(toGeographicMapCellPosition)))
        stringMaker.delete(0, stringMaker.length())
        raise Exception(str(stringMaker.append("Error: ").append(string)))
    

    # throws Exception
    def getEightDirectionFromCellPositionToCellPosition(self, fromGeographicMapCellPosition: GeographicMapCellPosition, toGeographicMapCellPosition: GeographicMapCellPosition) -> Direction:
        fromColumn: int = fromGeographicMapCellPosition.getColumn()
        fromRow: int = fromGeographicMapCellPosition.getRow()
        goColumn: int = toGeographicMapCellPosition.getColumn()
        goRow: int = toGeographicMapCellPosition.getRow()
        directionFactory: DirectionFactory = DirectionFactory.getInstance()
        if fromGeographicMapCellPosition == toGeographicMapCellPosition:
            return directionFactory.NO_DIRECTION
        elif fromRow == goRow:
            if fromColumn > goColumn:
                return directionFactory.LEFT
            elif fromColumn < goColumn:
                return directionFactory.RIGHT
        elif fromRow > goRow:
            if fromColumn > goColumn:
                return directionFactory.UP_LEFT
            elif fromColumn < goColumn:
                return directionFactory.UP_RIGHT
            elif fromColumn == goColumn:
                return directionFactory.UP
        elif fromRow < goRow:
            if fromColumn > goColumn:
                return directionFactory.DOWN_LEFT
            elif fromColumn < goColumn:
                return directionFactory.DOWN_RIGHT
            elif fromColumn == goColumn:
                return directionFactory.DOWN
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.ERROR)
        stringBuffer.append(CellPosition.toStringCellPosition(fromGeographicMapCellPosition))
        stringBuffer.append(self.EQUAL)
        stringBuffer.append(CellPosition.toStringCellPosition(toGeographicMapCellPosition))
        raise Exception(str(stringBuffer))
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.direction.Direction import Direction
from org.allbinary.direction.DirectionFactory import DirectionFactory
from org.allbinary.graphics.CellPosition import CellPosition


GeographicMapDirectionUtil.instance = GeographicMapDirectionUtil()


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
# package org.allbinary.direction

from __future__ import annotations



class DirectionUtil:
    instance: DirectionUtil = None

    def _init_fields(self) -> None:
        self.directionArray: list[Angle] = [None] * (10)
        self.directionArray2: list[Angle] = [None] * (10)
    

    @staticmethod
    def getInstance() -> DirectionUtil:
        return DirectionUtil.instance
    

    def __init__(self) -> None:
        from org.allbinary.direction.DirectionFactory import DirectionFactory
        self._init_fields()
        angleFactory: AngleFactory = AngleFactory.getInstance()
        directionFactory: DirectionFactory = DirectionFactory.getInstance()
        self.directionArray[directionFactory.LEFT.getValue()] = angleFactory.LEFT
        self.directionArray[directionFactory.RIGHT.getValue()] = angleFactory.RIGHT
        self.directionArray[directionFactory.UP.getValue()] = angleFactory.UP
        self.directionArray[directionFactory.DOWN.getValue()] = angleFactory.DOWN
        self.directionArray2[directionFactory.LEFT.getValue()] = angleFactory.LEFT
        self.directionArray2[directionFactory.RIGHT.getValue()] = angleFactory.RIGHT
        self.directionArray2[directionFactory.UP.getValue()] = angleFactory.UP
        self.directionArray2[directionFactory.DOWN.getValue()] = angleFactory.DOWN
    

    def getAngle(self, direction: Direction) -> Angle:
        return self.directionArray2[direction.getValue()]
    

    def getFrameAngle(self, direction: Direction) -> Angle:
        return self.directionArray[direction.getValue()]
from org.allbinary.math.Angle import Angle
from org.allbinary.math.AngleFactory import AngleFactory


DirectionUtil.instance = DirectionUtil()


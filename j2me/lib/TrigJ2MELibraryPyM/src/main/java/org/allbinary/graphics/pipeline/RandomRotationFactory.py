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
# package org.allbinary.graphics.pipeline

from __future__ import annotations



class RandomRotationFactory:
    instance: RandomRotationFactory = None

    def _init_fields(self) -> None:
        self.myRandomFactory: MyRandomFactory = MyRandomFactory.getInstance()
        self.angleFactory: AngleFactory = AngleFactory.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> RandomRotationFactory:
        return RandomRotationFactory.instance
    

    # throws Exception
    def getInstanceList(self, vector: BasicArrayList, howMuch: int) -> BasicArrayList:
        from org.allbinary.graphics.pipeline.BasicGraphicsPipeline import BasicGraphicsPipeline
        graphicsPipe: BasicGraphicsPipeline = BasicGraphicsPipeline(vector)
        graphicsPipe.createMatrix()
        graphicsPipe.rotateToAngle(self.angleFactory.getAt(self.getNextRandomAngle(howMuch)))
        return graphicsPipe.getMatrix()
    

    def getNextRandomAngle(self, howMuch: int) -> int:
        return self.myRandomFactory.getNextInt(howMuch * 10)
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.util.BasicArrayList import BasicArrayList


RandomRotationFactory.instance = RandomRotationFactory()


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
# package org.allbinary.animation

from __future__ import annotations



class VectorExplosionGenerator:
    instance: VectorExplosionGenerator = None

    def _init_fields(self) -> None:
        self.RANDOM: VectorExplosionType = VectorExplosionType()
        self.ROTATION: VectorExplosionType = VectorExplosionType()
        self.vectorAnimationUtil: VectorAnimationUtil = VectorAnimationUtil.getInstance()
        self.randomRotationFactory: RandomRotationFactory = RandomRotationFactory.getInstance()
    

    @staticmethod
    def getInstance() -> VectorExplosionGenerator:
        return VectorExplosionGenerator.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def createList(self, list_: BasicArrayList, howMuch: int, type_: VectorExplosionType) -> BasicArrayList:
        point: GPoint = None
        size: int = list_.size()
        points: list[list[int]] = [[0] * (2) for _ in range(size)]
        for index in range(0, size):
            point = list_.objectArray[index]
            points[index][0] = point.getX()
            points[index][1] = point.getY()
        return self.createListFromPoints(list_, points, howMuch, type_)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, points: list[list[int]], howMuch: int, type_: VectorExplosionType) -> list[list[list[int]]]:
        pointsBasicArrayList: BasicArrayList = self.getInstanceStartFrame(points, howMuch, type_, True)
        tempBasicArrayList: BasicArrayList = pointsBasicArrayList.objectArray[0]
        newPoints: list[list[list[int]]] = self.vectorAnimationUtil.toAnimationArrayFromListOfPointListWithPointsPerFrame(pointsBasicArrayList, tempBasicArrayList.size())
        return newPoints
    

    # throws Exception
    def getInstanceStartFrame(self, points: list[list[int]], howMuch: int, type_: VectorExplosionType, startFrame: bool) -> BasicArrayList:
        try:
            pointsBasicArrayList: BasicArrayList = BasicArrayListS(howMuch)
            pointsBasicArrayList.add(self.createPointsBasicArrayList(points))
            frameIndex: int = 0
            tempBasicArrayList: BasicArrayList = None
            pointBasicArrayList: BasicArrayList = None
            while frameIndex < howMuch:
                tempBasicArrayList = pointsBasicArrayList.objectArray[frameIndex]
                pointBasicArrayList = self.createListFromPoints(tempBasicArrayList, points, howMuch, type_)
                pointsBasicArrayList.add(pointBasicArrayList)
                frameIndex += 1
            if not startFrame:
                pointsBasicArrayList.removeAt(0)
            return pointsBasicArrayList
        except Exception as e:
            raise e
    

    # throws Exception
    def createListFromPoints(self, tempBasicArrayList: BasicArrayList, points: list[list[int]], howMuch: int, type_: VectorExplosionType) -> BasicArrayList:
        index: int = 0
        pointBasicArrayList: BasicArrayList = BasicArrayListD()
        sectionBasicArrayList: BasicArrayList = None
        while index < len(points):
            sectionBasicArrayList = BasicArrayListD()
            while points[index][0] != 1000:
                sectionBasicArrayList.add(tempBasicArrayList.objectArray[index])
                index += 1
                if index >= len(points):
                    break
            sectionBasicArrayList = RandomTranslation.getInstance(sectionBasicArrayList, howMuch)
            if type_ == self.ROTATION:
                sectionBasicArrayList = self.randomRotationFactory.getInstanceList(sectionBasicArrayList, howMuch)
            size: int = sectionBasicArrayList.size()
            for index2 in range(0, size):
                pointBasicArrayList.add(sectionBasicArrayList.objectArray[index2])
            if index >= len(points):
                break
            elif points[index][0] == 1000:
                pointBasicArrayList.add(tempBasicArrayList.objectArray[index])
                index += 1
        return pointBasicArrayList
    

    # throws Exception
    def createPointsBasicArrayList(self, points: list[list[int]]) -> BasicArrayList:
        if len(points) == 0:
            raise Exception("Not Points Provided")
        firstPointBasicArrayList: BasicArrayList = BasicArrayListS(len(points))
        pointFactory: PointFactory = PointFactory.getInstance()
        for index in range(0, len(points)):
            firstPointBasicArrayList.add(pointFactory.createXY(points[index][0], points[index][1]))
        return firstPointBasicArrayList
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.pipeline.RandomRotationFactory import RandomRotationFactory
from org.allbinary.graphics.pipeline.RandomTranslation import RandomTranslation
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListS import BasicArrayListS
from org.allbinary.animation.VectorExplosionType import VectorExplosionType
from org.allbinary.animation.VectorAnimationUtil import VectorAnimationUtil


VectorExplosionGenerator.instance = VectorExplosionGenerator()


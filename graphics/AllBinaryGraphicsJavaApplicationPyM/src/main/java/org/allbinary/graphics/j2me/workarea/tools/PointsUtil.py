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
# package org.allbinary.graphics.j2me.workarea.tools

from __future__ import annotations



class PointsUtil:
    instance: PointsUtil = None
    

    @staticmethod
    def getInstance() -> PointsUtil:
        return PointsUtil.instance
    

    # throws Exception
    def doTransforms(self, pointVector: BasicArrayList, angle: float, fulcrumPoint: GPoint) -> BasicArrayList:
        return VectorRotationGenerator.getInstance().getListAtAngle(fulcrumPoint.getX(), fulcrumPoint.getY(), pointVector, AngleFactory.getInstance().getAt(int(angle)))
from org.allbinary.animation.VectorRotationGenerator import VectorRotationGenerator
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.math.AngleFactory import AngleFactory
from org.allbinary.util.BasicArrayList import BasicArrayList


PointsUtil.instance = PointsUtil()


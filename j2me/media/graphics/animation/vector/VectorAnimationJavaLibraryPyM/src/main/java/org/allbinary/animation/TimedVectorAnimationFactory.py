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

from org.allbinary.animation.VectorAnimationFactoryInterface import VectorAnimationFactoryInterface


class TimedVectorAnimationFactory(VectorAnimationFactoryInterface):
    

    def getInstance(self, points: list[list[list[int]]], basicColor: BasicColor) -> VectorAnimation:
        from org.allbinary.animation.TimedVectorAnimation import TimedVectorAnimation
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        return TimedVectorAnimation(points, basicColor, AnimationBehavior.getInstance())
from org.allbinary.graphics.color.BasicColor import BasicColor



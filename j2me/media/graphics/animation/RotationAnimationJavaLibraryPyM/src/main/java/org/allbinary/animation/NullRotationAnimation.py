# Generated Code Do Not Modify
# package org.allbinary.animation

from __future__ import annotations

from org.allbinary.animation.RotationAnimation import RotationAnimation


class NullRotationAnimation(RotationAnimation):
    

    @staticmethod
    def createTotalAngle(angleInfo: AngleInfo, totalAngle: int, animationBehavior: AnimationBehavior) -> NullRotationAnimation:
        from org.allbinary.math.AngleInfo import AngleInfo
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        return NullRotationAnimation(angleInfo, CircularIndexUtil.createInstance(totalAngle / angleInfo.getAngleIncrementInfo().getAngleIncrement()), animationBehavior)
    

    @staticmethod
    def createQuarter(animationBehavior: AnimationBehavior) -> NullRotationAnimation:
        from org.allbinary.math.AngleFactory import AngleFactory
        from org.allbinary.math.AngleInfo import AngleInfo
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        return NullRotationAnimation(AngleInfo.getInstance(AngleFactory.getInstance().QUARTER_TOTAL_ANGLE), CircularIndexUtil.createInstance(4), animationBehavior)
    

    def __init__(self, angleInfo: AngleInfo, circularIndexUtil: CircularIndexUtil, animationBehavior: AnimationBehavior) -> None:
        from org.allbinary.math.AngleInfo import AngleInfo
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        super().__init__(angleInfo, circularIndexUtil, animationBehavior)
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return 0
# from org.allbinary.math.AngleFactory import AngleFactory
# from org.allbinary.math.AngleInfo import AngleInfo
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil



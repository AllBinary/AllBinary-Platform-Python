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
# package org.allbinary.animation.vector

from __future__ import annotations

from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface


class LineAnimationFactory(AnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.basicColor: BasicColor = None
    

    def __init__(self, basicColor: BasicColor) -> None:
        self._init_fields()
        self.basicColor = basicColor
    

    # throws Exception
    def getInstance(self, instanceId: int) -> Animation:
        from org.allbinary.animation.vector.LineAnimation import LineAnimation
        return LineAnimation(self.basicColor)
    

    def setInitialScale(self, scaleProperties: ScaleProperties) -> None:
        pass
from org.allbinary.animation.Animation import Animation
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.media.ScaleProperties import ScaleProperties



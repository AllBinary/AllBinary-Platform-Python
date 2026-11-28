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
# package org.allbinary.animation.image

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from org.allbinary.animation.RotationAnimation import RotationAnimation


@java_inherited_overloads
class ImageBaseRotationAnimation(RotationAnimation):
    def _java_defaults(self):
        vars(self).setdefault("image", None)
        vars(self).setdefault("anchor", 0)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.Anchor import Anchor
        if "image" not in vars(self): self.image: Image = None
        self.anchor: int = Anchor.TOP_LEFT
    

    def __init__(self, image: Image, angleInfo: AngleInfo, totalAngle: int, animationBehavior: AnimationBehavior) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.math.AngleInfo import AngleInfo
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        super().__init__(angleInfo, CircularIndexUtil.createInstance(java_divide(totalAngle, angleInfo.getAngleIncrementInfo().getAngleIncrement())), animationBehavior)
        __class__._init_fields(self)
        self.image = image
    

    # throws Exception
    def getAnimationSize(self) -> int:
        return self.getSize()
    

    def setSequence(self, sequence: list[int]) -> None:
        pass
    

    def getSequence(self) -> list[int]:
        from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
        return PrimitiveIntUtil.getArrayInstance()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        graphics.drawImage(self.image, x, y, self.anchor)
    

    def getImage(self) -> Image:
        from javax.microedition.lcdui.Image import Image
        return self.image
    

    def getWidth(self) -> int:
        return self.image.getWidth()
    

    def getHeight(self) -> int:
        return self.image.getHeight()
    

    # throws Exception
    def close(self) -> None:
        from org.allbinary.DisposalUtil import DisposalUtil
        DisposalUtil.getInstance().disposeImage(self.image)
    

    # throws Throwable
    def finalize(self) -> None:
        from org.allbinary.DisposalUtil import DisposalUtil
        DisposalUtil.getInstance().disposeImage(self.image)
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.DisposalUtil import DisposalUtil
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.graphics.Anchor import Anchor
# from org.allbinary.logic.math.PrimitiveIntUtil import PrimitiveIntUtil
# from org.allbinary.math.AngleInfo import AngleInfo
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil



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
# package org.allbinary.game.layer.pickup

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactoryBase import PickedUpLayerInterfaceFactoryBase


@java_inherited_overloads
class PickedUpLayerInterfaceFactory(PickedUpLayerInterfaceFactoryBase):
    def _java_defaults(self):
        vars(self).setdefault("pickedUpLayerType", None)
        vars(self).setdefault("iconLayer", None)
        vars(self).setdefault("animationInterface", None)

    def _init_fields(self) -> None:
        if "pickedUpLayerType" not in vars(self): self.pickedUpLayerType: PickedUpLayerType = None
        if "iconLayer" not in vars(self): self.iconLayer: IconLayer = None
        if "animationInterface" not in vars(self): self.animationInterface: Animation = None
    

    def __init__(self, pickeUpLayerType: PickedUpLayerType, iconLayer: IconLayer, animationInterface: Animation) -> None:
        __class__._java_defaults(self)
        from org.allbinary.animation.Animation import Animation
        super().__init__()
        __class__._init_fields(self)
        self.pickedUpLayerType = pickeUpLayerType
        self.animationInterface = animationInterface
        self.iconLayer = iconLayer
    

    def getIconLayer(self) -> AllBinaryLayer:
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        return self.iconLayer
    

    def getAnimationInterface(self) -> Animation:
        from org.allbinary.animation.Animation import Animation
        return self.animationInterface
    

    def getPickedUpLayerType(self) -> PickedUpLayerType:
        return self.pickedUpLayerType
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer



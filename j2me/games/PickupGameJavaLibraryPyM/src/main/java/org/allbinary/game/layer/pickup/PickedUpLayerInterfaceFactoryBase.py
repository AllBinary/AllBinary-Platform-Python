# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactoryInterface import PickedUpLayerInterfaceFactoryInterface


class PickedUpLayerInterfaceFactoryBase(PickedUpLayerInterfaceFactoryInterface):
    NULL_PICKED_UP_LAYER_FACTORY_BASE: PickedUpLayerInterfaceFactoryBase = None
    

    def getIconLayer(self) -> AllBinaryLayer:
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        raise RuntimeError()
    

    def getAnimationInterface(self) -> Animation:
        from org.allbinary.animation.Animation import Animation
        raise RuntimeError()
    

    def getPickedUpLayerType(self) -> PickedUpLayerType:
        raise RuntimeError()
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


def _PickedUpLayerInterfaceFactoryBase_NULL_PICKED_UP_LAYER_FACTORY_BASE() -> object:
    return PickedUpLayerInterfaceFactoryBase()

lazy_static(PickedUpLayerInterfaceFactoryBase, "NULL_PICKED_UP_LAYER_FACTORY_BASE", _PickedUpLayerInterfaceFactoryBase_NULL_PICKED_UP_LAYER_FACTORY_BASE)


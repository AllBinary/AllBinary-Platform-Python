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



class IconLayerFactory:
    

    # throws Exception
    @staticmethod
    def getInstance(animationInterface: Animation, width: int, height: int) -> IconLayer:
        from org.allbinary.game.layer.pickup.IconLayer import IconLayer
        return IconLayer(animationInterface, width, height)
from org.allbinary.animation.Animation import Animation



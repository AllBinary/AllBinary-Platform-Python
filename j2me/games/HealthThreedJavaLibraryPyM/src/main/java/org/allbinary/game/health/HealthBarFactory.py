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
# package org.allbinary.game.health

from __future__ import annotations



class HealthBarFactory:
    

    # throws Exception
    def getInstance(self, layerInterface: AllBinaryLayer, healthInterface: Health, location: int, direction: int) -> HealthBar:
        from org.allbinary.game.health.HealthBar import HealthBar
        from org.allbinary.game.health.HealthBarTwodAnimation import HealthBarTwodAnimation
        from org.allbinary.game.health.Health import Health
        from org.allbinary.game.health.HealthBar import HealthBar
        if OpenGLFeatureUtil.getInstance().isAnyThreed():
            featuredAnimationInterfaceFactoryInterfaceFactory: FeaturedAnimationInterfaceFactoryInterfaceFactory = FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance()
            healthBarAnimationInterfaceFactory: HealthBarAnimationInterfaceFactory = featuredAnimationInterfaceFactoryInterfaceFactory.get(Health.NAME)
            return HealthBar(layerInterface, healthInterface, healthBarAnimationInterfaceFactory.getInstanceByLocation(layerInterface, location), direction)
        else:
            return HealthBar(layerInterface, healthInterface, HealthBarTwodAnimation(layerInterface, location), direction)
from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer



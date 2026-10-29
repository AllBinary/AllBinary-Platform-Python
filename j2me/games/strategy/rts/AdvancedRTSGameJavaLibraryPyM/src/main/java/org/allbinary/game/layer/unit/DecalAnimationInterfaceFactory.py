# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer.unit

from __future__ import annotations



class DecalAnimationInterfaceFactory:
    instance: DecalAnimationInterfaceFactory = None
    

    @staticmethod
    def getInstance() -> DecalAnimationInterfaceFactory:
        return DecalAnimationInterfaceFactory.instance
    

    # throws Exception
    def getAnimationFactory(self, basicGameResources: BasicGameResources, basicColor: BasicColor) -> AnimationInterfaceFactoryInterface:
        animationInterfaceFactoryInterface: AnimationInterfaceFactoryInterface = None
        if basicColor == BasicColorFactory.getInstance().RED:
            animationInterfaceFactoryInterface = FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().get(basicGameResources.RESOURCE)
        else:
            animationInterfaceFactoryInterface = NullRotationAnimationFactory.getFactoryInstance()
        return animationInterfaceFactoryInterface
from org.allbinary.game.layer.resources.BasicGameResources import BasicGameResources
from org.allbinary.animation.AnimationInterfaceFactoryInterface import AnimationInterfaceFactoryInterface
from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.animation.NullRotationAnimationFactory import NullRotationAnimationFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory


DecalAnimationInterfaceFactory.instance = DecalAnimationInterfaceFactory()


# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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

from java.lang.JavaRuntimeStatic import lazy_static


class AnimationBehaviorFactory:
    instance: AnimationBehaviorFactory = None
    

    @staticmethod
    def getInstance() -> AnimationBehaviorFactory:
        return AnimationBehaviorFactory.instance
    

    def getOrCreateInstance(self) -> AnimationBehavior:
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        return AnimationBehavior.getInstance()


def _AnimationBehaviorFactory_instance() -> object:
    return AnimationBehaviorFactory()

lazy_static(AnimationBehaviorFactory, "instance", _AnimationBehaviorFactory_instance)


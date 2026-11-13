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
# package org.allbinary.input.motion.gesture.configuration

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class MotionGestureConfigurationFactory:
    config: MotionGestureConfiguration = None
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> MotionGestureConfiguration:
        return MotionGestureConfigurationFactory.config


def _MotionGestureConfigurationFactory_config() -> object:
    from org.allbinary.input.motion.gesture.configuration.MotionGestureConfiguration import MotionGestureConfiguration
    return MotionGestureConfiguration()

lazy_static(MotionGestureConfigurationFactory, "config", _MotionGestureConfigurationFactory_config)


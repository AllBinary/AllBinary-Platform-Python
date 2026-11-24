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
# package org.allbinary.game.layer

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class SensorActionFactory:
    instance: SensorActionFactory = None

    def _init_fields(self) -> None:
        self.ATTACK: SensorAction = SensorAction("Attack")
        self.EVADE: SensorAction = SensorAction("Evade")
    

    @staticmethod
    def getInstance() -> SensorActionFactory:
        return SensorActionFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
from org.allbinary.game.layer.SensorAction import SensorAction


def _SensorActionFactory_instance() -> object:
    return SensorActionFactory()

lazy_static(SensorActionFactory, "instance", _SensorActionFactory_instance)


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
# package org.allbinary

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class ThreedResources:
    threedResources: ThreedResources = None
    

    @staticmethod
    def getThreedResources() -> ThreedResources:
        return ThreedResources.threedResources
    

    def add(self) -> None:
        pass


def _ThreedResources_threedResources() -> object:
    return ThreedResources()

lazy_static(ThreedResources, "threedResources", _ThreedResources_threedResources)


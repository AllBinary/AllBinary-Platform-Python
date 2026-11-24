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
# package org.allbinary.graphics.opengles.shader

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class ModelViewProjection:
    instance: ModelViewProjection = None
    

    @staticmethod
    def getInstance() -> ModelViewProjection:
        return ModelViewProjection.instance
    

    def get(self) -> list[float]:
        return None


def _ModelViewProjection_instance() -> object:
    return ModelViewProjection()

lazy_static(ModelViewProjection, "instance", _ModelViewProjection_instance)


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


class ShaderManagerFactory:
    instance: ShaderManagerFactory = None
    

    @staticmethod
    def getInstance() -> ShaderManagerFactory:
        return ShaderManagerFactory.instance
    

    def create(self) -> ShaderManager:
        from org.allbinary.graphics.opengles.shader.ShaderManager import ShaderManager
        return ShaderManager.getInstance()


def _ShaderManagerFactory_instance() -> object:
    return ShaderManagerFactory()

lazy_static(ShaderManagerFactory, "instance", _ShaderManagerFactory_instance)


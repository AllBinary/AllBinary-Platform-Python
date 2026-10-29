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
# package org.allbinary.graphics

from __future__ import annotations



class RendererStateFactory:
    instance: RendererStateFactory = None

    def _init_fields(self) -> None:
        self.loaded: bool = False
        self.surfaceChanged: bool = False

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> RendererStateFactory:
        return RendererStateFactory.instance
    

    def setLoaded(self, loaded: bool) -> None:
        self.loaded = loaded
    

    def isLoaded(self) -> bool:
        return self.loaded
    

    def setSurfaceChanged(self, initialized: bool) -> None:
        self.surfaceChanged = initialized
    

    def isSurfaceChanged(self) -> bool:
        return self.surfaceChanged


RendererStateFactory.instance = RendererStateFactory()


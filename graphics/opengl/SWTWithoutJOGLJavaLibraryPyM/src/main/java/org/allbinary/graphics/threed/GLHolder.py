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
# package org.allbinary.graphics.threed

from __future__ import annotations



class GLHolder:

    def _init_fields(self) -> None:
        self.isCreated: bool = True
    

    def __init__(self) -> None:
        self._init_fields()
    

    def runOnSurfaceCreated(self, renderer: object) -> None:
        pass
    

    def runOnSurfaceChanged(self, renderer: object, width: int, height: int) -> None:
        pass
    

    def run(self, renderer: object) -> None:
        pass



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
# package org.allbinary.graphics

from __future__ import annotations



class GraphicsStrings:
    instance: GraphicsStrings = None

    def _init_fields(self) -> None:
        self.ANIMATION: str = "animation"
        self.ANGLE: str = "angle"
        self.MOVEMENT_ANGLE: str = "movement_angle"
        self.ROTATION: str = "rotation"
        self.OPACITY: str = "opacity"
        self.HTML: str = "HTML"
        self.WIDTH: str = "width"
        self.HEIGHT: str = "height"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> GraphicsStrings:
        return GraphicsStrings.instance


GraphicsStrings.instance = GraphicsStrings()


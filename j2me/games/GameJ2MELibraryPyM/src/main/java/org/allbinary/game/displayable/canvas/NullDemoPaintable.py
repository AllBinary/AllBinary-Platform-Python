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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.displayable.canvas.DemoPaintableInterface import DemoPaintableInterface


class NullDemoPaintable(DemoPaintableInterface):
    NULL_DEMO_PAINTABLE: NullDemoPaintable = None
    

    def showGamePaintable(self) -> None:
        pass


def _NullDemoPaintable_NULL_DEMO_PAINTABLE() -> object:
    return NullDemoPaintable()

lazy_static(NullDemoPaintable, "NULL_DEMO_PAINTABLE", _NullDemoPaintable_NULL_DEMO_PAINTABLE)


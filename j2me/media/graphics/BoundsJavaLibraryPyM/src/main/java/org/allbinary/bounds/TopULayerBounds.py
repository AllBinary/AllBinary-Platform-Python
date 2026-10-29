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
# package org.allbinary.bounds

from __future__ import annotations

from org.allbinary.bounds.LayerBounds import LayerBounds


class TopULayerBounds(LayerBounds):
    

    def __init__(self, rectangle: Rectangle) -> None:
        super().__init__(rectangle)
    

    def visit(self, boundsVisitorInterface: BoundsVisitorInterface) -> None:
        if boundsVisitorInterface.getX() > self.rectangle.getMaxX():
            boundsVisitorInterface.maxX()
        if boundsVisitorInterface.getX() < self.rectangle.getPoint().getX():
            boundsVisitorInterface.minX()
        if boundsVisitorInterface.getY() < self.rectangle.getPoint().getY():
            boundsVisitorInterface.minY()
from org.allbinary.graphics.Rectangle import Rectangle



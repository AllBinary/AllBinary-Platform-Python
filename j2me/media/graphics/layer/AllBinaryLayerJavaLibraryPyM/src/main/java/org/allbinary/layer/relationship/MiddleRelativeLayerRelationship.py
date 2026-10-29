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
# package org.allbinary.layer.relationship

from __future__ import annotations

from org.allbinary.layer.relationship.RelativeLayerRelationship import RelativeLayerRelationship


class MiddleRelativeLayerRelationship(RelativeLayerRelationship):
    

    def __init__(self, layer: AllBinaryLayer) -> None:
        super().__init__(layer, PointFactory.getInstance().createXY(layer.getHalfWidth(), layer.getHalfHeight()), BasicArrayListUtil.getInstance().getImmutableInstance())
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil



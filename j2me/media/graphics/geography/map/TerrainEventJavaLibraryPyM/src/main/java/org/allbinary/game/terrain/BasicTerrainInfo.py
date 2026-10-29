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
# package org.allbinary.game.terrain

from __future__ import annotations

from org.allbinary.math.AngleFactory import AngleFactory


class BasicTerrainInfo:
    NULL_BASIC_TERRAIN_INFO: BasicTerrainInfo = None

    def _init_fields(self) -> None:
        self.angle: Angle = None
    

    def __init__(self, angle: Angle) -> None:
        self._init_fields()
        self.angle = angle
    

    def getAngle(self) -> Angle:
        return self.angle
    

    def setAngle(self, angle: Angle) -> None:
        self.angle = angle
from org.allbinary.math.Angle import Angle


BasicTerrainInfo.NULL_BASIC_TERRAIN_INFO = BasicTerrainInfo(AngleFactory.getInstance().NOT_ANGLE)


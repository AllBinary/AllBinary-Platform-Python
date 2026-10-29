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
# package org.allbinary.game.layer

from __future__ import annotations



class VehicleProperties:

    def _init_fields(self) -> None:
        self.velocityProperties: VelocityProperties = None
        self.vehicleFrictionProperties: VehicleFrictionProperties = None
    

    def __init__(self, velocityProperties: VelocityProperties, vehicleFrictionProperties: VehicleFrictionProperties) -> None:
        self._init_fields()
        self.velocityProperties = velocityProperties
        self.vehicleFrictionProperties = vehicleFrictionProperties
    

    def getVehicleFrictionProperties(self) -> VehicleFrictionProperties:
        return self.vehicleFrictionProperties
    

    def setVehicleFrictionProperties(self, vehicleFrictionProperties: VehicleFrictionProperties) -> None:
        self.vehicleFrictionProperties = vehicleFrictionProperties
    

    def getVelocityProperties(self) -> VelocityProperties:
        return self.velocityProperties
from org.allbinary.game.physics.velocity.VelocityProperties import VelocityProperties



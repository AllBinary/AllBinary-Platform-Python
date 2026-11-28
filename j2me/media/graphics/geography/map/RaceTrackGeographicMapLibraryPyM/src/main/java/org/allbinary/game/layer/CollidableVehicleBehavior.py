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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.layer.special.CollidableDestroyableDamageableBehavior import CollidableDestroyableDamageableBehavior


@java_inherited_overloads
class CollidableVehicleBehavior(CollidableDestroyableDamageableBehavior):
    def _java_defaults(self):
        vars(self).setdefault("totalImpactVelocity", 0)
        vars(self).setdefault("halfImpactVelocityX", 0)
        vars(self).setdefault("halfImpactVelocityY", 0)

    def _init_fields(self) -> None:
        self.totalImpactVelocity: int = 0
        if "halfImpactVelocityX" not in vars(self): self.halfImpactVelocityX: int = 0
        if "halfImpactVelocityY" not in vars(self): self.halfImpactVelocityY: int = 0
    

    def __init__(self, collidable: bool) -> None:
        __class__._java_defaults(self)
        super().__init__(collidable)
        __class__._init_fields(self)
    

    # throws Exception
    def collide(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableCompositeLayer) -> None:
        from org.allbinary.game.layer.pickup.PickedUpLayerInterface import PickedUpLayerInterface
        from org.allbinary.game.collision.CollisionType import CollisionType
        from org.allbinary.game.collision.CollisionTypeFactory import CollisionTypeFactory
        from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
        collisionTypeFactory: CollisionTypeFactory = CollisionTypeFactory.getInstance()
        collisionType: CollisionType = collidableInterfaceCompositeInterface.getCollidableInferface().getCollisionTypeWith(ownerLayer)
        if collisionType == collisionTypeFactory.PICKUP:
            collidableDestroyableDamageableLayer: CollidableDestroyableDamageableLayer = (ownerLayer)
            collidableDestroyableDamageableLayer.getPickupBehavior().doPickupLayer(collidableInterfaceCompositeInterface)
        elif collisionType == collisionTypeFactory.COLLISION:
            java_super_call(super(), "collide", ownerLayer, collidableInterfaceCompositeInterface)
        else:
            self.collideVehicle(ownerLayer, collidableInterfaceCompositeInterface)
    

    def collideInterface(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface) -> None:
        from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
        from org.allbinary.game.collision.CollidableInterfaceCompositeInterface import CollidableInterfaceCompositeInterface
        ForcedLogUtil.log("Don't Use Interface Version It Is Slower", self)
    

    def collideVehicle(self, ownerLayer: CollidableCompositeLayer, vehiclePropertiesCompositeInterface: VehiclePropertiesCompositeInterface) -> None:
        ownerVehicleLayerInterface: VehiclePropertiesCompositeInterface = (ownerLayer)
        ownerVehicleProperties: VehicleProperties = ownerVehicleLayerInterface.getVehicleProperties()
        vehicleProperties: VehicleProperties = vehiclePropertiesCompositeInterface.getVehicleProperties()
        impactVelocityX: int = ownerVehicleProperties.getVelocityProperties().getVelocityXBasicDecimalP().getUnscaled() - vehicleProperties.getVelocityProperties().getVelocityXBasicDecimalP().getUnscaled()
        impactVelocityY: int = ownerVehicleProperties.getVelocityProperties().getVelocityYBasicDecimalP().getUnscaled() - vehicleProperties.getVelocityProperties().getVelocityYBasicDecimalP().getUnscaled()
        if impactVelocityX != 0:
            self.halfImpactVelocityX = (int(impactVelocityX) >> (int(1) & 63))
            ownerVehicleProperties.getVelocityProperties().getVelocityXBasicDecimalP().addlong(self.halfImpactVelocityX)
            vehicleProperties.getVelocityProperties().getVelocityXBasicDecimalP().addlong(self.halfImpactVelocityX)
        else:
            pass
        if impactVelocityY != 0:
            self.halfImpactVelocityY = (int(impactVelocityY) >> (int(1) & 63))
            ownerVehicleProperties.getVelocityProperties().getVelocityYBasicDecimalP().addlong(self.halfImpactVelocityY)
            vehicleProperties.getVelocityProperties().getVelocityXBasicDecimalP().addlong(self.halfImpactVelocityY)
        else:
            pass
        self.collideFriction(ownerVehicleLayerInterface)
        self.collideFriction(vehiclePropertiesCompositeInterface)
        self.totalImpactVelocity = impactVelocityX + impactVelocityY
    

    def collideFriction(self, vehiclePropertiesCompositeInterface: VehiclePropertiesCompositeInterface) -> None:
        vehicleFrictionProperties: VehicleFrictionProperties = vehiclePropertiesCompositeInterface.getVehicleProperties().getVehicleFrictionProperties()
        vehiclePropertiesCompositeInterface.getVehicleProperties().getVehicleFrictionProperties().friction(vehiclePropertiesCompositeInterface.getVehicleProperties().getVelocityProperties(), vehicleFrictionProperties.getCrashFrictionNominator())
# from org.allbinary.game.layer.pickup.PickedUpLayerInterface import PickedUpLayerInterface
# from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
# from org.allbinary.game.collision.CollidableInterfaceCompositeInterface import CollidableInterfaceCompositeInterface
# from org.allbinary.game.collision.CollisionType import CollisionType
# from org.allbinary.game.collision.CollisionTypeFactory import CollisionTypeFactory
# from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer



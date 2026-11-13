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
# package org.allbinary.game.collision

from __future__ import annotations

from org.allbinary.game.collision.CollidableInterface import CollidableInterface


class CollidableBaseBehavior(CollidableInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.layerCollisionUtil: LayerCollisionUtil = LayerCollisionUtil.getInstance()
        self.collidable: bool = True
    

    def __init__(self, collidable: bool) -> None:
        self._init_fields()
        self.collidable = collidable
    

    def update(self) -> None:
        pass
    

    def getName(self) -> str:
        return type(self).__module__ + "." + type(self).__qualname__
    

    def setCollidable(self, collidable: bool) -> None:
        self.collidable = collidable
    

    def isCollidable(self, ownerLayer: CollidableCompositeLayer) -> bool:
        from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
        return self.collidable
    

    # throws Exception
    def collide(self, ownerLayer: CollidableCompositeLayer, allbinaryCollidableLayer: CollidableCompositeLayer) -> None:
        from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonLabels import CommonLabels
        raise Exception(str(StringMaker().append(self.commonStrings.NOT_IMPLEMENTED).append(CommonLabels.getInstance().COLON_SEP).append(type(self).__module__ + "." + type(self).__qualname__)))
    

    def isCollision(self, ownerLayer: CollidableCompositeLayer, collisionLayer: CollidableCompositeLayer) -> bool:
        from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
        return self.layerCollisionUtil.isCollision(ownerLayer, collisionLayer)
    

    def isCollisionInterface(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface) -> bool:
        from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        return self.layerCollisionUtil.isCollision(ownerLayer, collidableInterfaceCompositeInterface)
    

    # throws Exception
    def collideInterface(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableInterfaceCompositeInterface) -> None:
        from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    def paint(self, ownerLayer: CollidableCompositeLayer, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
        pass
    

    def getCollisionTypeWith(self, layerInterface: AllBinaryLayer) -> CollisionType:
        from org.allbinary.game.collision.CollisionTypeFactory import CollisionTypeFactory
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        return CollisionTypeFactory.getInstance().NONE
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.game.collision.LayerCollisionUtil import LayerCollisionUtil



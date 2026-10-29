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
# package org.allbinary.game.layer.special

from __future__ import annotations

from org.allbinary.game.combat.damage.DamageableInterface import DamageableInterface
from org.allbinary.game.combat.destroy.DestroyableInterface import DestroyableInterface
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.game.layer.pickup.PickupCompositeInterface import PickupCompositeInterface
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.game.layer.special.SpecialGameInputInterface import SpecialGameInputInterface


class CollidableDestroyableDamageableLayer(CollidableCompositeLayer, DestroyableInterface, DamageableInterface, PickupCompositeInterface, SpecialGameInputInterface):
    NULL_COLLIDABLE_DESTROYABLE_DAMAGE_LAYER: object = NullUtil.getInstance().NULL_OBJECT
    READYFOREXPLOSION: str = "ReadyForExplosion: "

    def _init_fields(self) -> None:
        self.groupInterface: list[Group] = None
        self.readyForExplosion: bool = False
        self.initWidth: int = None
        self.initHeight: int = None
        self.initX: int = 0
        self.initY: int = 0
        self.initZ: int = 0
        self.partInterfaceArrayP: list[PartInterface] = PartInterfaceUtil.getZeroArray()
        self.pickupBehavior: PickupBehavior = None
        self.allBinaryGameLayerManagerP: AllBinaryGameLayerManager = AllBinaryGameLayerManager.getNullInstance()
        self.isDraggable: bool = False
        self.isDragged: bool = False
        self.isDropped: bool = False
    

    @staticmethod
    def getNullInstance() -> CollidableDestroyableDamageableLayer:
        if CollidableDestroyableDamageableLayer.NULL_COLLIDABLE_DESTROYABLE_DAMAGE_LAYER == NullUtil.getInstance().NULL_OBJECT:
            CollidableDestroyableDamageableLayer.NULL_COLLIDABLE_DESTROYABLE_DAMAGE_LAYER = CollidableDestroyableDamageableLayer(BasicGroupFactory.getInstance().NONE_ARRAY, StringUtil.getInstance().EMPTY_STRING, RectangleFactory.SINGLETON, ViewPositionBase.NULL_VIEW_POSITION)
        return CollidableDestroyableDamageableLayer.NULL_COLLIDABLE_DESTROYABLE_DAMAGE_LAYER
    

    def __init__(self, groupInterface: list[Group], name: str, layerInfo: Rectangle, viewPosition: ViewPositionBase) -> None:
        super().__init__(name, layerInfo, viewPosition, CollidableNeverCollideBehaviorFactory.getInstance())
        self._init_fields()
        self.initWidth = layerInfo.getWidth()
        self.initHeight = layerInfo.getHeight()
        self.groupInterface = groupInterface
        self.pickupBehavior = PickupBehavior.getNullInstance()
    

    # throws Exception
    def initPosition(self) -> None:
        self.setPosition(self.initX, self.initY, self.initZ)
    

    # throws Exception
    def initPositionXYZ(self, x: int, y: int, z: int) -> None:
        self.initX = x
        self.initY = y
        self.initZ = z
    

    def paint(self, graphics: Graphics) -> None:
        super().paint(graphics)
    

    # throws Exception
    def damage(self, damage: int, damageType: int) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def getDamage(self, damageType: int) -> int:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    def isDestroyed(self) -> bool:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    def getGroupInterface(self) -> list[Group]:
        return self.groupInterface
    

    def setGroupInterface(self, teamInterface: list[Group]) -> None:
        self.groupInterface = teamInterface
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        self.allBinaryGameLayerManagerP = allBinaryGameLayerManager
        if self.allBinaryGameLayerManagerP is None:
            raise RuntimeError()
    

    def isReadyForExplosion(self) -> bool:
        return self.readyForExplosion
    

    def setReadyForExplosion(self, isReadyForExplosion: bool) -> None:
        self.readyForExplosion = isReadyForExplosion
    

    def getInitWidth(self) -> int:
        return self.initWidth
    

    def getInitHeight(self) -> int:
        return self.initHeight
    

    def getInitX(self) -> int:
        return self.initX
    

    def getInitY(self) -> int:
        return self.initY
    

    # throws Exception
    def up(self) -> None:
        pass
    

    # throws Exception
    def down(self) -> None:
        pass
    

    # throws Exception
    def right(self) -> None:
        pass
    

    # throws Exception
    def left(self) -> None:
        pass
    

    # throws Exception
    def strafeLeft(self) -> None:
        pass
    

    # throws Exception
    def strafeRight(self) -> None:
        pass
    

    # throws Exception
    def fire(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    # throws Exception
    def special1(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    # throws Exception
    def special2(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    # throws Exception
    def special3(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    # throws Exception
    def special4(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    # throws Exception
    def special5(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
        pass
    

    # throws Exception
    def upAnalog(self, yAnalogValue: int) -> None:
        pass
    

    # throws Exception
    def downAnalog(self, yAnalogValue: int) -> None:
        pass
    

    # throws Exception
    def rightAnalog(self, xAnalogValue: int) -> None:
        pass
    

    # throws Exception
    def leftAnalog(self, xAnalogValue: int) -> None:
        pass
    

    # throws Exception
    def rightTrigger(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent, xAnalogValue: int) -> None:
        pass
    

    # throws Exception
    def leftTrigger(self, layerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent, xAnalogValue: int) -> None:
        pass
    

    def onDestroyed(self, destroyedEvent: DestroyedEvent) -> None:
        pass
    

    def getPickupBehavior(self) -> PickupBehavior:
        return self.pickupBehavior
    

    def setPickupBehavior(self, pickupBehavior: PickupBehavior) -> None:
        self.pickupBehavior = pickupBehavior
    

    # throws Exception
    def addPart(self, pickedUpLayerInterfaceFactoryInterface: PickedUpLayerInterfaceFactoryInterface) -> None:
        pass
    

    def setPartInterfaceArray(self, partInterfaceArray: list[PartInterface]) -> None:
        self.partInterfaceArrayP = partInterfaceArray
    

    def getPartInterfaceArray(self) -> list[PartInterface]:
        return self.partInterfaceArrayP
    

    def toStringAppend(self, stringBuffer: StringMaker) -> None:
        commonSeps: CommonSeps = CommonSeps.getInstance()
        positionStrings: PositionStrings = PositionStrings.getInstance()
        super().toStringAppend(stringBuffer)
        stringBuffer.append(commonSeps.NEW_LINE)
        groupInterfaceArray: list[Group] = self.getGroupInterface()
        size: int = len(groupInterfaceArray)
        for index in range(0, size):
            stringBuffer.append(str(groupInterfaceArray[index]))
            stringBuffer.append(commonSeps.COMMA)
        pickupBehavior: PickupBehavior = self.getPickupBehavior()
        if pickupBehavior is not None:
            stringBuffer.append(commonSeps.NEW_LINE)
            stringBuffer.append(str(pickupBehavior))
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(CollidableDestroyableDamageableLayer.READYFOREXPLOSION)
        stringBuffer.appendboolean(self.readyForExplosion)
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(self.commonStrings.INIT)
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(positionStrings.X_LABEL)
        stringBuffer.appendint(self.initX)
        stringBuffer.append(positionStrings.Y_LABEL)
        stringBuffer.appendint(self.initX)
        stringBuffer.append(positionStrings.Z_LABEL)
        stringBuffer.appendint(self.initZ)
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        self.toStringAppend(stringBuffer)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.collision.CollidableNeverCollideBehaviorFactory import CollidableNeverCollideBehaviorFactory
from org.allbinary.game.combat.destroy.event.DestroyedEvent import DestroyedEvent
from org.allbinary.game.identification.BasicGroupFactory import BasicGroupFactory
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.game.layer.pickup.PickedUpLayerInterfaceFactoryInterface import PickedUpLayerInterfaceFactoryInterface
from org.allbinary.game.layer.pickup.PickupBehavior import PickupBehavior
from org.allbinary.game.part.PartInterface import PartInterface
from org.allbinary.game.part.PartInterfaceUtil import PartInterfaceUtil
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.RectangleFactory import RectangleFactory
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.view.ViewPositionBase import ViewPositionBase



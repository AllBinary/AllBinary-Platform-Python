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

from org.allbinary.game.collision.CollidableInterfaceCompositeInterface import CollidableInterfaceCompositeInterface
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer


class CollidableCompositeLayer(AllBinaryGameLayer, CollidableInterfaceCompositeInterface):
    NULL_COLLIDABLE_COMPOSITE_LAYER: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.collidableInferface: CollidableBaseBehavior = CollidableNeverCollideBehaviorFactory.getInstance().createBehavior()
    

    @staticmethod
    def getNullInstance() -> CollidableCompositeLayer:
        if CollidableCompositeLayer.NULL_COLLIDABLE_COMPOSITE_LAYER == NullUtil.getInstance().NULL_OBJECT:
            CollidableCompositeLayer.NULL_COLLIDABLE_COMPOSITE_LAYER = CollidableCompositeLayer(StringUtil.getInstance().EMPTY_STRING, RectangleFactory.SINGLETON, ViewPositionBase.NULL_VIEW_POSITION, CollidableNeverCollideBehaviorFactory.getInstance())
        return CollidableCompositeLayer.NULL_COLLIDABLE_COMPOSITE_LAYER
    

    def __init__(self, name: str, layerInfo: Rectangle, viewPosition: ViewPositionBase, collidableBaseBehaviorFactory: CollidableBaseBehaviorFactory) -> None:
        super().__init__(name, layerInfo, viewPosition)
        self._init_fields()
        if collidableBaseBehaviorFactory != CollidableNeverCollideBehaviorFactory.getInstance():
            self.setCollidableInferface(collidableBaseBehaviorFactory.createBehavior())
    

    def getArtificialIntelligenceInterface(self) -> ArtificialIntelligenceInterface:
        ForcedLogUtil.log(self.commonStrings.NOT_IMPLEMENTED, self)
        return ArtificialIntelligence.getInstance()
    

    def getCollidableInferface(self) -> CollidableBaseBehavior:
        return self.collidableInferface
    

    def setCollidableInferface(self, collidableInferface: CollidableBaseBehavior) -> None:
        self.collidableInferface = collidableInferface
    

    def implmentsCollidableInterface(self) -> bool:
        return True
    

    def toStringAppend(self, stringBuffer: StringMaker) -> None:
        commonSeps: CommonSeps = CommonSeps.getInstance()
        super().toStringAppend(stringBuffer)
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append(str(self.getCollidableInferface()))
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        self.toStringAppend(stringBuffer)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.ai.ArtificialIntelligence import ArtificialIntelligence
from org.allbinary.ai.ArtificialIntelligenceInterface import ArtificialIntelligenceInterface
from org.allbinary.game.collision.CollidableBaseBehavior import CollidableBaseBehavior
from org.allbinary.game.collision.CollidableBaseBehaviorFactory import CollidableBaseBehaviorFactory
from org.allbinary.game.collision.CollidableNeverCollideBehaviorFactory import CollidableNeverCollideBehaviorFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.RectangleFactory import RectangleFactory
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.view.ViewPositionBase import ViewPositionBase



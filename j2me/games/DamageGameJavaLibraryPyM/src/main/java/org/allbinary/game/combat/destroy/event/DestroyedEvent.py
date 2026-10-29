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
# package org.allbinary.game.combat.destroy.event

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class DestroyedEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.allBinaryGameCanvas: AllBinaryGameCanvas = NullGameCanvas.getInstance()
        self.allBinaryLayerInterface: AllBinaryLayer = AllBinaryLayer.NULL_ALLBINARY_LAYER
    

    def __init__(self, combatGameCanvas: AllBinaryGameCanvas) -> None:
        from org.allbinary.game.combat.destroy.event.DestroyedEventHandler import DestroyedEventHandler
        super().__init__(DestroyedEventHandler.getInstance())
        self._init_fields()
        self.setAllBinaryGameCanvas(combatGameCanvas)
    

    def getAllBinaryGameCanvas(self) -> AllBinaryGameCanvas:
        return self.allBinaryGameCanvas
    

    def getLayerInterface(self) -> AllBinaryLayer:
        return self.allBinaryLayerInterface
    

    def setAllBinaryGameCanvas(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        self.allBinaryGameCanvas = allBinaryGameCanvas
    

    def setLayerInterfaceForCircularStaticPool(self, allBinaryLayerInterface: AllBinaryLayer) -> None:
        self.allBinaryLayerInterface = allBinaryLayerInterface
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("DestroyedEvent: \n")
        stringBuffer.append("AllBinaryLayerInterface: ")
        stringBuffer.append(str(self.allBinaryLayerInterface))
        stringBuffer.append("\nAllBinaryGameCanvas: ")
        stringBuffer.append(StringUtil.getInstance().toString(self.getAllBinaryGameCanvas()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.game.displayable.canvas.NullGameCanvas import NullGameCanvas
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil



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

from org.allbinary.logic.util.event.AllBinaryEventObjectFactoryInterface import AllBinaryEventObjectFactoryInterface


class DestroyEventFactory(AllBinaryEventObjectFactoryInterface):

    def _init_fields(self) -> None:
        self.combatGameCanvas: AllBinaryGameCanvas = None
    

    def __init__(self, combatGameCanvas: AllBinaryGameCanvas) -> None:
        self._init_fields()
        self.combatGameCanvas = combatGameCanvas
    

    def getInstance(self) -> AllBinaryEventObject:
        from org.allbinary.game.combat.destroy.event.DestroyedEvent import DestroyedEvent
        return DestroyedEvent(self.combatGameCanvas)
from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject



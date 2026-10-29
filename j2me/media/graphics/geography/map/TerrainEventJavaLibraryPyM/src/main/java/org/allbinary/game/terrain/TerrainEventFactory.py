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

from org.allbinary.logic.util.event.AllBinaryEventObjectFactoryInterface import AllBinaryEventObjectFactoryInterface


class TerrainEventFactory(AllBinaryEventObjectFactoryInterface):
    

    def __init__(self) -> None:
        pass
    

    def getInstance(self) -> AllBinaryEventObject:
        from org.allbinary.game.terrain.TerrainEvent import TerrainEvent
        return TerrainEvent(NullUtil.getInstance().NULL_OBJECT)
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject



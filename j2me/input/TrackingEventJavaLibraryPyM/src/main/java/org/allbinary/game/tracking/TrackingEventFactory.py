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
# package org.allbinary.game.tracking

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObjectFactoryInterface import AllBinaryEventObjectFactoryInterface


class TrackingEventFactory(AllBinaryEventObjectFactoryInterface):
    

    def __init__(self) -> None:
        pass
    

    def getInstance(self) -> AllBinaryEventObject:
        from org.allbinary.game.tracking.TrackingEvent import TrackingEvent
        from org.allbinary.game.tracking.TrackingEventHandler import TrackingEventHandler
        return TrackingEvent(TrackingEventHandler.getInstance())
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject



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
# package org.allbinary.media.graphics.geography.map.event

from __future__ import annotations



class GeographicMapCellPositionEventUtil:

    def _init_fields(self) -> None:
        self.geographicMapCellPositionEvent: GeographicMapCellPositionEvent = None
        self.geographicMapCellPositionEventHandler: GeographicMapCellPositionEventHandler = GeographicMapCellPositionEventHandler.getInstance()
    

    def __init__(self, anyType: object) -> None:
        from org.allbinary.media.graphics.geography.map.event.GeographicMapCellPositionEvent import GeographicMapCellPositionEvent
        self._init_fields()
        self.geographicMapCellPositionEvent = GeographicMapCellPositionEvent(anyType, CellPositionFactory.getInstance().NONE)
    

    # throws Exception
    def update(self, geographicMapCellPositionTracking: GeographicMapCellPositionTracking) -> None:
        self.geographicMapCellPositionEvent.setGeographicMapCellPosition(geographicMapCellPositionTracking.getCurrentGeographicMapCellPosition())
        self.geographicMapCellPositionEventHandler.fireEvent(self.geographicMapCellPositionEvent)
    

    # throws Exception
    def remove(self, geographicMapCellPositionTracking: GeographicMapCellPositionTracking) -> None:
        self.geographicMapCellPositionEvent.setGeographicMapCellPosition(geographicMapCellPositionTracking.getCurrentGeographicMapCellPosition())
        self.geographicMapCellPositionEventHandler.fireRemoveEvent(self.geographicMapCellPositionEvent)
from org.allbinary.graphics.CellPositionFactory import CellPositionFactory
from org.allbinary.media.graphics.geography.map.GeographicMapCellPositionTracking import GeographicMapCellPositionTracking
from org.allbinary.media.graphics.geography.map.event.GeographicMapCellPositionEventHandler import GeographicMapCellPositionEventHandler



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
# package org.allbinary.bounds

from __future__ import annotations

from org.allbinary.bounds.event.BoundsChangeEventListener import BoundsChangeEventListener


class LayerBounds(BoundsChangeEventListener):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.rectangle: Rectangle = None
    

    def __init__(self, rectangle: Rectangle) -> None:
        self._init_fields()
        self.rectangle = rectangle
    

    def getRectangleP(self) -> Rectangle:
        return self.rectangle
    

    def visit(self, boundsVisitorInterface: BoundsVisitorInterface) -> None:
        pass
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onBoundsChangeEvent(self, boundsChangeEvent: BoundsChangeEvent) -> None:
        self.rectangle = boundsChangeEvent.getRectangle()
from org.allbinary.bounds.event.BoundsChangeEvent import BoundsChangeEvent
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings



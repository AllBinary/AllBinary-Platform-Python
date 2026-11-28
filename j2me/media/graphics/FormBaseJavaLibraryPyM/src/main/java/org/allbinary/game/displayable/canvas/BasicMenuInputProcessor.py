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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.input.PlayerGameInput import PlayerGameInput
from org.allbinary.input.motion.gesture.observer.BaseMotionGestureEventListener import BaseMotionGestureEventListener


@java_inherited_overloads
class BasicMenuInputProcessor(*java_bases(PlayerGameInput, BaseMotionGestureEventListener)):
    def _java_defaults(self):
        vars(self).setdefault("motionGestureEventList", None)
        vars(self).setdefault("canvas", None)

    def _init_fields(self) -> None:
        from javax.microedition.lcdui.NullCanvas import NullCanvas
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.motionGestureEventList: BasicArrayList = BasicArrayListD()
        self.canvas: Canvas = NullCanvas.NULL_CANVAS
    

    def __init__(self, gameKeyEventList: BasicArrayList, playerInputId: int, gameCanvas: Canvas) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Canvas import Canvas
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        super().__init__(gameKeyEventList, BasicArrayListD(), playerInputId)
        __class__._init_fields(self)
        self.canvas = gameCanvas
    

    def onMotionGestureEvent(self, motionGestureEvent: MotionGestureEvent) -> None:
        from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
        self.motionGestureEventList.add(motionGestureEvent)
    

    def onScrolledMotionGestureEvent(self, motionGestureEvent: MotionGestureEvent) -> None:
        from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
        pass
    

    def setCanvas(self, canvas: MyCanvas) -> None:
        from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
        self.canvas = canvas
    

    def getCanvas(self) -> MyCanvas:
        from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
        return self.canvas
    

    # throws Exception
    def processInputList(self) -> int:
        return -1
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.NullCanvas import NullCanvas
# from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
# from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD



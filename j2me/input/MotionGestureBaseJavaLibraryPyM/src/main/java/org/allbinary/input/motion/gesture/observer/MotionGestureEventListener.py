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
# package org.allbinary.input.motion.gesture.observer

from __future__ import annotations

from org.allbinary.input.motion.gesture.observer.BaseMotionGestureEventListener import BaseMotionGestureEventListener


# Java interface
class MotionGestureEventListener(BaseMotionGestureEventListener):
    

    def onPressedMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        raise NotImplementedError()
    

    def onUpMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        raise NotImplementedError()
    

    def onDownMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        raise NotImplementedError()
    

    def onLeftMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        raise NotImplementedError()
    

    def onRightMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        raise NotImplementedError()
    

    def onDiagonalDownRightMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        raise NotImplementedError()
    

    def onDiagonalDownLeftMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        raise NotImplementedError()
    

    def onDiagonalUpRightMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        raise NotImplementedError()
    

    def onDiagonalUpLeftMotionGestureEvent(self, ev: MotionGestureEvent) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def released(self, ev: MotionGestureEvent) -> None:
        raise NotImplementedError()



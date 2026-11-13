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
# package org.allbinary.input.motion.gesture

from __future__ import annotations



class MotionGestureToMotionGestureActionAssociation:

    def _init_fields(self) -> None:
        from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.list_: BasicArrayList = None
        self.motionGestureAction: CompleteMotionGestureInputEvent = None
    

    def __init__(self, list_: BasicArrayList, commandAction: CompleteMotionGestureInputEvent) -> None:
        from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self._init_fields()
        self.list_ = list_
        self.motionGestureAction = commandAction
    

    def getMotionGesture(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.list_
    

    def setMotionGestures(self, list_: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.list_ = list_
    

    def getCommandAction(self) -> CompleteMotionGestureInputEvent:
        from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
        return self.motionGestureAction
    

    def setMotionGestureAction(self, commandAction: CompleteMotionGestureInputEvent) -> None:
        from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
        self.motionGestureAction = commandAction
    

    def isMotionGestureArrayEquals(self, aList: BasicArrayList) -> bool:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        size: int = aList.size()
        if self.list_.size() != size:
            return False
        for i in range(size - 1, 0 - 1, -1):
            if aList.objectArray[i] != self.list_.objectArray[i]:
                return False
        return True
# from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
# from org.allbinary.util.BasicArrayList import BasicArrayList



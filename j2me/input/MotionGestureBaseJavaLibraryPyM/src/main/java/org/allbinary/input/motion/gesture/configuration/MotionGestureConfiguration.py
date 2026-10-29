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
# package org.allbinary.input.motion.gesture.configuration

from __future__ import annotations



class MotionGestureConfiguration:

    def _init_fields(self) -> None:
        self.diagonalMotionGestureAllowed: bool = True
        self.diagonalTolerance: int = 7
        self.minimumMotionGesture: int = 9
        self.button: str = StringUtil.getInstance().EMPTY_STRING
        self.color: BasicColor = BasicColorFactory.getInstance().BLUE
        self.executingActions: bool = True
        self.mouseButtonMask: int = 0
        self.activeCommands: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def addMotionGestureAction(self, list_: BasicArrayList, commandAction: CompleteMotionGestureInputEvent) -> None:
        self.activeCommands.add(MotionGestureToMotionGestureActionAssociation(list_, commandAction))
    

    def clearMotionGestureAction(self) -> None:
        self.activeCommands.clear()
    

    def getAssociateCommandActionsList(self) -> BasicArrayList:
        return self.activeCommands
    

    def isDiagonalMotionGestureAllowed(self) -> bool:
        return self.diagonalMotionGestureAllowed
    

    def isExecutingActionsAllowed(self) -> bool:
        return self.executingActions
    

    def setExecutingActionsAllowed(self, executingActionAllowed: bool) -> None:
        self.executingActions = executingActionAllowed
    

    def setDiagonalMotionGestureAllowed(self, diagonalMotionGestureAllowed: bool) -> None:
        self.diagonalMotionGestureAllowed = diagonalMotionGestureAllowed
    

    def getDiagonalTolerance(self) -> int:
        return self.diagonalTolerance
    

    def setDiagonalTolerance(self, diagonalTolerance: int) -> None:
        self.diagonalTolerance = diagonalTolerance
    

    def getMinimumMotionGesture(self) -> int:
        return self.minimumMotionGesture
    

    def setMinimumMotionGesture(self, minimumMotionGesture: int) -> None:
        self.minimumMotionGesture = minimumMotionGesture
    

    def getButton(self) -> str:
        return self.button
    

    def setButton(self, button: str) -> None:
        self.button = button
    

    def getColor(self) -> BasicColor:
        return self.color
    

    def setColor(self, color: BasicColor) -> None:
        self.color = color
    

    def getMouseButtonMask(self) -> int:
        return self.mouseButtonMask
    

    def setMouseButtonMask(self, mouseButtonMask: int) -> None:
        self.mouseButtonMask = mouseButtonMask
from org.allbinary.game.input.CompleteMotionGestureInputEvent import CompleteMotionGestureInputEvent
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.input.motion.gesture.MotionGestureToMotionGestureActionAssociation import MotionGestureToMotionGestureActionAssociation
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD



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

from org.allbinary.game.displayable.canvas.CommandFormInputProcessor import CommandFormInputProcessor


class PopupCommandFormInputProcessor(CommandFormInputProcessor):
    

    def __init__(self, gameKeyEventList: BasicArrayList, playerInputId: int, gameCanvas: MyCanvas, form: ScrollSelectionForm, popupMenuInputProcessor: PopupMenuInputProcessor) -> None:
        super().__init__(gameKeyEventList, playerInputId, gameCanvas, form)
    

    # throws Exception
    def processInput(self, key: int) -> int:
        return super().processInput(key)
    

    # throws Exception
    def processMotionInput(self, motionGestureEvent: MotionGestureEvent) -> None:
        super().processMotionInput(motionGestureEvent)
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
from org.allbinary.util.BasicArrayList import BasicArrayList



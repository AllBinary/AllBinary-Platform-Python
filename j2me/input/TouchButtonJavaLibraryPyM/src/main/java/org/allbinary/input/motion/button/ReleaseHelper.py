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
# package org.allbinary.input.motion.button

from __future__ import annotations



class ReleaseHelper:

    def _init_fields(self) -> None:
        self.touchButtonRecognizer: TouchButtonRecognizer = None
    

    def __init__(self, touchButtonRecognizer: TouchButtonRecognizer) -> None:
        self._init_fields()
        self.touchButtonRecognizer = touchButtonRecognizer
    

    # throws Exception
    def release(self, touchButtonInput: TouchButtonInput, deviceId: int) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        nextTouchButtonInput: TouchButtonInput = None
        gameKeyEvent: GameKeyEvent = None
        for index in range(self.touchButtonRecognizer.currentlyPressedTouchButtonSingleton.size() - 1, 0 - 1, -1):
            nextTouchButtonInput = self.touchButtonRecognizer.currentlyPressedTouchButtonSingleton.get(index)
            gameKeyEvent = nextTouchButtonInput.getGameKeyEvent()
            self.touchButtonRecognizer.upGameKeyEventHandler.fireEvent(gameKeyEvent)
            self.touchButtonRecognizer.upGameKeyEventHandler.getInstanceForDevice(deviceId).fireEvent(gameKeyEvent)
            self.touchButtonRecognizer.currentlyPressedTouchButtonSingleton.removeAt(index)
# from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent



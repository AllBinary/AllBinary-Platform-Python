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



class GameEventHandlerUtil:
    

    @staticmethod
    def removeAllListeners() -> None:
        BasicMotionGesturesHandler.getInstance().removeAllListeners()
        GameKeyEventHandler.getInstance().removeAllListeners()
        GameInputMotionEventProcessorFactory.getInstance().addListener()
from org.allbinary.android.input.motion.GameInputMotionEventProcessorFactory import GameInputMotionEventProcessorFactory
from org.allbinary.game.input.event.GameKeyEventHandler import GameKeyEventHandler
from org.allbinary.input.motion.gesture.observer.BasicMotionGesturesHandler import BasicMotionGesturesHandler



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



class MotionGestureReceiveInterfaceFactory:
    

    @staticmethod
    def getInstance() -> CompleteMotionGestureListenerInterface:
        from org.allbinary.input.motion.gesture.observer.ResolveCompleteMotionGestureListener import ResolveCompleteMotionGestureListener
        from org.allbinary.input.motion.gesture.observer.NullCompleteMotionGestureReceiver import NullCompleteMotionGestureReceiver
        configuration: MotionGestureConfiguration = MotionGestureConfigurationFactory.getInstance()
        if not configuration.isExecutingActionsAllowed():
            return NullCompleteMotionGestureReceiver()
        else:
            return ResolveCompleteMotionGestureListener()
from org.allbinary.input.motion.gesture.configuration.MotionGestureConfiguration import MotionGestureConfiguration
from org.allbinary.input.motion.gesture.configuration.MotionGestureConfigurationFactory import MotionGestureConfigurationFactory



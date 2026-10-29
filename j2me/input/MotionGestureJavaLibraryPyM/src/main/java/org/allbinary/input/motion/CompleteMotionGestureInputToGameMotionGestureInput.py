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
# package org.allbinary.input.motion

from __future__ import annotations



class CompleteMotionGestureInputToGameMotionGestureInput:
    instance: CompleteMotionGestureInputToGameMotionGestureInput = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CompleteMotionGestureInputToGameMotionGestureInput:
        return CompleteMotionGestureInputToGameMotionGestureInput.instance
    

    def init(self) -> None:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            PreLogUtil.put("Compound Motion Gestures", self, commonStrings.INIT)
            motionGestureConfiguration: MotionGestureConfiguration = MotionGestureConfigurationFactory.getInstance()
            touchMotionGestureFactory: TouchMotionGestureFactory = TouchMotionGestureFactory.getInstance()
            list_: BasicArrayList = BasicArrayListD()
            list_.add(touchMotionGestureFactory.DIAGONAL_DOWN_LEFT)
            motionGestureConfiguration.addMotionGestureAction(list_, DiagonalDownLeftTouchInputToGameKeyEventAction.getInstance())
            list_ = BasicArrayListD()
            list_.add(touchMotionGestureFactory.DIAGONAL_DOWN_RIGHT)
            motionGestureConfiguration.addMotionGestureAction(list_, DiagonalDownRightTouchInputToGameKeyEventAction.getInstance())
            list_ = BasicArrayListD()
            list_.add(touchMotionGestureFactory.DIAGONAL_UP_LEFT)
            motionGestureConfiguration.addMotionGestureAction(list_, DiagonalUpLeftTouchInputToGameKeyEventAction.getInstance())
            list_ = BasicArrayListD()
            list_.add(touchMotionGestureFactory.DIAGONAL_UP_RIGHT)
            motionGestureConfiguration.addMotionGestureAction(list_, DiagonalUpRightTouchInputToGameKeyEventAction.getInstance())
            list_ = BasicArrayListD()
            list_.add(touchMotionGestureFactory.LEFT)
            motionGestureConfiguration.addMotionGestureAction(list_, LeftTouchInputToGameKeyEventAction.getInstance())
            list_ = BasicArrayListD()
            list_.add(touchMotionGestureFactory.RIGHT)
            motionGestureConfiguration.addMotionGestureAction(list_, RightTouchInputToGameKeyEventAction.getInstance())
            list_ = BasicArrayListD()
            list_.add(touchMotionGestureFactory.DOWN)
            motionGestureConfiguration.addMotionGestureAction(list_, DownTouchInputToGameKeyEventAction.getInstance())
            list_ = BasicArrayListD()
            list_.add(touchMotionGestureFactory.UP)
            motionGestureConfiguration.addMotionGestureAction(list_, UpTouchInputToGameKeyEventAction.getInstance())
            list_ = BasicArrayListD()
            list_.add(touchMotionGestureFactory.RELEASED)
            motionGestureConfiguration.addMotionGestureAction(list_, ReleaseTouchInputToGameKeyEventAction.getInstance())
        except Exception as e:
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.INIT, e)
from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
from org.allbinary.input.motion.gesture.configuration.MotionGestureConfiguration import MotionGestureConfiguration
from org.allbinary.input.motion.gesture.configuration.MotionGestureConfigurationFactory import MotionGestureConfigurationFactory
from org.allbinary.input.motion.touch.action.DiagonalDownLeftTouchInputToGameKeyEventAction import DiagonalDownLeftTouchInputToGameKeyEventAction
from org.allbinary.input.motion.touch.action.DiagonalDownRightTouchInputToGameKeyEventAction import DiagonalDownRightTouchInputToGameKeyEventAction
from org.allbinary.input.motion.touch.action.DiagonalUpLeftTouchInputToGameKeyEventAction import DiagonalUpLeftTouchInputToGameKeyEventAction
from org.allbinary.input.motion.touch.action.DiagonalUpRightTouchInputToGameKeyEventAction import DiagonalUpRightTouchInputToGameKeyEventAction
from org.allbinary.input.motion.touch.action.DownTouchInputToGameKeyEventAction import DownTouchInputToGameKeyEventAction
from org.allbinary.input.motion.touch.action.LeftTouchInputToGameKeyEventAction import LeftTouchInputToGameKeyEventAction
from org.allbinary.input.motion.touch.action.ReleaseTouchInputToGameKeyEventAction import ReleaseTouchInputToGameKeyEventAction
from org.allbinary.input.motion.touch.action.RightTouchInputToGameKeyEventAction import RightTouchInputToGameKeyEventAction
from org.allbinary.input.motion.touch.action.UpTouchInputToGameKeyEventAction import UpTouchInputToGameKeyEventAction
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


CompleteMotionGestureInputToGameMotionGestureInput.instance = CompleteMotionGestureInputToGameMotionGestureInput()


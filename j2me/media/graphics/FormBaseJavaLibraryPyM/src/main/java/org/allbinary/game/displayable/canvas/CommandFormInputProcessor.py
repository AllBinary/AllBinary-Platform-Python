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

from org.allbinary.game.displayable.canvas.BasicMenuInputProcessor import BasicMenuInputProcessor


#In general allow scrolling of the menu and selection the center item
class CommandFormInputProcessor(BasicMenuInputProcessor):

    def _init_fields(self) -> None:
        self.MOTION_GESTURE_SOURCE_ID: int = GameKeyEventFactory.getInstance().MOTION_GESTURE_SOURCE_ID
        self.CLICK_DELAY: int = 150
        self.clickTimeHelper: TimeDelayHelper = TimeDelayHelper(self.CLICK_DELAY)
        self.DOUBLE_CLICK_DELAY: int = 1200
        self.doubleClickTimeHelper: TimeDelayHelper = TimeDelayHelper(self.DOUBLE_CLICK_DELAY)
        self.isSingleKeyProcessing: bool = InputFeatureFactory.getInstance().isSingleKeyProcessing()
        self.form: ScrollSelectionForm = None
        self.hasPressed: bool = False
        self.PROCESS_COMMAND: str = "processCommand"
        self.NAME_LABEL: str = " ScrollSelectionForm: "
    

    def __init__(self, gameKeyEventList: BasicArrayList, playerInputId: int, gameCanvas: MyCanvas, form: ScrollSelectionForm) -> None:
        super().__init__(gameKeyEventList, playerInputId, gameCanvas)
        self._init_fields()
        self.form = form
    

    # throws Exception
    def processInput(self, key: int) -> int:
        if key == Canvas.LEFT or key == Canvas.RIGHT or key == Canvas.UP or key == Canvas.DOWN:
            PrimaryPlayerQueueFactory.getInstance().add(SelectSound.getInstance())
            self.form.processInputKey(key)
            return 1
        elif key == Canvas.FIRE:
            PrimaryPlayerQueueFactory.getInstance().add(SelectSound.getInstance())
            return self.processCommand()
        return 0
    

    def processCommand(self) -> int:
        from org.allbinary.game.displayable.canvas.CommandRunnable import CommandRunnable
        from org.allbinary.game.displayable.canvas.CommandRunnable import CommandRunnable
        commandCurrentSelectionForm: CommandCurrentSelectionForm = self.form
        command: Command = commandCurrentSelectionForm.getSelectedCommand()
        self.logUtil.putF(str(command), self, self.PROCESS_COMMAND)
        features: Features = Features.getInstance()
        openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
        if SWTUtil.isSWT and features.isFeature(openGLFeatureFactory.OPENGL) and command != GameCommandsFactory.getInstance().EXIT_COMMAND:
            CommandRunnable(self, command).run()
        else:
            PrimaryThreadPool.getInstance().runTask(CommandRunnable(self, command))
        if command == GameCommandsFactory.getInstance().QUIT_COMMAND:
            return -1
        else:
            return 1
    

    # throws Exception
    def processInputList(self) -> int:
        try:
            motionInputsIndex: int = self.processMotionInputs()
            list_: BasicArrayList = self.getGameKeyEventList()
            size: int = list_.size()
            key: int = 0
            gameKeyEvent: GameKeyEvent = None
            for index in range(0, size):
                gameKeyEvent = list_.objectArray[index]
                key = gameKeyEvent.getKey()
                if gameKeyEvent.getSourceId() != self.MOTION_GESTURE_SOURCE_ID:
                    if self.processInput(key) == 1:
                        break
            self.clear()
            if size > 0 or motionInputsIndex >= 0:
                return 1
            else:
                return -1
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.gameInputStrings.PROCESS_INPUT, e)
            return -1
    

    # throws Exception
    def processMotionInputs(self) -> int:
        lastIndex: int = self.motionGestureEventList.size() - 1
        if lastIndex >= 0:
            motionGestureEvent: MotionGestureEvent = self.motionGestureEventList.objectArray[lastIndex]
            self.processMotionInput(motionGestureEvent)
        self.motionGestureEventList.clear()
        return lastIndex
    

    # throws Exception
    def processMotionInput(self, motionGestureEvent: MotionGestureEvent) -> None:
        touchMotionGestureFactory: TouchMotionGestureFactory = TouchMotionGestureFactory.getInstance()
        motionGestureInput: MotionGestureInput = motionGestureEvent.getMotionGesture()
        if motionGestureInput == touchMotionGestureFactory.RELEASED:
            point: GPoint = motionGestureEvent.getCurrentPoint()
            if self.form.isInForm(point):
                index: int = self.form.getSelectedIndexForPoint(point)
                if index != -1:
                    PrimaryPlayerQueueFactory.getInstance().add(SelectSound.getInstance())
                    if index == self.form.getSelectedIndex():
                        if self.clickTimeHelper.isTimeTNT():
                            self.processCommand()
                    else:
                        self.form.setSelectedIndex(index)
                else:
                    pass
            if self.hasPressed:
                if not self.doubleClickTimeHelper.isTimeTNT():
                    self.logUtil.putF("Double Press", self, self.gameInputStrings.PROCESS_MOTION_INPUT)
                    self.processCommand()
                self.doubleClickTimeHelper.delay = self.DOUBLE_CLICK_DELAY
                self.doubleClickTimeHelper.setStartTimeTNT()
            self.hasPressed = False
        elif motionGestureInput == touchMotionGestureFactory.PRESSED:
            self.doubleClickTimeHelper.delay = 0
            self.hasPressed = True
    

    def toString(self) -> str:
        return str(StringMaker().append(str(super())).append(self.NAME_LABEL).append(str(self.form)))

    def __str__(self) -> str:
        return self.toString()
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Command import Command
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.InputFeatureFactory import InputFeatureFactory
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
from org.allbinary.game.layer.SWTUtil import SWTUtil
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
from org.allbinary.graphics.form.CommandCurrentSelectionForm import CommandCurrentSelectionForm
from org.allbinary.graphics.form.ScrollSelectionForm import ScrollSelectionForm
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.audio.PrimaryPlayerQueueFactory import PrimaryPlayerQueueFactory
from org.allbinary.media.audio.SelectSound import SelectSound
from org.allbinary.thread.PrimaryThreadPool import PrimaryThreadPool
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.BasicArrayList import BasicArrayList



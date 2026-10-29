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

from org.allbinary.input.motion.button.BaseTouchInput import BaseTouchInput


class BasicTouchButtonsBuilder(BaseTouchInput):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def getList(self) -> BasicArrayList:
        from org.allbinary.input.motion.button.CommonButtons import CommonButtons
        from org.allbinary.input.motion.button.TouchButtonLocationHelper import TouchButtonLocationHelper
        from org.allbinary.input.motion.button.BasicTouchButtonCellPositionFactory import BasicTouchButtonCellPositionFactory
        from org.allbinary.input.motion.button.TouchButton import TouchButton
        from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
        from org.allbinary.input.motion.button.TouchButtonUpResource import TouchButtonUpResource
        from org.allbinary.input.motion.button.TouchButton import TouchButton
        from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
        from org.allbinary.input.motion.button.TouchButtonDownResource import TouchButtonDownResource
        from org.allbinary.input.motion.button.TouchButton import TouchButton
        from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
        from org.allbinary.input.motion.button.TouchButtonTurnLeftResource import TouchButtonTurnLeftResource
        from org.allbinary.input.motion.button.TouchButton import TouchButton
        from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
        from org.allbinary.input.motion.button.TouchButtonTurnRightResource import TouchButtonTurnRightResource
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
            list_: BasicArrayList = BasicArrayListD()
            commonButtons: CommonButtons = CommonButtons.getInstance()
            touchButtonLocationHelper: TouchButtonLocationHelper = TouchButtonLocationHelper()
            basicTouchButtonCellPositionFactory: BasicTouchButtonCellPositionFactory = BasicTouchButtonCellPositionFactory()
            UP: TouchButton = TouchButton.createButton(BasicTouchInputFactory.getInstance().UP, TouchButtonUpResource.getInstance(), commonButtons.NORMAL_BUTTON, basicTouchButtonCellPositionFactory.SECOND_FROM_BOTTOM_LEFT, touchButtonLocationHelper.getColumnsRemainderHalf(), touchButtonLocationHelper.getRowsRemainderHalf())
            DOWN: TouchButton = TouchButton.createButton(BasicTouchInputFactory.getInstance().DOWN, TouchButtonDownResource.getInstance(), commonButtons.NORMAL_BUTTON, basicTouchButtonCellPositionFactory.BOTTOM_LEFT, touchButtonLocationHelper.getColumnsRemainderHalf(), touchButtonLocationHelper.getRowsRemainderHalf())
            LEFT: TouchButton = TouchButton.createButton(BasicTouchInputFactory.getInstance().SPECIAL_BUTTON_FOUR, TouchButtonTurnLeftResource.getInstance(), commonButtons.NORMAL_BUTTON, basicTouchButtonCellPositionFactory.BOTTOM_SECOND_FROM_RIGHT, touchButtonLocationHelper.getColumnsRemainderHalf(), touchButtonLocationHelper.getRowsRemainderHalf())
            RIGHT: TouchButton = TouchButton.createButton(BasicTouchInputFactory.getInstance().SPECIAL_BUTTON_THREE, TouchButtonTurnRightResource.getInstance(), commonButtons.NORMAL_BUTTON, basicTouchButtonCellPositionFactory.BOTTOM_RIGHT, touchButtonLocationHelper.getColumnsRemainderHalf(), touchButtonLocationHelper.getRowsRemainderHalf())
            list_.add(UP)
            list_.add(LEFT)
            list_.add(RIGHT)
            list_.add(DOWN)
            return list_
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.GET_LIST, e)
            return BasicArrayListUtil.getInstance().getImmutableInstance()
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil



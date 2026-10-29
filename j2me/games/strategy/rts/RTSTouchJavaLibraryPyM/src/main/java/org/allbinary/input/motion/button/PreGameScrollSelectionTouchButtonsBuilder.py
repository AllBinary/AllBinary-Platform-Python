# 
# AllBinary Open License Version 1 
# Copyright (c) 2007 AllBinary 
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


class PreGameScrollSelectionTouchButtonsBuilder(BaseTouchInput):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def getList(self) -> BasicArrayList:
        from org.allbinary.input.motion.button.TouchButtonLocationHelper import TouchButtonLocationHelper
        from org.allbinary.input.motion.button.CommonButtons import CommonButtons
        from org.allbinary.input.motion.button.BasicTouchButtonCellPositionFactory import BasicTouchButtonCellPositionFactory
        from org.allbinary.input.motion.button.TouchButton import TouchButton
        from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
        from org.allbinary.input.motion.button.TouchButtonStrafeLeftResource import TouchButtonStrafeLeftResource
        from org.allbinary.input.motion.button.TouchButton import TouchButton
        from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
        from org.allbinary.input.motion.button.TouchButtonStrafeRightResource import TouchButtonStrafeRightResource
        from org.allbinary.input.motion.button.TouchButton import TouchButton
        from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
        from org.allbinary.input.motion.button.TouchButtonStartResource import TouchButtonStartResource
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.GET_LIST)
            list_: BasicArrayList = BasicArrayListD()
            touchButtonLocationHelper: TouchButtonLocationHelper = TouchButtonLocationHelper()
            commonButtons: CommonButtons = CommonButtons.getInstance()
            basicTouchButtonCellPositionFactory: BasicTouchButtonCellPositionFactory = BasicTouchButtonCellPositionFactory()
            LEFT: TouchButton = TouchButton.createButton(BasicTouchInputFactory.getInstance().LEFT, TouchButtonStrafeLeftResource.getInstance(), commonButtons.NORMAL_BUTTON, basicTouchButtonCellPositionFactory.TOP_LEFT, touchButtonLocationHelper.getColumnsRemainderHalf(), touchButtonLocationHelper.getRowsRemainderHalf())
            RIGHT: TouchButton = TouchButton.createButton(BasicTouchInputFactory.getInstance().RIGHT, TouchButtonStrafeRightResource.getInstance(), commonButtons.NORMAL_BUTTON, basicTouchButtonCellPositionFactory.TOP_RIGHT, touchButtonLocationHelper.getColumnsRemainderHalf(), touchButtonLocationHelper.getRowsRemainderHalf())
            START: TouchButton = TouchButton.createButton(BasicTouchInputFactory.getInstance().SPECIAL_BUTTON_FIVE, TouchButtonStartResource.getInstance(), commonButtons.NORMAL_BUTTON, basicTouchButtonCellPositionFactory.BOTTOM_RIGHT, touchButtonLocationHelper.getColumnsRemainderHalf(), touchButtonLocationHelper.getRowsRemainderHalf())
            list_.add(LEFT)
            list_.add(RIGHT)
            list_.add(START)
            return list_
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.GET_LIST, e)
            return BasicArrayListUtil.getInstance().getImmutableInstance()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil



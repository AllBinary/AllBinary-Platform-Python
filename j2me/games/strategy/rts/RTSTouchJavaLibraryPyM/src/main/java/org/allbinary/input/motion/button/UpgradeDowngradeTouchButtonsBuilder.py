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


class UpgradeDowngradeTouchButtonsBuilder(BaseTouchInput):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def getList(self) -> BasicArrayList:
        from org.allbinary.input.motion.button.TouchButtonLocationHelper import TouchButtonLocationHelper
        from org.allbinary.input.motion.button.BasicTouchButtonCellPositionFactory import BasicTouchButtonCellPositionFactory
        from org.allbinary.input.motion.button.CommonButtons import CommonButtons
        from org.allbinary.input.motion.button.TouchButton import TouchButton
        from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
        from org.allbinary.input.motion.button.TouchButton import TouchButton
        from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
            list_: BasicArrayList = BasicArrayListD()
            touchButtonLocationHelper: TouchButtonLocationHelper = TouchButtonLocationHelper()
            cellPositionFactory: CellPositionFactory = CellPositionFactory.getInstance()
            basicTouchButtonCellPositionFactory: BasicTouchButtonCellPositionFactory = BasicTouchButtonCellPositionFactory()
            if basicTouchButtonCellPositionFactory.SECOND_FROM_TOP_LEFT != cellPositionFactory.NONE and basicTouchButtonCellPositionFactory.SECOND_FROM_TOP_RIGHT != cellPositionFactory.NONE:
                commonButtons: CommonButtons = CommonButtons.getInstance()
                UP: TouchButton = TouchButton.createButton(BasicTouchInputFactory.getInstance().SPECIAL_BUTTON_TWO, TouchButtonUpgradeResource.getInstance(), commonButtons.NORMAL_BUTTON, basicTouchButtonCellPositionFactory.SECOND_FROM_TOP_LEFT, touchButtonLocationHelper.getColumnsRemainderHalf(), touchButtonLocationHelper.getRowsRemainderHalf())
                DOWN: TouchButton = TouchButton.createButton(BasicTouchInputFactory.getInstance().SPECIAL_BUTTON_ONE, TouchButtonDowngradeResource.getInstance(), commonButtons.NORMAL_BUTTON, basicTouchButtonCellPositionFactory.SECOND_FROM_TOP_RIGHT, touchButtonLocationHelper.getColumnsRemainderHalf(), touchButtonLocationHelper.getRowsRemainderHalf())
                list_.add(UP)
                list_.add(DOWN)
            return list_
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
            return BasicArrayListUtil.getInstance().getImmutableInstance()
from org.allbinary.game.input.resource.TouchButtonDowngradeResource import TouchButtonDowngradeResource
from org.allbinary.game.input.resource.TouchButtonUpgradeResource import TouchButtonUpgradeResource
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.graphics.CellPositionFactory import CellPositionFactory



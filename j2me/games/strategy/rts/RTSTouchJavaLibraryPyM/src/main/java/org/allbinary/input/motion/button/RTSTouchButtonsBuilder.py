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


class RTSTouchButtonsBuilder(BaseTouchInput):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def getList(self) -> BasicArrayList:
        from org.allbinary.input.motion.button.BasicTouchButtonsBuilder import BasicTouchButtonsBuilder
        from org.allbinary.input.motion.button.BuildingScrollTouchButtonsBuilder import BuildingScrollTouchButtonsBuilder
        from org.allbinary.input.motion.button.UpgradeDowngradeTouchButtonsBuilder import UpgradeDowngradeTouchButtonsBuilder
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
            list_: BasicArrayList = BasicArrayListD()
            list_.addAllList(BasicTouchButtonsBuilder().getList())
            list_.addAllList(BuildingScrollTouchButtonsBuilder().getList())
            list_.addAllList(UpgradeDowngradeTouchButtonsBuilder().getList())
            return list_
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
            return BasicArrayListUtil.getInstance().getImmutableInstance()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil



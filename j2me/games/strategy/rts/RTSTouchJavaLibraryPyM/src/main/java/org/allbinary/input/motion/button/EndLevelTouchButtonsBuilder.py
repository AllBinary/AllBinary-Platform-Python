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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.input.motion.button.TouchButtonsListBuilder import TouchButtonsListBuilder


@java_inherited_overloads
class EndLevelTouchButtonsBuilder(TouchButtonsListBuilder):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def getList(self) -> BasicArrayList:
        from org.allbinary.input.motion.button.BasicTouchButtonsBuilder import BasicTouchButtonsBuilder
        from org.allbinary.input.motion.button.BuildingScrollTouchButtonsBuilder import BuildingScrollTouchButtonsBuilder
        from org.allbinary.input.motion.button.UpgradeDowngradeTouchButtonsBuilder import UpgradeDowngradeTouchButtonsBuilder
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
            list_: BasicArrayList = BasicArrayListD()
            list_.addAllList(BasicTouchButtonsBuilder().getList())
            list_.addAllList(BuildingScrollTouchButtonsBuilder().getList())
            list_.addAllList(UpgradeDowngradeTouchButtonsBuilder().getList())
            self.addList(list_)
            return list_
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
            return BasicArrayListUtil.getInstance().getImmutableInstance()
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil



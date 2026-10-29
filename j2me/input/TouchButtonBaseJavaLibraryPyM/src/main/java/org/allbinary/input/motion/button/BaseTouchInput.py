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



class BaseTouchInput:

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getList(self) -> BasicArrayList:
        return self.basicArrayListUtil.getImmutableInstance()
    

    def toString(self) -> str:
        return type(self).__module__ + "." + type(self).__qualname__

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil



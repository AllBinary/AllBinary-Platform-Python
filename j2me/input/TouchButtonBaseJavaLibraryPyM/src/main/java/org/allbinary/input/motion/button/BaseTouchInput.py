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
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def getList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.basicArrayListUtil.getImmutableInstance()
    

    def toString(self) -> str:
        return __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(self))

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil



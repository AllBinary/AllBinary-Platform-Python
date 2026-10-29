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
# package org.allbinary.data.tree.dom

from __future__ import annotations



class ToDomHelper:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def convertNull(value: str) -> str:
        if value is None:
            value = StringUtil.getInstance().NULL_STRING
        return value
from org.allbinary.logic.string.StringUtil import StringUtil



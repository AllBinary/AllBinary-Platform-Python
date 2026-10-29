# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations



class LayerUtil:
    HASHTABLE: str = "Hashtable: "
    

    @staticmethod
    def toString(hashtable: ABHashtable[object, object], x: int, y: int, z: int) -> str:
        commonSeps: CommonSeps = CommonSeps.getInstance()
        positionStrings: PositionStrings = PositionStrings.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(LayerUtil.HASHTABLE)
        stringBuffer.append(StringUtil.getInstance().toString(hashtable))
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(positionStrings.X_LABEL)
        stringBuffer.appendint(x)
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(positionStrings.Y_LABEL)
        stringBuffer.appendint(y)
        stringBuffer.append(commonSeps.SPACE)
        stringBuffer.append(positionStrings.Z_LABEL)
        stringBuffer.appendint(z)
        return str(stringBuffer)
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.util.ABHashtable import ABHashtable



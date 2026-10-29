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
# package org.allbinary.media.image.cache

from __future__ import annotations

from org.allbinary.logic.StdUtil import StdUtil


class BufferedImageInfoFactory:
    hashMap: dict = StdUtil.getInstance().createHashMap()
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance(width: int, height: int, type_: int) -> BufferedImageInfo:
        from org.allbinary.media.image.cache.BufferedImageInfo import BufferedImageInfo
        stringbuffer: StringMaker = StringMaker()
        stringbuffer.appendint(width)
        stringbuffer.appendint(height)
        stringbuffer.appendint(type_)
        key: str = str(stringbuffer)
        bufferedImageInfo: BufferedImageInfo = BufferedImageInfoFactory.hashMap.get(key)
        if bufferedImageInfo is None:
            bufferedImageInfo = BufferedImageInfo(width, height, type_)
            BufferedImageInfoFactory.hashMap.put(key, bufferedImageInfo)
        return bufferedImageInfo
# from java.util.HashMap import HashMap
from org.allbinary.logic.string.StringMaker import StringMaker



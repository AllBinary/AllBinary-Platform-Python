# 
# AllBinary Open License Version 1 
# Copyright (c) 2026 AllBinary 
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
# package org.allbinary.logic

from __future__ import annotations

import time


class ABSystemWrapper:
    instance: ABSystemWrapper = None
    

    @staticmethod
    def getInstance() -> ABSystemWrapper:
        return ABSystemWrapper.instance
    

    def arraycopy(self, src: object, srcPos: int, dest: object, destPos: int, length: int) -> None:
        dest[destPos:destPos + length] = src[srcPos:srcPos + length]
    

    def currentTimeMillis(self) -> int:
        return int(time.time() * 1000)
from jsinterop.annotations.JsType import JsType


ABSystemWrapper.instance = ABSystemWrapper()


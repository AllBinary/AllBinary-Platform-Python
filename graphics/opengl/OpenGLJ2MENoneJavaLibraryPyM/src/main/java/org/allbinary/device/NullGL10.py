# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.device

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from javax.microedition.khronos.opengles.GL10 import GL10


class NullGL10(GL10):
    NULL_GL10: NullGL10 = None


def _NullGL10_NULL_GL10() -> object:
    return NullGL10()

lazy_static(NullGL10, "NULL_GL10", _NullGL10_NULL_GL10)


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
# package org.allbinary.thread

from __future__ import annotations

import threading
from java.lang.JavaRuntimeStatic import lazy_static


class NullThread:
    NULL_THREAD: threading.Thread = None


def _NullThread_NULL_THREAD() -> object:
    return threading.Thread()

lazy_static(NullThread, "NULL_THREAD", _NullThread_NULL_THREAD)


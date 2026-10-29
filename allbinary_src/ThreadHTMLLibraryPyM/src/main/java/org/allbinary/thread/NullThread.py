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
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.thread.NullRunnable import NullRunnable


class NullThread:
    NULL_THREAD: threading.Thread = threading.Thread(target=NullRunnable.getInstance().run, name=StringUtil.getInstance().EMPTY_STRING)



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
# package org.allbinary.logic.io

from __future__ import annotations

# from java.io.Closeable import Closeable


class NullCloseable(Closeable):
    NULL_CLOSEABLE: NullCloseable = None
    

    # throws IOException
    def close(self) -> None:
        pass
# from java.io.IOException import IOException


NullCloseable.NULL_CLOSEABLE = NullCloseable()


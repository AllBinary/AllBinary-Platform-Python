#
# AllBinary Open License Version 1
# Copyright (c) 2009 AllBinary
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
# package org.allbinary.android.input.motion

from __future__ import annotations



class GameInputMotionInfo:

    def _init_fields(self) -> None:
        self.MAX_API: int = None
        self.MAX_POINTERS: int = None
    

    def __init__(self, maxApi: int, maxPointers: int) -> None:
        self._init_fields()
        self.MAX_API = maxApi
        self.MAX_POINTERS = maxPointers



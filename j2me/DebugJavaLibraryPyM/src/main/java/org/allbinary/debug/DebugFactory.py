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
# package org.allbinary.debug

from __future__ import annotations



class DebugFactory:
    

    @staticmethod
    def getInstance() -> DebugInterface:
        from org.allbinary.debug.NoDebug import NoDebug
        return NoDebug.getInstance()



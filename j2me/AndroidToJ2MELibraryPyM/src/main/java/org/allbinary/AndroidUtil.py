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
# package org.allbinary

from __future__ import annotations

from android.app.Activity import Activity
from android.os.Build import Build


class AndroidUtil:
    NULL_ACTIVITY: Activity = Activity()
    version: int = int(Build.VERSION.SDK)
    

    @staticmethod
    def isMemoryRestrictive() -> bool:
        if AndroidUtil.version < 30:
            return True
        return False
    

    @staticmethod
    def isAndroid() -> bool:
        return True



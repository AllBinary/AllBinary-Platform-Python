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

from java.lang.JavaRuntimeStatic import lazy_static


class AndroidUtil:
    NULL_ACTIVITY: Activity = None
    version: int = None
    

    @staticmethod
    def isMemoryRestrictive() -> bool:
        if AndroidUtil.version < 30:
            return True
        return False
    

    @staticmethod
    def isAndroid() -> bool:
        return True
# from android.app.Activity import Activity
# from android.os.Build import Build


def _AndroidUtil_NULL_ACTIVITY() -> object:
    from android.app.Activity import Activity
    return Activity()

lazy_static(AndroidUtil, "NULL_ACTIVITY", _AndroidUtil_NULL_ACTIVITY)

def _AndroidUtil_version() -> object:
    from android.os.Build import Build
    return int(Build.VERSION.SDK)

lazy_static(AndroidUtil, "version", _AndroidUtil_version)


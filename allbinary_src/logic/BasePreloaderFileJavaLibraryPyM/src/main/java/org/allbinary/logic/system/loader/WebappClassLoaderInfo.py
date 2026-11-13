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
# package org.allbinary.logic.system.loader

from __future__ import annotations

import threading
from java.lang.JavaRuntimeStatic import lazy_static


class WebappClassLoaderInfo:
    classLoader: object = None
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def setLoader(classLoader: ClassLoader) -> None:
        with WebappClassLoaderInfo._lock:
            return WebappClassLoaderInfo._setLoader_unlocked(classLoader)

    @staticmethod
    def _setLoader_unlocked(classLoader: ClassLoader) -> None:
        WebappClassLoaderInfo.classLoader = classLoader
    

    @staticmethod
    def getLoader() -> ClassLoader:
        with WebappClassLoaderInfo._lock:
            return WebappClassLoaderInfo._getLoader_unlocked()

    @staticmethod
    def _getLoader_unlocked() -> ClassLoader:
        return WebappClassLoaderInfo.classLoader
# from org.allbinary.logic.NullUtil import NullUtil


def _WebappClassLoaderInfo_classLoader() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(WebappClassLoaderInfo, "classLoader", _WebappClassLoaderInfo_classLoader)


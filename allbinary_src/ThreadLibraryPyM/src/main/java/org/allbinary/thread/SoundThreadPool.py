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
# package org.allbinary.thread

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class SoundThreadPool:
    instance: ThreadPool = None
    

    @staticmethod
    def getInstance() -> ThreadPool:
        return SoundThreadPool.instance


def _SoundThreadPool_instance() -> object:
    from org.allbinary.thread.ThreadPool import ThreadPool
    from org.allbinary.thread.ThreadPool import ThreadPool
    return ThreadPool("Sound", 1, ThreadPool.NORMAL_PRIORITY)

lazy_static(SoundThreadPool, "instance", _SoundThreadPool_instance)


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
# package org.allbinary.media.audio

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class SecondaryPlayerQueueFactory:
    SINGLETON: PlayerQueue = None
    

    @staticmethod
    def getInstance() -> PlayerQueue:
        return SecondaryPlayerQueueFactory.SINGLETON


def _SecondaryPlayerQueueFactory_SINGLETON() -> object:
    from org.allbinary.media.audio.PlayerQueue import PlayerQueue
    return PlayerQueue(4)

lazy_static(SecondaryPlayerQueueFactory, "SINGLETON", _SecondaryPlayerQueueFactory_SINGLETON)


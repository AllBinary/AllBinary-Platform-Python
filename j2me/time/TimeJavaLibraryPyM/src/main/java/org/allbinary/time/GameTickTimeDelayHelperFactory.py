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
# package org.allbinary.time

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class GameTickTimeDelayHelperFactory:
    instance: GameTickTimeDelayHelper = None
    

    @staticmethod
    def getInstance() -> GameTickTimeDelayHelper:
        return GameTickTimeDelayHelperFactory.instance
    

    def __init__(self) -> None:
        pass


def _GameTickTimeDelayHelperFactory_instance() -> object:
    from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
    return GameTickTimeDelayHelper(-1)

lazy_static(GameTickTimeDelayHelperFactory, "instance", _GameTickTimeDelayHelperFactory_instance)


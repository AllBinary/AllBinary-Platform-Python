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
# package org.allbinary.game

from __future__ import annotations

from org.allbinary.game.IntermissionEnableListenerInterface import IntermissionEnableListenerInterface


class NullIntermissionEnableListener(IntermissionEnableListenerInterface):
    SINGLETON: IntermissionEnableListenerInterface = None
    

    @staticmethod
    def getInstance() -> IntermissionEnableListenerInterface:
        return NullIntermissionEnableListener.SINGLETON
    

    def __init__(self) -> None:
        pass
    

    def notifyIntermission(self, enable: bool) -> None:
        pass


NullIntermissionEnableListener.SINGLETON = NullIntermissionEnableListener()


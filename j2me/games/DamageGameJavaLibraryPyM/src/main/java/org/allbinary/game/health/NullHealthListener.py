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
# package org.allbinary.game.health

from __future__ import annotations

from org.allbinary.game.health.HealthListenerInterface import HealthListenerInterface


class NullHealthListener(HealthListenerInterface):
    NULL_HEALTH_LISTENER: NullHealthListener = None
    

    def onHealthChange(self) -> None:
        pass


NullHealthListener.NULL_HEALTH_LISTENER = NullHealthListener()


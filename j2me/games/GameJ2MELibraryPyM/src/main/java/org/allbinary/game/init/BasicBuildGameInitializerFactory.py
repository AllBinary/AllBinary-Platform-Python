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
# package org.allbinary.game.init

from __future__ import annotations

from org.allbinary.game.init.GameInitializationInterfaceFactoryInterface import GameInitializationInterfaceFactoryInterface


class BasicBuildGameInitializerFactory(GameInitializationInterfaceFactoryInterface):
    NULL_BASE_BUILD_GMAE_INITIALIZER_FACTORY: BasicBuildGameInitializerFactory = None
    

    def getInstance(self) -> GameInitializationInterface:
        from org.allbinary.game.init.BaseGameInitialization import BaseGameInitialization
        return BaseGameInitialization.NULL_BASE_GAME_INITIALIZATION


BasicBuildGameInitializerFactory.NULL_BASE_BUILD_GMAE_INITIALIZER_FACTORY = BasicBuildGameInitializerFactory()


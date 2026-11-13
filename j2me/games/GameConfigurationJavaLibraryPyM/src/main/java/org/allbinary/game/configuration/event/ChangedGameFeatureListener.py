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
# package org.allbinary.game.configuration.event

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.configuration.event.BaseChangedGameFeatureListener import BaseChangedGameFeatureListener


class ChangedGameFeatureListener(BaseChangedGameFeatureListener):
    gameFeatureListener: ChangedGameFeatureListener = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> ChangedGameFeatureListener:
        return ChangedGameFeatureListener.gameFeatureListener
    

    def isChangedGameConfiguration(self, gameConfiguration: GameConfiguration) -> bool:
        from org.allbinary.game.configuration.GameConfiguration import GameConfiguration
        return self.list_.contains(gameConfiguration)
# from org.allbinary.game.configuration.GameConfiguration import GameConfiguration


def _ChangedGameFeatureListener_gameFeatureListener() -> object:
    return ChangedGameFeatureListener()

lazy_static(ChangedGameFeatureListener, "gameFeatureListener", _ChangedGameFeatureListener_gameFeatureListener)


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

from org.allbinary.game.configuration.event.BaseChangedGameFeatureListener import BaseChangedGameFeatureListener


class ChangedGameFeatureListener(BaseChangedGameFeatureListener):
    gameFeatureListener: ChangedGameFeatureListener = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> ChangedGameFeatureListener:
        return ChangedGameFeatureListener.gameFeatureListener
    

    def isChangedGameConfiguration(self, gameConfiguration: GameConfiguration) -> bool:
        return self.list_.contains(gameConfiguration)
from org.allbinary.game.configuration.GameConfiguration import GameConfiguration


ChangedGameFeatureListener.gameFeatureListener = ChangedGameFeatureListener()


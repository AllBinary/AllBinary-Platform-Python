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
# package org.allbinary.game.configuration.feature

from __future__ import annotations



class GameFeatureFactory:
    instance: GameFeatureFactory = None

    def _init_fields(self) -> None:
        self.SOUND: GameFeature = GameFeature("Sound")
        self.MUSIC: GameFeature = GameFeature("Music")
        self.SCREEN_SHAKE: Feature = Feature("Screen Shake")
        self.POST_IMAGE_LOADING_MODIFICATION: Feature = Feature("Post Image Loading Modification (Scaling, Rotation, or Other)")
        self.HEALTH_BARS: GameFeature = GameFeature("Health Bars")
        self.DAMAGE_FLOATERS: GameFeature = GameFeature("Damage Floaters")
        self.GAME_INPUT_LAYER_PROCESSOR: GameFeature = GameFeature("Game Input Layer Processor")
        self.ARTIFICIAL_INTELLEGENCE_PROCESSOR: GameFeature = GameFeature("Artificial Intelligence Layer Processor")
        self.COLLIDABLE_INTERFACE_LAYER_PROCESSOR: GameFeature = GameFeature("Collidable Interface Layer Processor")
        self.TICKABLE_LAYER_PROCESSOR: GameFeature = GameFeature("Tickable Layer Processor")
        self.CHEATING: GameFeature = GameFeature("Cheating")
        self.DROPPED_ITEMS: GameFeature = GameFeature("Drops")
        self.DROPPED_ITEMS_FROM_DEATH: GameFeature = GameFeature("Drops from Dead")
        self.TEST_DESTROYED_LAYER_PROCESSOR: GameFeature = GameFeature("Destroyed Layer Processor")
        self.COLLISIONS_WITH_SOURCE: GameFeature = GameFeature("Allow Collisions With Source")
        self.COLLISIONS_FORCED_TWO_DIMENSIONAL: GameFeature = GameFeature("Collisions Forced Two Dimensional")
    

    @staticmethod
    def getInstance() -> GameFeatureFactory:
        return GameFeatureFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
from org.allbinary.game.configuration.feature.GameFeature import GameFeature
from org.allbinary.game.configuration.feature.Feature import Feature


GameFeatureFactory.instance = GameFeatureFactory()


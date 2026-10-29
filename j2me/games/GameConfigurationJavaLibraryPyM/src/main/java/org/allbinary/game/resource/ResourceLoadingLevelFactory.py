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
# package org.allbinary.game.resource

from __future__ import annotations



class ResourceLoadingLevelFactory:
    instance: ResourceLoadingLevelFactory = None

    def _init_fields(self) -> None:
        self.LOAD_EARLY: ResourceLoadingLevel = ResourceLoadingLevel("Load Early", 2147483647)
        self.LOAD_TOUCH: ResourceLoadingLevel = ResourceLoadingLevel("Load Touch", 2147483647 - 1)
        self.LOAD_GAME: ResourceLoadingLevel = ResourceLoadingLevel("Load Game", 2147483647 - 2)
        self.LEVEL: ResourceLoadingLevel = ResourceLoadingLevel("Level", 2147483647 - 99)
        self.MAX_LEVEL: ResourceLoadingLevel = ResourceLoadingLevel("Max Level", 2147483647 - 100)
        self.LOAD_ALL: ResourceLoadingLevel = ResourceLoadingLevel("Load All", -1)
        self.RESOURCE_LOADING_LEVEL_ARRAY: list[ResourceLoadingLevel] = [self.LOAD_ALL, self.MAX_LEVEL, self.LEVEL, self.LOAD_GAME, self.LOAD_TOUCH, self.LOAD_EARLY]

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ResourceLoadingLevelFactory:
        return ResourceLoadingLevelFactory.instance
    

    def getLevelString(self, level: int) -> str:
        for index in range(0, len(self.RESOURCE_LOADING_LEVEL_ARRAY)):
            if level == self.RESOURCE_LOADING_LEVEL_ARRAY[index].getLevel():
                return self.RESOURCE_LOADING_LEVEL_ARRAY[index].getName()
        return str(level)
from org.allbinary.game.resource.ResourceLoadingLevel import ResourceLoadingLevel


ResourceLoadingLevelFactory.instance = ResourceLoadingLevelFactory()


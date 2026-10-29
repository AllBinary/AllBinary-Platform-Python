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

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class GameInitializedEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.resourceLoadingLevel: ResourceLoadingLevel = ResourceLoadingLevelFactory.getInstance().LEVEL
        self.level: int = 0
    

    def __init__(self, anyType: object) -> None:
        super().__init__(anyType)
        self._init_fields()
    

    def setLevel(self, level: int) -> None:
        self.level = level
        self.resourceLoadingLevel = ResourceLoadingLevelFactory.getInstance().LEVEL
    

    def getLevel(self) -> int:
        return self.level
    

    def setResourceLoadingLevel(self, resourceLoadingLevel: ResourceLoadingLevel) -> None:
        self.resourceLoadingLevel = resourceLoadingLevel
        self.level = self.resourceLoadingLevel.getLevel()
    

    def getResourceLoadingLevel(self) -> ResourceLoadingLevel:
        return self.resourceLoadingLevel
from org.allbinary.game.resource.ResourceLoadingLevel import ResourceLoadingLevel
from org.allbinary.game.resource.ResourceLoadingLevelFactory import ResourceLoadingLevelFactory



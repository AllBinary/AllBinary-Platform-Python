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

from org.allbinary.game.configuration.feature.GameFeatureControlledInterface import GameFeatureControlledInterface


# Java interface
class ResourceRelativeRelationshipFactoryInterface(GameFeatureControlledInterface):
    

    # throws Exception
    def getResourceRelativeRelationshipList(self, resource: str) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def addResourceRelativeRelationship(self, resource: str, relativeRelationship: RelativeRelationship) -> None:
        raise NotImplementedError()
from org.allbinary.graphics.RelativeRelationship import RelativeRelationship
from org.allbinary.util.BasicArrayList import BasicArrayList



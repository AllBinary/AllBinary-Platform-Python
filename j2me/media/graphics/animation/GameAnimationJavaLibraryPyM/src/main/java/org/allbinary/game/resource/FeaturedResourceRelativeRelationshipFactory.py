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

from org.allbinary.game.resource.FeaturedResourceFactory import FeaturedResourceFactory


class FeaturedResourceRelativeRelationshipFactory(FeaturedResourceFactory):
    INSTANCE: FeaturedResourceRelativeRelationshipFactory = None

    def _init_fields(self) -> None:
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> FeaturedResourceRelativeRelationshipFactory:
        return FeaturedResourceRelativeRelationshipFactory.INSTANCE
    

    # throws Exception
    def getRelativeRelationshipList(self, resource: str, layer: AllBinaryLayer) -> BasicArrayList:
        featureReleaseList: BasicArrayList = self.getList()
        size: int = self.getList().size()
        for index in range(0, size):
            featureInterface: ResourceRelativeRelationshipFactoryInterface = featureReleaseList.objectArray[index]
            if featureInterface.isFeature():
                list_: BasicArrayList = featureInterface.getResourceRelativeRelationshipList(resource)
                if list_ != self.basicArrayListUtil.getImmutableInstance():
                    return self.duplicate(list_, layer)
        raise Exception(str(StringMaker().append("Not available for current feature selection or Resource: ").append(resource)))
    

    # throws Exception
    def duplicate(self, list_: BasicArrayList, layer: AllBinaryLayer) -> BasicArrayList:
        pointFactory: PointFactory = PointFactory.getInstance()
        newList: BasicArrayList = BasicArrayListD()
        size: int = list_.size()
        for index in range(0, size):
            relativeRelationship: RelativeRelationship = list_.objectArray[index]
            newList.add(RelativeLayerRelationship(layer, pointFactory.createXY(relativeRelationship.getX(), relativeRelationship.getY()), BasicArrayListUtil.getInstance().getImmutableInstance()))
        return newList
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.RelativeRelationship import RelativeRelationship
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.relationship.RelativeLayerRelationship import RelativeLayerRelationship
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil


FeaturedResourceRelativeRelationshipFactory.INSTANCE = FeaturedResourceRelativeRelationshipFactory()


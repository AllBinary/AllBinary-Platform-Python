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



class FeatureResourceInitializationUtil:
    instance: FeatureResourceInitializationUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> FeatureResourceInitializationUtil:
        return FeatureResourceInitializationUtil.instance
    

    # throws Exception
    def init(self, level: int) -> None:
        from org.allbinary.game.resource.FeaturedResourceRelativeRelationshipFactory import FeaturedResourceRelativeRelationshipFactory
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF(commonStrings.START, self, commonStrings.INIT)
        featuredResourceFactory: FeaturedResourceFactory = FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance()
        featuredResourceFactory.init(level)
        FeaturedResourceRelativeRelationshipFactory.getInstance().init(level)
from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


FeatureResourceInitializationUtil.instance = FeatureResourceInitializationUtil()


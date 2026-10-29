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
# package org.allbinary.game.layer.resources

from __future__ import annotations



class OnDemandResources:
    NULL_ON_DEMAND_RESOURCES: OnDemandResources = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def waitFor(self) -> None:
        pass
    

    # throws Exception
    def init(self) -> None:
        pass
    

    # throws Exception
    def initAt(self, imageCache: ImageCache, resourceAnimationInterfaceFactoryInterfaceFactory: BaseResourceAnimationInterfaceFactoryInterfaceFactory, portion: int, loadingString: str, index: int) -> int:
        return 0
from org.allbinary.animation.resource.BaseResourceAnimationInterfaceFactoryInterfaceFactory import BaseResourceAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.image.ImageCache import ImageCache
from org.allbinary.logic.communication.log.LogUtil import LogUtil


OnDemandResources.NULL_ON_DEMAND_RESOURCES = OnDemandResources()


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
# package org.allbinary.business.advertisement.campaign

from __future__ import annotations



# Java interface
class AdvertisementCampaignInterface:
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def getComponent(self) -> object:
        raise NotImplementedError()
    

    def setName(self, name: str) -> None:
        raise NotImplementedError()
    

    def setComponentName(self, name: str) -> None:
        raise NotImplementedError()
    

    def search(self, advertisementSearchInterface: AdvertisementSearchInterface) -> AdvertisementsInterface:
        raise NotImplementedError()
from org.allbinary.business.advertisement.AdvertisementsInterface import AdvertisementsInterface
from org.allbinary.business.advertisement.search.AdvertisementSearchInterface import AdvertisementSearchInterface



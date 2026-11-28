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

from org.allbinary.business.advertisement.campaign.AdvertisementCampaignInterface import AdvertisementCampaignInterface


class AdvertisementCampaign(AdvertisementCampaignInterface):

    def _init_fields(self) -> None:
        if "hashMap" not in vars(self): self.hashMap: HashMap = None
    

    def __init__(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        __class__._init_fields(self)
        self.hashMap = hashMap
    

    def getComponent(self) -> object:
        return None
    

    def getName(self) -> str:
        from org.allbinary.business.advertisement.campaign.AdvertisementCampaignData import AdvertisementCampaignData
        return self.hashMap.get(AdvertisementCampaignData.getInstance().NAME)
    

    def setComponentName(self, name: str) -> None:
        from org.allbinary.business.DynamicObjectData import DynamicObjectData
        self.hashMap.put(DynamicObjectData.NAME, name)
    

    def setName(self, name: str) -> None:
        from org.allbinary.business.advertisement.campaign.AdvertisementCampaignData import AdvertisementCampaignData
        self.hashMap.put(AdvertisementCampaignData.getInstance().NAME, name)
    

    def search(self, advertisementSearchInterface: AdvertisementSearchInterface) -> AdvertisementsInterface:
        from org.allbinary.business.advertisement.AdvertisementsInterface import AdvertisementsInterface
        from org.allbinary.business.advertisement.search.AdvertisementSearchInterface import AdvertisementSearchInterface
        return None
# from java.util.HashMap import HashMap
# from org.allbinary.business.DynamicObjectData import DynamicObjectData
# from org.allbinary.business.advertisement.AdvertisementsInterface import AdvertisementsInterface
# from org.allbinary.business.advertisement.search.AdvertisementSearchInterface import AdvertisementSearchInterface



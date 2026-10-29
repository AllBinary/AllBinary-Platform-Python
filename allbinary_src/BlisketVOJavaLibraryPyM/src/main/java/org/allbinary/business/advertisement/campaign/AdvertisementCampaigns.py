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

from org.allbinary.business.advertisement.campaign.AdvertisementCampaignsInterface import AdvertisementCampaignsInterface


class AdvertisementCampaigns(AdvertisementCampaignsInterface):

    def _init_fields(self) -> None:
        self.advertisementsVector: BasicArrayList = None
    

    def __init__(self, vector: BasicArrayList) -> None:
        self._init_fields()
        self.advertisementsVector = self.advertisementsVector
    

    def add(self, advertisementInterface: AdvertisementInterface) -> None:
        self.advertisementsVector.add(advertisementInterface)
    

    def get(self, index: int) -> AdvertisementInterface:
        return self.advertisementsVector.get(index)
    

    def size(self) -> int:
        return self.advertisementsVector.size()
    

    def isEnabled(self) -> bool:
        return True
    

    def search(self, advertisementSearchInterface: AdvertisementSearchInterface) -> AdvertisementsInterface:
        return None
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.advertisement.AdvertisementInterface import AdvertisementInterface
from org.allbinary.business.advertisement.AdvertisementsInterface import AdvertisementsInterface
from org.allbinary.business.advertisement.search.AdvertisementSearchInterface import AdvertisementSearchInterface



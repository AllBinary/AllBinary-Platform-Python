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
class AdvertisementCampaignsInterface:
    

    def add(self, advertisementInterface: AdvertisementInterface) -> None:
        raise NotImplementedError()
    

    def get(self, index: int) -> AdvertisementInterface:
        raise NotImplementedError()
    

    def size(self) -> int:
        raise NotImplementedError()
    

    def isEnabled(self) -> bool:
        raise NotImplementedError()
from org.allbinary.business.advertisement.AdvertisementInterface import AdvertisementInterface



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
# package org.allbinary.business.advertisement.area

from __future__ import annotations



# Java interface
class AdvertisementAreaInterface:
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def getStoreName(self) -> str:
        raise NotImplementedError()
    

    def getDescription(self) -> str:
        raise NotImplementedError()
    

    def getConstraints(self) -> AdvertisementAreaConstraintsInterface:
        raise NotImplementedError()
    

    def getCampaign(self) -> str:
        raise NotImplementedError()
    

    def setName(self, name: str) -> None:
        raise NotImplementedError()
    

    def setStoreName(self, storeName: str) -> None:
        raise NotImplementedError()
    

    def setDescription(self, description: str) -> None:
        raise NotImplementedError()
    

    def setConstraints(self, advertisementConstraintsInterface: AdvertisementAreaConstraintsInterface) -> None:
        raise NotImplementedError()
    

    def setCampaign(self, campaign: str) -> None:
        raise NotImplementedError()



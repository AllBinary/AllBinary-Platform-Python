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

from org.allbinary.business.advertisement.area.AdvertisementAreaInterface import AdvertisementAreaInterface


class AdvertisementArea(AdvertisementAreaInterface):

    def _init_fields(self) -> None:
        self.name: str = None
        self.storeName: str = None
        self.description: str = None
        self.advertisementAreaConstraintsInterface: AdvertisementAreaConstraintsInterface = None
        self.campaign: str = None
    

    def __init__(self, hashMap: dict) -> None:
        from org.allbinary.business.advertisement.area.AdvertisementAreaData import AdvertisementAreaData
        from org.allbinary.business.advertisement.area.AdvertisementAreaData import AdvertisementAreaData
        from org.allbinary.business.advertisement.area.AdvertisementAreaData import AdvertisementAreaData
        from org.allbinary.business.advertisement.area.AdvertisementAreaConstraints import AdvertisementAreaConstraints
        self._init_fields()
        self.name = hashMap.get(AdvertisementAreaData.getInstance().NAME)
        self.storeName = hashMap.get(StoreFrontData.getInstance().NAME)
        self.description = hashMap.get(AdvertisementAreaData.getInstance().DESCRIPTION)
        constraintsDomString: str = hashMap.get(AdvertisementAreaData.getInstance().CONSTRAINTS)
        document: Document = DomDocumentHelper.create(constraintsDomString)
        self.advertisementAreaConstraintsInterface = AdvertisementAreaConstraints(document)
        self.campaign = hashMap.get(AdvertisementCampaignData.getInstance().NAME)
    

    def getName(self) -> str:
        return self.name
    

    def getStoreName(self) -> str:
        return self.storeName
    

    def getDescription(self) -> str:
        return self.description
    

    def getConstraints(self) -> AdvertisementAreaConstraintsInterface:
        return self.advertisementAreaConstraintsInterface
    

    def getCampaign(self) -> str:
        return self.campaign
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def setStoreName(self, storeName: str) -> None:
        self.storeName = storeName
    

    def setDescription(self, description: str) -> None:
        self.description = description
    

    def setConstraints(self, advertisementConstraintsInterface: AdvertisementAreaConstraintsInterface) -> None:
        self.advertisementAreaConstraintsInterface = self.advertisementAreaConstraintsInterface
    

    def setCampaign(self, campaign: str) -> None:
        self.campaign = campaign
# from java.util.HashMap import HashMap
from org.allbinary.business.advertisement.campaign.AdvertisementCampaignData import AdvertisementCampaignData
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.w3c.dom.Document import Document



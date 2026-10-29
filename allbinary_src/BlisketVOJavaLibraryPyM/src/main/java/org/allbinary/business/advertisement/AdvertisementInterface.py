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
# package org.allbinary.business.advertisement

from __future__ import annotations



# Java interface
class AdvertisementInterface:
    

    def getArtist(self) -> str:
        raise NotImplementedError()
    

    def getArtistLink(self) -> str:
        raise NotImplementedError()
    

    def getTitle(self) -> str:
        raise NotImplementedError()
    

    def getDateAdded(self) -> str:
        raise NotImplementedError()
    

    def getDirectory(self) -> str:
        raise NotImplementedError()
    

    def getFramedLink(self) -> str:
        raise NotImplementedError()
    

    def getListPrice(self) -> Money:
        raise NotImplementedError()
    

    def getOurPrice(self) -> Money:
        raise NotImplementedError()
    

    def getRank(self) -> int:
        raise NotImplementedError()
    

    def getImage(self) -> AdvertisementImageInterface:
        raise NotImplementedError()
    

    def getProduct(self) -> AdvertisementProductInterface:
        raise NotImplementedError()
    

    def getThumbnail(self) -> AdvertisementThumbnailInterface:
        raise NotImplementedError()
    

    def getDisplayInBrowserContraintsInterface(self) -> DisplayInBrowserContraintsInterface:
        raise NotImplementedError()
    

    def setArtist(self, artist: str) -> None:
        raise NotImplementedError()
    

    def setArtistLink(self, artistLink: str) -> None:
        raise NotImplementedError()
    

    def setTitle(self, title: str) -> None:
        raise NotImplementedError()
    

    def setDateAdded(self, dateAdded: str) -> None:
        raise NotImplementedError()
    

    def setDirectory(self, directory: str) -> None:
        raise NotImplementedError()
    

    def setFramedLink(self, framedLink: str) -> None:
        raise NotImplementedError()
    

    def setRank(self, rank: int) -> None:
        raise NotImplementedError()
    

    def setImage(self, AdvertisementImageInterface: AdvertisementImageInterface) -> None:
        raise NotImplementedError()
    

    def setProduct(self, AdvertisementProductInterface: AdvertisementProductInterface) -> None:
        raise NotImplementedError()
    

    def setThumbnail(self, AdvertisementThumbnailInterface: AdvertisementThumbnailInterface) -> None:
        raise NotImplementedError()
from org.allbinary.business.advertisement.image.AdvertisementImageInterface import AdvertisementImageInterface
from org.allbinary.business.advertisement.product.AdvertisementProductInterface import AdvertisementProductInterface
from org.allbinary.business.advertisement.thumbnail.AdvertisementThumbnailInterface import AdvertisementThumbnailInterface
from org.allbinary.business.user.commerce.money.Money import Money
from org.allbinary.logic.control.contraints.display.browser.DisplayInBrowserContraintsInterface import DisplayInBrowserContraintsInterface



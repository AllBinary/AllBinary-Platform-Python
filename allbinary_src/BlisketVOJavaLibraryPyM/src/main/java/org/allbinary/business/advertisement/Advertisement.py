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

from org.allbinary.business.advertisement.AdvertisementInterface import AdvertisementInterface


class Advertisement(AdvertisementInterface):

    def _init_fields(self) -> None:
        self.artist: str = None
        self.artistLink: str = None
        self.title: str = None
        self.dateAdded: str = None
        self.directory: str = None
        self.framedLink: str = None
        self.rank: int = 0
        self.listPrice: Money = None
        self.ourPrice: Money = None
        self.image: AdvertisementImageInterface = None
        self.product: AdvertisementProductInterface = None
        self.thumbnail: AdvertisementThumbnailInterface = None
        self.displayInBrowserContraintsInterface: DisplayInBrowserContraintsInterface = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.displayInBrowserContraintsInterface = None
    

    def getArtist(self) -> str:
        return self.artist
    

    def setArtist(self, artist: str) -> None:
        self.artist = artist
    

    def getArtistLink(self) -> str:
        return self.artistLink
    

    def setArtistLink(self, artistLink: str) -> None:
        self.artistLink = artistLink
    

    def getTitle(self) -> str:
        return self.title
    

    def setTitle(self, title: str) -> None:
        self.title = title
    

    def getDateAdded(self) -> str:
        return self.dateAdded
    

    def setDateAdded(self, dateAdded: str) -> None:
        self.dateAdded = dateAdded
    

    def getDirectory(self) -> str:
        return self.directory
    

    def setDirectory(self, directory: str) -> None:
        self.directory = directory
    

    def getFramedLink(self) -> str:
        return self.framedLink
    

    def setFramedLink(self, framedLink: str) -> None:
        self.framedLink = framedLink
    

    def getListPrice(self) -> Money:
        return self.listPrice
    

    def setListPrice(self, listPrice: Money) -> None:
        self.listPrice = listPrice
    

    def getOurPrice(self) -> Money:
        return self.ourPrice
    

    def setOurPrice(self, ourPrice: Money) -> None:
        self.ourPrice = ourPrice
    

    def getRank(self) -> int:
        return self.rank
    

    def setRank(self, rank: int) -> None:
        self.rank = rank
    

    def getImage(self) -> AdvertisementImageInterface:
        return self.image
    

    def setImage(self, image: AdvertisementImageInterface) -> None:
        self.image = image
    

    def getProduct(self) -> AdvertisementProductInterface:
        return self.product
    

    def setProduct(self, product: AdvertisementProductInterface) -> None:
        self.product = product
    

    def getThumbnail(self) -> AdvertisementThumbnailInterface:
        return self.thumbnail
    

    def setThumbnail(self, thumbnail: AdvertisementThumbnailInterface) -> None:
        self.thumbnail = thumbnail
    

    def getDisplayInBrowserContraintsInterface(self) -> DisplayInBrowserContraintsInterface:
        return self.displayInBrowserContraintsInterface
from org.allbinary.business.advertisement.image.AdvertisementImageInterface import AdvertisementImageInterface
from org.allbinary.business.advertisement.product.AdvertisementProductInterface import AdvertisementProductInterface
from org.allbinary.business.advertisement.thumbnail.AdvertisementThumbnailInterface import AdvertisementThumbnailInterface
from org.allbinary.business.user.commerce.money.Money import Money
from org.allbinary.logic.control.contraints.display.browser.DisplayInBrowserContraintsInterface import DisplayInBrowserContraintsInterface



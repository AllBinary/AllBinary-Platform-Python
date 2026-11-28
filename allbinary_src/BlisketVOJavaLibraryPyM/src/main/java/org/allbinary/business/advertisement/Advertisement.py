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
        if "artist" not in vars(self): self.artist: str = None
        if "artistLink" not in vars(self): self.artistLink: str = None
        if "title" not in vars(self): self.title: str = None
        if "dateAdded" not in vars(self): self.dateAdded: str = None
        if "directory" not in vars(self): self.directory: str = None
        if "framedLink" not in vars(self): self.framedLink: str = None
        if "rank" not in vars(self): self.rank: int = 0
        if "listPrice" not in vars(self): self.listPrice: Money = None
        if "ourPrice" not in vars(self): self.ourPrice: Money = None
        if "image" not in vars(self): self.image: AdvertisementImageInterface = None
        if "product" not in vars(self): self.product: AdvertisementProductInterface = None
        if "thumbnail" not in vars(self): self.thumbnail: AdvertisementThumbnailInterface = None
        if "displayInBrowserContraintsInterface" not in vars(self): self.displayInBrowserContraintsInterface: DisplayInBrowserContraintsInterface = None
    

    def __init__(self) -> None:
        __class__._init_fields(self)
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
        from org.allbinary.business.user.commerce.money.Money import Money
        return self.listPrice
    

    def setListPrice(self, listPrice: Money) -> None:
        from org.allbinary.business.user.commerce.money.Money import Money
        self.listPrice = listPrice
    

    def getOurPrice(self) -> Money:
        from org.allbinary.business.user.commerce.money.Money import Money
        return self.ourPrice
    

    def setOurPrice(self, ourPrice: Money) -> None:
        from org.allbinary.business.user.commerce.money.Money import Money
        self.ourPrice = ourPrice
    

    def getRank(self) -> int:
        return self.rank
    

    def setRank(self, rank: int) -> None:
        self.rank = rank
    

    def getImage(self) -> AdvertisementImageInterface:
        from org.allbinary.business.advertisement.image.AdvertisementImageInterface import AdvertisementImageInterface
        return self.image
    

    def setImage(self, image: AdvertisementImageInterface) -> None:
        from org.allbinary.business.advertisement.image.AdvertisementImageInterface import AdvertisementImageInterface
        self.image = image
    

    def getProduct(self) -> AdvertisementProductInterface:
        from org.allbinary.business.advertisement.product.AdvertisementProductInterface import AdvertisementProductInterface
        return self.product
    

    def setProduct(self, product: AdvertisementProductInterface) -> None:
        from org.allbinary.business.advertisement.product.AdvertisementProductInterface import AdvertisementProductInterface
        self.product = product
    

    def getThumbnail(self) -> AdvertisementThumbnailInterface:
        from org.allbinary.business.advertisement.thumbnail.AdvertisementThumbnailInterface import AdvertisementThumbnailInterface
        return self.thumbnail
    

    def setThumbnail(self, thumbnail: AdvertisementThumbnailInterface) -> None:
        from org.allbinary.business.advertisement.thumbnail.AdvertisementThumbnailInterface import AdvertisementThumbnailInterface
        self.thumbnail = thumbnail
    

    def getDisplayInBrowserContraintsInterface(self) -> DisplayInBrowserContraintsInterface:
        from org.allbinary.logic.control.contraints.display.browser.DisplayInBrowserContraintsInterface import DisplayInBrowserContraintsInterface
        return self.displayInBrowserContraintsInterface
# from org.allbinary.business.advertisement.image.AdvertisementImageInterface import AdvertisementImageInterface
# from org.allbinary.business.advertisement.product.AdvertisementProductInterface import AdvertisementProductInterface
# from org.allbinary.business.advertisement.thumbnail.AdvertisementThumbnailInterface import AdvertisementThumbnailInterface
# from org.allbinary.business.user.commerce.money.Money import Money
# from org.allbinary.logic.control.contraints.display.browser.DisplayInBrowserContraintsInterface import DisplayInBrowserContraintsInterface



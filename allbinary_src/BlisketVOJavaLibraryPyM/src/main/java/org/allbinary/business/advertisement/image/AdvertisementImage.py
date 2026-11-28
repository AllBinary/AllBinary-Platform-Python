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
# package org.allbinary.business.advertisement.image

from __future__ import annotations

from org.allbinary.business.advertisement.image.AdvertisementImageInterface import AdvertisementImageInterface


class AdvertisementImage(AdvertisementImageInterface):

    def _init_fields(self) -> None:
        if "imageFileName" not in vars(self): self.imageFileName: str = None
        if "imageUrl" not in vars(self): self.imageUrl: str = None
        if "constraint" not in vars(self): self.constraint: TwoDimensionalConstraintInterface = None
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def getFileName(self) -> str:
        return self.imageFileName
    

    def getUrl(self) -> str:
        return self.imageUrl
    

    def getTwoDimensionalConstraint(self) -> TwoDimensionalConstraintInterface:
        from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface
        return self.constraint
# from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface



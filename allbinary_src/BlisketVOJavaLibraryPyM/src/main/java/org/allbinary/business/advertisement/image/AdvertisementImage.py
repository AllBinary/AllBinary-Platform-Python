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
        self.imageFileName: str = None
        self.imageUrl: str = None
        self.constraint: TwoDimensionalConstraintInterface = None
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getFileName(self) -> str:
        return self.imageFileName
    

    def getUrl(self) -> str:
        return self.imageUrl
    

    def getTwoDimensionalConstraint(self) -> TwoDimensionalConstraintInterface:
        return self.constraint
from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface



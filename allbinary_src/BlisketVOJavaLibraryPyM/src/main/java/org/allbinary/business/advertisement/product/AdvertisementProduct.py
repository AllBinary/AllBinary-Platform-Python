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
# package org.allbinary.business.advertisement.product

from __future__ import annotations

from org.allbinary.business.advertisement.product.AdvertisementProductInterface import AdvertisementProductInterface


class AdvertisementProduct(AdvertisementProductInterface):

    def _init_fields(self) -> None:
        self.type_: str = None
        self.link: str = None
        self.number: int = 0
        self.constraint: TwoDimensionalConstraintInterface = None
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getType(self) -> str:
        return self.type_
    

    def getLink(self) -> str:
        return self.link
    

    def getNumber(self) -> int:
        return self.number
    

    def getTwoDimensionalConstraint(self) -> TwoDimensionalConstraintInterface:
        return self.constraint
from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface



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
        if "type_" not in vars(self): self.type_: str = None
        if "link" not in vars(self): self.link: str = None
        if "number" not in vars(self): self.number: int = 0
        if "constraint" not in vars(self): self.constraint: TwoDimensionalConstraintInterface = None
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def getType(self) -> str:
        return self.type_
    

    def getLink(self) -> str:
        return self.link
    

    def getNumber(self) -> int:
        return self.number
    

    def getTwoDimensionalConstraint(self) -> TwoDimensionalConstraintInterface:
        from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface
        return self.constraint
# from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface



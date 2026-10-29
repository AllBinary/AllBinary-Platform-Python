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



# Java interface
class AdvertisementImageInterface:
    

    def getFileName(self) -> str:
        raise NotImplementedError()
    

    def getUrl(self) -> str:
        raise NotImplementedError()
    

    def getTwoDimensionalConstraint(self) -> TwoDimensionalConstraintInterface:
        raise NotImplementedError()
from org.allbinary.logic.control.contraints.size.TwoDimensionalConstraintInterface import TwoDimensionalConstraintInterface



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
# package org.allbinary.business.user.commerce.money.tax.modules

from __future__ import annotations



# Java interface
class TaxModuleInterface:
    

    # throws Exception
    def getTaxRate(self, streetAddress: StreetAddress, storeFrontInterface: StoreFrontInterface) -> float:
        raise NotImplementedError()
    

    # throws Exception
    def isValid(self, streetAddress: StreetAddress, storeFrontInterface: StoreFrontInterface) -> bool:
        raise NotImplementedError()
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.address.StreetAddress import StreetAddress



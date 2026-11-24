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
# package views.admin.inventory.listings

from __future__ import annotations



# Java interface
class ProductListingInterface:
    

    # throws Exception
    def generateAll_j0(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def generateAll_j1(self, storeName: str) -> str:
        raise NotImplementedError()

    def generateAll(self, *args):
        return getattr(self, "generateAll_j" + str(len(args)))(*args)



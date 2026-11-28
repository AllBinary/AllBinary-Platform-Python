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
# package org.allbinary.business.user.commerce.inventory.item

from __future__ import annotations



class ItemInfo:

    def _init_fields(self) -> None:
        if "type_" not in vars(self): self.type_: list[str] = None
        if "view" not in vars(self): self.view: list[str] = None
        if "data" not in vars(self): self.data: list[str] = None
        if "creationDate" not in vars(self): self.creationDate: list[str] = None
        if "lastModified" not in vars(self): self.lastModified: list[str] = None
    

    def __init__(self) -> None:
        __class__._init_fields(self)



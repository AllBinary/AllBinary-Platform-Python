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
# package org.allbinary.logic.system.security.licensing

from __future__ import annotations



class LicenseType:

    def _init_fields(self) -> None:
        self.name: str = None
    

    def __init__(self, name: str) -> None:
        self._init_fields()
        self.setName(name)
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def getName(self) -> str:
        return self.name



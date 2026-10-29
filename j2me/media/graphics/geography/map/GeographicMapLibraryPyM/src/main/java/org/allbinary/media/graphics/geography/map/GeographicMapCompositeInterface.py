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
# package org.allbinary.media.graphics.geography.map

from __future__ import annotations



# Java interface
class GeographicMapCompositeInterface:
    

    def geographicMapCellTypeArray(self) -> list[GeographicMapCellType]:
        raise NotImplementedError()
    

    def getGeographicMapInterface(self) -> list[BasicGeographicMap]:
        raise NotImplementedError()
    

    def setGeographicMapInterface(self, geographicMapInterface: list[BasicGeographicMap]) -> None:
        raise NotImplementedError()



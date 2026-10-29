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
# package org.allbinary.media.image

from __future__ import annotations



class ImageUnifierCell:

    def _init_fields(self) -> None:
        self.width: int = None
        self.height: int = None
    

    def __init__(self, width: int, height: int) -> None:
        self._init_fields()
        self.setWidth(width)
        self.setHeight(height)
    

    def getWidth(self) -> int:
        return self.width
    

    def setWidth(self, width: int) -> None:
        self.width = width
    

    def getHeight(self) -> int:
        return self.height
    

    def setHeight(self, height: int) -> None:
        self.height = height



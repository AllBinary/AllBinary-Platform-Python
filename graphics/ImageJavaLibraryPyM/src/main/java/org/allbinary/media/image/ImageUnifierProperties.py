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



class ImageUnifierProperties:

    def _init_fields(self) -> None:
        if "rows" not in vars(self): self.rows: int = None
        if "columns" not in vars(self): self.columns: int = None
        if "imageUnifierCell" not in vars(self): self.imageUnifierCell: ImageUnifierCell = None
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def getWidth(self) -> int:
        return int(self.getColumns()) * int(self.getImageUnifierCell().getWidth())
    

    def getHeight(self) -> int:
        return int(self.getRows()) * int(self.getImageUnifierCell().getHeight())
    

    def getRows(self) -> int:
        return self.rows
    

    def setRows(self, rows: int) -> None:
        self.rows = rows
    

    def getColumns(self) -> int:
        return self.columns
    

    def setColumns(self, columns: int) -> None:
        self.columns = columns
    

    def getImageUnifierCell(self) -> ImageUnifierCell:
        return self.imageUnifierCell
    

    def setImageUnifierCell(self, imageUnifierCell: ImageUnifierCell) -> None:
        self.imageUnifierCell = imageUnifierCell



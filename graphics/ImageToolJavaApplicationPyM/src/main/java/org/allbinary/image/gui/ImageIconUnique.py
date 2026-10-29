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
# package org.allbinary.image.gui

from __future__ import annotations

from org.allbinary.image.gui.ImageIcon import ImageIcon


class ImageIconUnique(ImageIcon):

    def _init_fields(self) -> None:
        self.id: int = 0
    

    def __init__(self, bufferedImage: BufferedImage, index: int) -> None:
        super().__init__(bufferedImage)
        self._init_fields()
        self.setId(index)
    

    def getId(self) -> int:
        return self.id
    

    def setId(self, id: int) -> None:
        self.id = id
# from java.awt.image.BufferedImage import BufferedImage
# from javax.swing import *



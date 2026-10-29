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



class ImageProcessorInput:

    def _init_fields(self) -> None:
        self.bufferedImageArray: list[BufferedImage] = None
        self.files: list[File] = None
    

    def __init__(self, files: list[File], bufferedImageArray: list[BufferedImage]) -> None:
        super().__init__()
        self._init_fields()
        self.bufferedImageArray = bufferedImageArray
        self.files = files
    

    def getBufferedImageArray(self) -> list[BufferedImage]:
        return self.bufferedImageArray
    

    def getFiles(self) -> list[File]:
        return self.files
# from java.awt.image.BufferedImage import BufferedImage
# from java.io.File import File



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
# package org.allbinary.logic.visual.media

from __future__ import annotations



class MediaDataFactory:
    instance: MediaDataFactory = None

    def _init_fields(self) -> None:
        self.AVI: MediaData = MediaData("avi")
        self.BMP: MediaData = MediaData("bmp")
        self.CEL: MediaData = MediaData("cel")
        self.FITS: MediaData = MediaData("fits")
        self.FLI: MediaData = MediaData("fli")
        self.GBR: MediaData = MediaData("gbr")
        self.GIF: MediaData = MediaData("gif")
        self.GIH: MediaData = MediaData("gih")
        self.JPG: MediaData = MediaData("jpg")
        self.PIX: MediaData = MediaData("pix")
        self.PNG: MediaData = MediaData("png")
        self.PNM: MediaData = MediaData("pnm")
        self.PSD: MediaData = MediaData("psd")
        self.PSP: MediaData = MediaData("psp")
        self.PS: MediaData = MediaData("ps")
        self.SGI: MediaData = MediaData("SGI")
        self.SWF: MediaData = MediaData("swf")
        self.TGA: MediaData = MediaData("tga")
        self.TIFF: MediaData = MediaData("tiff")
        self.WMF: MediaData = MediaData("wmf")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> MediaDataFactory:
        return MediaDataFactory.instance
from org.allbinary.logic.visual.media.MediaData import MediaData


MediaDataFactory.instance = MediaDataFactory()


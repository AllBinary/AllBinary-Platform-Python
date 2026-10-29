# Generated Code Do Not Modify
# package org.allbinary.logic.visual.media

from __future__ import annotations



class MediaIOUtil:
    instance: MediaIOUtil = None
    

    @staticmethod
    def getInstance() -> MediaIOUtil:
        return MediaIOUtil.instance
    

    def getReaderFormatNames(self) -> list[str]:
        return ImageIO.getReaderFormatNames()
    

    def getWriterFormatNames(self) -> list[str]:
        return ImageIO.getWriterFormatNames()
# from javax.imageio.ImageIO import ImageIO


MediaIOUtil.instance = MediaIOUtil()


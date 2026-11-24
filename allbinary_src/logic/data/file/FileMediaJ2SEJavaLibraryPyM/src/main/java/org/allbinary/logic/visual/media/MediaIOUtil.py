# Generated Code Do Not Modify
# package org.allbinary.logic.visual.media

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


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


def _MediaIOUtil_instance() -> object:
    return MediaIOUtil()

lazy_static(MediaIOUtil, "instance", _MediaIOUtil_instance)


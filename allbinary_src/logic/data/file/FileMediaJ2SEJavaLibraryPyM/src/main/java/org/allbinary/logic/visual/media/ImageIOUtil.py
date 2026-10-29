# Generated Code Do Not Modify
# package org.allbinary.logic.visual.media

from __future__ import annotations



class ImageIOUtil:
    

    # throws Exception
    @staticmethod
    def read(file: AbFile) -> BufferedImage:
        return ImageIO.read(AbFileNativeUtil.get(file))
    

    # throws Exception
    @staticmethod
    def write(renderedImage: RenderedImage, name: str, file: AbFile) -> bool:
        return ImageIO.write(renderedImage, name, AbFileNativeUtil.get(file))
# from java.awt.image.BufferedImage import BufferedImage
# from java.awt.image.RenderedImage import RenderedImage
# from javax.imageio.ImageIO import ImageIO
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil



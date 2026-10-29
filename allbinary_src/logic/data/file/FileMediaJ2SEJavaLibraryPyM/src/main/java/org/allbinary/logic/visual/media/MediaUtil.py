# Generated Code Do Not Modify
# package org.allbinary.logic.visual.media

from __future__ import annotations



#import com.sun.imageio.plugins.common.ImageUtil;
class MediaUtil:
    instance: MediaUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> MediaUtil:
        return MediaUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def saveImageFile(self, originalImageFile: AbFile, newImageFileName: str, category: str, mediaData: MediaData, newWidth: int, newHeight: int) -> None:
        from org.allbinary.logic.visual.media.ImageIOUtil import ImageIOUtil
        from org.allbinary.logic.visual.media.ImageIOUtil import ImageIOUtil
        if originalImageFile is None or not originalImageFile.isFile():
            raise Exception("Original Image File Does Not Exist.")
        bufferedImage: BufferedImage = ImageIOUtil.read(originalImageFile)
        if bufferedImage is None:
            raise Exception("Unable to find ImageReader for this file.")
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            hashMap: dict = self.getImageBufferPropertyHashMap(bufferedImage)
            self.logUtil.putF("Image Properties: " + str(hashMap), self, "saveImageFile()")
        imageFile: AbFile = AbFile.createAbFile(category + newImageFileName)
        imageFile.createNewFile()
        imageUtil: ImageUtil = ImageUtil.getInstance()
        newBufferedImage: BufferedImage = imageUtil.createBufferedImageForSave(bufferedImage, newWidth, newHeight)
        isWritten: bool = ImageIOUtil.write(newBufferedImage, mediaData.getName(), imageFile)
        if not isWritten:
            raise Exception("Unable to write.")
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            commonLabels: CommonLabels = CommonLabels.getInstance()
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Get Path: ")
            stringBuffer.append(originalImageFile.getPath())
            stringBuffer.append("\nNewImageFileName: ")
            stringBuffer.append(newImageFileName)
            stringBuffer.append("\nCategory: ")
            stringBuffer.append(category)
            stringBuffer.append("\nSave File Type: ")
            stringBuffer.append(mediaData.getName())
            stringBuffer.append("\nNew").append(commonLabels.WIDTH_LABEL)
            stringBuffer.appendint(newWidth)
            stringBuffer.append("\nNew").append(commonLabels.HEIGHT_LABEL)
            stringBuffer.appendint(newHeight)
            stringBuffer.append("\nFile Length: ")
            stringBuffer.appendlong(originalImageFile.length())
            stringBuffer.append("\nNew File Length: ")
            stringBuffer.appendlong(imageFile.length())
            self.logUtil.putF(str(stringBuffer), self, "saveImageFile()")
    

    @staticmethod
    def getImageBufferPropertyHashMap(bufferedImage: BufferedImage) -> dict:
        hashMap: dict = StdUtil.getInstance().createHashMap()
        propertyStringArray: list[str] = bufferedImage.getPropertyNames()
        if propertyStringArray is not None:
            for index in range(0, len(propertyStringArray)):
                propertyObject: object = bufferedImage.getProperty(propertyStringArray[index])
                hashMap.put(propertyStringArray[index], str(propertyObject))
        return hashMap
# from java.awt.image.BufferedImage import BufferedImage
# from java.awt.image.RenderedImage import RenderedImage
# from java.util.HashMap import HashMap
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.image.ImageUtil import ImageUtil
from org.allbinary.string.CommonLabels import CommonLabels


MediaUtil.instance = MediaUtil()


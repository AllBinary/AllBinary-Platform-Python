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
# package views.admin.inventory

from __future__ import annotations



class InventoryUploadMediaUtil:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.mediaUtil: MediaUtil = MediaUtil.getInstance()
        self.LARGEWIDTH: int = 1024
        self.LARGEHEIGHT: int = 1024
        self.MEDIUMWIDTH: int = 256
        self.MEDIUMHEIGHT: int = 256
        self.SMALLWIDTH: int = 128
        self.SMALLHEIGHT: int = 128
        self.SMALL: str = "Small"
        self.MEDIUM: str = "Medium"
        self.LARGE: str = "Large"
        self.storeFrontInterface: StoreFrontInterface = None
        self.itemInterface: ItemInterface = None
    

    def __init__(self, storeFrontInterface: StoreFrontInterface, itemInterface: ItemInterface) -> None:
        self._init_fields()
        self.storeFrontInterface = storeFrontInterface
        self.itemInterface = itemInterface
    

    # throws Exception
    def saveFiles(self, byteArray: list[int], fileName: str, mediaData: MediaData) -> ItemInterface:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF("Start FileName: " + fileName, self, "saveFiles()")
        if StringValidationUtil.getInstance().isEmpty(fileName):
            raise Exception("Image File Name Was Null")
        fileUtil: FileUtil = FileUtil.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.URLGLOBALS.getWebappPath())
        stringBuffer.append(self.storeFrontInterface.getCurrentHostNamePath())
        stringBuffer.append(self.itemInterface.getCategory())
        fullPath: str = str(stringBuffer)
        imageDirectoryFile: AbFile = AbFile.createAbFile(fullPath)
        if not imageDirectoryFile.isDirectory():
            raise Exception("Unable to save file to non existant directory")
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(fullPath)
        stringBuffer.append(fileName)
        stringBuffer.append(AbPathData.getInstance().EXTENSION_SEP)
        stringBuffer.append(mediaData.getName())
        originalImageFile: AbFile = AbFile.createAbFile(str(stringBuffer))
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF("Saving Original Image: " + str(originalImageFile), self, "saveFiles()")
        originalImageFile.createNewFile()
        fileUtil.write(ByteArrayInputStream(byteArray), originalImageFile)
        uploadMedia: UploadMediaSingleton = UploadMediaSingleton.getInstance()
        isMediaSupported: bool = uploadMedia.isWriterSupported(mediaData.getName()) or uploadMedia.isReaderSupported(mediaData.getName())
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append("Is Image Type: ")
            stringBuffer.append(mediaData.getName())
            stringBuffer.append(" supported: ")
            stringBuffer.appendboolean(isMediaSupported)
            self.logUtil.putF(str(stringBuffer), self, "saveFiles()")
        defaultMediaData: MediaData = MediaData.getDefault()
        self.setFileNames(fileName)
        if isMediaSupported:
            isMediaResizable: bool = uploadMedia.isWriterMedia(mediaData.getName(), MediaTypeData.getInstance().RESIZABLE_MEDIA)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append("Is ")
                stringBuffer.append(str(mediaData))
                stringBuffer.append(" Image Resize Supported:")
                stringBuffer.appendboolean(uploadMedia.isSupported(mediaData.getName()))
                stringBuffer.append(" WriterMedia: ")
                stringBuffer.appendboolean(isMediaResizable)
                self.logUtil.putF(str(stringBuffer), self, "saveFiles()")
            if isMediaResizable:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
                    self.logUtil.putF("Saving Small Image: " + str(self.itemInterface.getSmallImage()), self, "saveFiles()")
                self.mediaUtil.saveImageFile(originalImageFile, self.itemInterface.getSmallImage(), fullPath, mediaData, self.SMALLWIDTH, self.SMALLHEIGHT)
                self.mediaUtil.saveImageFile(originalImageFile, self.itemInterface.getMediumImage(), fullPath, mediaData, self.MEDIUMWIDTH, self.MEDIUMHEIGHT)
                self.mediaUtil.saveImageFile(originalImageFile, self.itemInterface.getLargeImage(), fullPath, mediaData, self.LARGEWIDTH, self.LARGEHEIGHT)
            else:
                isConvertable: bool = mediaData.isConvertableTo(defaultMediaData)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
                    stringBuffer.delete(0, stringBuffer.length())
                    stringBuffer.append("Converting: ")
                    stringBuffer.append(defaultMediaData.getName())
                    stringBuffer.append(" into ")
                    stringBuffer.append(mediaData.getName())
                    stringBuffer.append(" if Convertable is it: ")
                    stringBuffer.appendboolean(isConvertable)
                    self.logUtil.putF(str(stringBuffer), self, "saveFiles()")
                if isConvertable:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
                        self.logUtil.putF("Saving Small Image: " + str(self.itemInterface.getSmallImage()), self, "saveFiles()")
                    self.mediaUtil.saveImageFile(originalImageFile, self.itemInterface.getSmallImage(), fullPath, defaultMediaData, self.SMALLWIDTH, self.SMALLHEIGHT)
                    self.mediaUtil.saveImageFile(originalImageFile, self.itemInterface.getMediumImage(), fullPath, defaultMediaData, self.MEDIUMWIDTH, self.MEDIUMHEIGHT)
                    self.mediaUtil.saveImageFile(originalImageFile, self.itemInterface.getLargeImage(), fullPath, defaultMediaData, self.LARGEWIDTH, self.LARGEHEIGHT)
                else:
                    smallImageFile: AbFile = AbFile.createAbFile(self.itemInterface.getSmallImage())
                    smallImageFile.createNewFile()
                    fileUtil.write(ByteArrayInputStream(byteArray), smallImageFile)
                    mediumImageFile: AbFile = AbFile.createAbFile(self.itemInterface.getMediumImage())
                    smallImageFile.createNewFile()
                    fileUtil.write(ByteArrayInputStream(byteArray), mediumImageFile)
                    largeImageFile: AbFile = AbFile.createAbFile(self.itemInterface.getSmallImage())
                    largeImageFile.createNewFile()
                    fileUtil.write(ByteArrayInputStream(byteArray), largeImageFile)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.END, self, "saveFiles()")
        return self.itemInterface
    

    def setFileNames(self, fileName: str) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.itemInterface.getId())
        stringBuffer.append(AbPathData.getInstance().EXTENSION_SEP)
        stringBuffer.append(MediaData.getDefault().getName())
        END: str = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(fileName)
        stringBuffer.append(self.SMALL)
        stringBuffer.append(END)
        newImageFileName: str = str(stringBuffer)
        self.itemInterface.setSmallImage(newImageFileName)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(fileName)
        stringBuffer.append(self.MEDIUM)
        stringBuffer.append(END)
        newImageFileName = str(stringBuffer)
        self.itemInterface.setMediumImage(newImageFileName)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(fileName)
        stringBuffer.append(self.LARGE)
        stringBuffer.append(END)
        newImageFileName = str(stringBuffer)
        self.itemInterface.setLargeImage(newImageFileName)
# from java.io.ByteArrayInputStream import ByteArrayInputStream
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.http.file.upload.media.UploadMediaSingleton import UploadMediaSingleton
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FileUtil import FileUtil
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.media.MediaData import MediaData
from org.allbinary.logic.visual.media.MediaTypeData import MediaTypeData
from org.allbinary.logic.visual.media.MediaUtil import MediaUtil
from org.allbinary.string.CommonStrings import CommonStrings



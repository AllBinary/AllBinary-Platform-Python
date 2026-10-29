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
# package views.admin.inventory.download

from __future__ import annotations

from org.allbinary.logic.communication.http.request.RequestMapInterface import RequestMapInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class DownloadableInventoryItemView(HttpStoreComponentView, RequestMapInterface):
    TYPE_ID: int = 11

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        self.request: HttpServletRequest = None
        self.id: str = None
        self.itemInterface: ItemInterface = None
        self.downloadableItem: DownloadableItem = None
        self.requestHashMap: dict = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor1(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.request = self.getPageContext().getRequest()
        self.getFormData()
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, empty: str) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.request = self.getPageContext().getRequest()
    

    def getTypeId(self) -> int:
        return DownloadableInventoryItemView.TYPE_ID
    

    # throws Exception
    def getFormData(self) -> None:
        self.setRequestHashMap(MultipartRequestParams(self.request).toHashMap())
        self.id = self.getRequestHashMap().get(self.basicItemData.ID)
    

    def addDomNodeInterfaces(self) -> None:
        vector: BasicArrayList = BasicArrayListD()
        if self.downloadableItem is not None:
            vector.add(DownloadableItemView(self.downloadableItem))
        self.addDomNodeInterface(BasicItemView(self.itemInterface, vector))
    

    # throws Exception
    def view(self) -> str:
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
    

    # throws Exception
    def processFile(self, fileItem: FileItem) -> None:
        fileName: str = fileItem.getName()
        fullPath: str = self.getItemFilePath()
        itemResourceFile: AbFile = AbFile.createAbFile(fullPath)
        itemResourceFile.mkdir()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(fullPath)
        stringBuffer.append(fileName)
        self.logUtil.putF("FileName: " + fileName, self, "processFile()")
        file: AbFile = AbFile.createAbFile(str(stringBuffer))
        self.logUtil.putF(file.getPath(), self, "processFiles()")
        file.createNewFile()
        byteArray: list[int] = fileItem.get()
        FileUtil.getInstance().write(ByteArrayInputStream(byteArray), file)
    

    # throws Exception
    def unzip(self, fileItem: FileItem) -> None:
        fileName: str = fileItem.getName()
        fullPath: str = self.getItemFilePath()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(fullPath)
        stringBuffer.append(fileName)
        self.logUtil.putF("FileName: " + fileName, self, "unzip()")
        file: AbFile = AbFile.createAbFile(str(stringBuffer))
        self.logUtil.putF(file.getPath(), self, "unzip()")
        ZipFileUtil.getInstance().unzip(fullPath, file, fileName)
    

    def getItemFilePath(self) -> str:
        storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.getWeblisketSession().getStoreName())
        filePathData: FilePathData = FilePathData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.URLGLOBALS.getWebappPath())
        stringBuffer.append(storeFrontInterface.getCurrentHostNamePath())
        stringBuffer.append(self.itemInterface.getCategory())
        stringBuffer.appendchar(filePathData.SEPARATORCHAR)
        stringBuffer.append(self.itemInterface.getId())
        stringBuffer.appendchar(filePathData.SEPARATORCHAR)
        stringBuffer.append(self.downloadableItem.getId())
        stringBuffer.appendchar(filePathData.SEPARATORCHAR)
        return str(stringBuffer)
    

    def setRequestHashMap(self, requestHashMap: dict) -> None:
        self.requestHashMap = requestHashMap
    

    def getRequestHashMap(self) -> dict:
        return self.requestHashMap
    

    def getDownloadableItem(self) -> DownloadableItem:
        return self.downloadableItem
# from java.io.ByteArrayInputStream import ByteArrayInputStream
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.business.user.commerce.inventory.item.BasicItemView import BasicItemView
from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItem import DownloadableItem
from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItemView import DownloadableItemView
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.request.MultipartRequestParams import MultipartRequestParams
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FilePathData import FilePathData
from org.allbinary.logic.io.file.FileUtil import FileUtil
from org.allbinary.logic.io.file.zip.ZipFileUtil import ZipFileUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.apache.commons.fileupload.FileItem import FileItem



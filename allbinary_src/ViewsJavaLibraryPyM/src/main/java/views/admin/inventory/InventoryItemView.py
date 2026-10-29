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

from org.allbinary.logic.communication.http.request.RequestMapInterface import RequestMapInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class InventoryItemView(HttpStoreComponentView, RequestMapInterface):
    TYPE_ID: int = 10

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        self.request: HttpServletRequest = None
        self.imageFileName: str = None
        self.mediaData: MediaData = None
        self.itemInterface: ItemInterface = None
        self.downloadableItemVector: BasicArrayList = None
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
        return InventoryItemView.TYPE_ID
    

    # throws Exception
    def getFormData(self) -> None:
        self.setRequestHashMap(MultipartRequestParams(self.request).toHashMap())
        imageFileItemObject: object = self.getRequestHashMap().get(self.basicItemData.IMAGE)
        if HttpFileUploadUtil.getInstance().isValid(imageFileItemObject):
            fileItem: FileItem = imageFileItemObject
            if fileItem is not None and fileItem.getSize() > 1:
                self.imageFileName = HttpRequestUtil.getInstance().generateFileName(fileItem.getName())
                pathData: AbPathData = AbPathData.getInstance()
                pathUtil: PathUtil = PathUtil.getInstance()
                self.mediaData = MediaData.get(pathData.getExtension(self.imageFileName))
                self.imageFileName = pathUtil.getWithoutExtension(self.imageFileName)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("Uploaded File Data: ")
                    stringBuffer.append(self.imageFileName)
                    stringBuffer.append(" Extension: ")
                    stringBuffer.append(self.mediaData.getName())
                    self.logUtil.putF(str(stringBuffer), self, "getFormData()")
        self.itemInterface = BasicItem(self.getRequestHashMap())
    

    def addDomNodeInterfaces(self) -> None:
        vector: BasicArrayList = BasicArrayListD()
        downloadableItem: DownloadableItem = None
        size: int = self.downloadableItemVector.size()
        for index in range(0, size):
            downloadableItem = self.downloadableItemVector.get(index)
            vector.add(DownloadableItemView(downloadableItem))
        self.addDomNodeInterface(BasicItemView(self.itemInterface, vector))
    

    def getItemInterface(self) -> ItemInterface:
        return self.itemInterface
    

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
    def processImageFiles(self) -> None:
        from views.admin.inventory.InventoryUploadMediaUtil import InventoryUploadMediaUtil
        set: Set = self.getRequestHashMap().keySet()
        fieldNameArray: list[object] = set.toArray()
        size: int = len(fieldNameArray)
        for index in range(0, size):
            fieldName: str = fieldNameArray[index]
            if ((fieldName > self.basicItemData.IMAGE) - (fieldName < self.basicItemData.IMAGE)) == 0:
                storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.getWeblisketSession().getStoreName())
                inventoryUploadMediaUtil: InventoryUploadMediaUtil = InventoryUploadMediaUtil(storeFrontInterface, self.itemInterface)
                fileItem: FileItem = self.getRequestHashMap().get(self.basicItemData.IMAGE)
                self.itemInterface = inventoryUploadMediaUtil.saveFiles(fileItem.get(), self.imageFileName, self.mediaData)
    

    def setRequestHashMap(self, requestHashMap: dict) -> None:
        self.requestHashMap = requestHashMap
    

    def getRequestHashMap(self) -> dict:
        return self.requestHashMap
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.inventory.item.BasicItem import BasicItem
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.business.user.commerce.inventory.item.BasicItemView import BasicItemView
from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItem import DownloadableItem
from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItemView import DownloadableItemView
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.file.upload.HttpFileUploadUtil import HttpFileUploadUtil
from org.allbinary.logic.communication.http.request.HttpRequestUtil import HttpRequestUtil
from org.allbinary.logic.communication.http.request.MultipartRequestParams import MultipartRequestParams
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.io.path.PathUtil import PathUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.visual.media.MediaData import MediaData
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.apache.commons.fileupload.FileItem import FileItem



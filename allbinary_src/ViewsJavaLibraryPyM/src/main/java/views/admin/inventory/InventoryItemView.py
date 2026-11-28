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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.communication.http.request.RequestMapInterface import RequestMapInterface
from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


@java_inherited_overloads
class InventoryItemView(*java_bases(HttpStoreComponentView, RequestMapInterface)):
    TYPE_ID: int = 10
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("basicItemData", None)
        vars(self).setdefault("request", None)
        vars(self).setdefault("imageFileName", None)
        vars(self).setdefault("mediaData", None)
        vars(self).setdefault("itemInterface", None)
        vars(self).setdefault("downloadableItemVector", None)
        vars(self).setdefault("requestHashMap", None)

    def _init_fields(self) -> None:
        from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        if "request" not in vars(self): self.request: HttpServletRequest = None
        if "imageFileName" not in vars(self): self.imageFileName: str = None
        if "mediaData" not in vars(self): self.mediaData: MediaData = None
        if "itemInterface" not in vars(self): self.itemInterface: ItemInterface = None
        if "downloadableItemVector" not in vars(self): self.downloadableItemVector: BasicArrayList = None
        if "requestHashMap" not in vars(self): self.requestHashMap: HashMap = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 2:
            __class__._constructor2(self, *args)
    

    def _constructor1(self, transformInfoInterface: TransformInfoInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface)
        __class__._init_fields(self)
        self.request = self.getPageContext().getRequest()
        self.getFormData()
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, empty: str) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface)
        __class__._init_fields(self)
        self.request = self.getPageContext().getRequest()
    

    def getTypeId(self) -> int:
        return InventoryItemView.TYPE_ID
    

    # throws Exception
    def getFormData(self) -> None:
        from org.allbinary.business.user.commerce.inventory.item.BasicItem import BasicItem
        from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
        from org.allbinary.logic.communication.http.file.upload.HttpFileUploadUtil import HttpFileUploadUtil
        from org.allbinary.logic.communication.http.request.HttpRequestUtil import HttpRequestUtil
        from org.allbinary.logic.communication.http.request.MultipartRequestParams import MultipartRequestParams
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.io.path.PathUtil import PathUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.visual.media.MediaData import MediaData
        from org.apache.commons.fileupload.FileItem import FileItem
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("Uploaded File Data: ")
                    stringBuffer.append(self.imageFileName)
                    stringBuffer.append(" Extension: ")
                    stringBuffer.append(self.mediaData.getName())
                    self.logUtil.putF(str(stringBuffer), self, "getFormData()")
        self.itemInterface = BasicItem(self.getRequestHashMap())
    

    def addDomNodeInterfaces(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.user.commerce.inventory.item.BasicItemView import BasicItemView
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItem import DownloadableItem
        from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItemView import DownloadableItemView
        vector: BasicArrayList = BasicArrayListD()
        downloadableItem: DownloadableItem = None
        size: int = self.downloadableItemVector.size()
        for index in range(0, size):
            downloadableItem = self.downloadableItemVector.get(index)
            vector.add(DownloadableItemView(downloadableItem))
        self.addDomNodeInterface(BasicItemView(self.itemInterface, vector))
    

    def getItemInterface(self) -> ItemInterface:
        from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
        return self.itemInterface
    

    # throws Exception
    def view(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            self.addDomNodeInterfaces()
            return java_super_call(super(), "view")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            raise e
    

    # throws Exception
    def processImageFiles(self) -> None:
        from views.admin.inventory.InventoryUploadMediaUtil import InventoryUploadMediaUtil
        from java.util.Set import Set
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.apache.commons.fileupload.FileItem import FileItem
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
    

    def setRequestHashMap(self, requestHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        self.requestHashMap = requestHashMap
    

    def getRequestHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        return self.requestHashMap
# from java.util.HashMap import HashMap
# from java.util.Set import Set
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.user.commerce.inventory.item.BasicItem import BasicItem
# from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
# from org.allbinary.business.user.commerce.inventory.item.BasicItemView import BasicItemView
# from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
# from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItem import DownloadableItem
# from org.allbinary.business.user.commerce.inventory.item.download.DownloadableItemView import DownloadableItemView
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.http.file.upload.HttpFileUploadUtil import HttpFileUploadUtil
# from org.allbinary.logic.communication.http.request.HttpRequestUtil import HttpRequestUtil
# from org.allbinary.logic.communication.http.request.MultipartRequestParams import MultipartRequestParams
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.io.path.PathUtil import PathUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.visual.media.MediaData import MediaData
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.apache.commons.fileupload.FileItem import FileItem
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



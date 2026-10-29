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
# package org.allbinary.business.backup

from __future__ import annotations



class BlisketBackupFactory:
    instance: BlisketBackupFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.directory: Directory = Directory.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BlisketBackupFactory:
        return BlisketBackupFactory.instance
    

    # throws Exception
    def getFileBasicArrayList(self, pathString: str) -> BasicArrayList:
        path: AbPath = AbPath(pathString, self.stringUtil.EMPTY_STRING)
        file: AbFile = AbFile.createAbFileFromAbPath(path)
        return self.directory.search(file, True)
    

    def backup(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, "backup()")
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.URLGLOBALS.getWebappPath())
            stringBuffer.append(self.PATH_GLOBALS.getInstance().BACKUP_PATH)
            backupPath: str = str(stringBuffer)
            path: AbPath = AbPath(backupPath, self.stringUtil.EMPTY_STRING)
            fileBasicArrayList: BasicArrayList = self.getFileBasicArrayList(backupPath)
            self.backup(fileBasicArrayList, str(path.toFileSystemString()) + "backup.zip")
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "backup()", e)
    

    def backupViews(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, "backupViews()")
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.URLGLOBALS.getWebappPath())
            stringBuffer.append(self.PATH_GLOBALS.getInstance().BACKUP_PATH)
            backupPath: str = str(stringBuffer)
            path: AbPath = AbPath(backupPath, self.stringUtil.EMPTY_STRING)
            fileBasicArrayList: BasicArrayList = BasicArrayListD()
            storeFrontsEntity: StoreFrontsEntity = StoreFrontsEntityFactory.getInstance().getStoreFrontsEntityInstance()
            storeFrontNamesBasicArrayList: BasicArrayList = storeFrontsEntity.getStoreFrontNames()
            size: int = storeFrontNamesBasicArrayList.size()
            nextStore: str = None
            viewsPath: str = None
            for index in range(0, size):
                nextStore = storeFrontNamesBasicArrayList.get(index)
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(self.URLGLOBALS.getWebappPath())
                stringBuffer.append(self.PATH_GLOBALS.getInstance().VIEWS_PATH)
                stringBuffer.append(nextStore)
                viewsPath = str(stringBuffer)
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append("Backup Store Views: ")
                stringBuffer.append(nextStore)
                stringBuffer.append(" from: ")
                stringBuffer.append(viewsPath)
                PreLogUtil.put(str(stringBuffer), self, "backupViews()")
                fileBasicArrayList.addAllList(self.getFileBasicArrayList(viewsPath))
            self.backup(fileBasicArrayList, str(path.toFileSystemString()) + "backupViews.zip")
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "backupViews()", e)
    

    def backupResources(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, "backupResources()")
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.URLGLOBALS.getWebappPath())
            stringBuffer.append(self.PATH_GLOBALS.getInstance().BACKUP_PATH)
            backupPath: str = str(stringBuffer)
            path: AbPath = AbPath(backupPath, self.stringUtil.EMPTY_STRING)
            fileBasicArrayList: BasicArrayList = BasicArrayListD()
            storeFrontsEntity: StoreFrontsEntity = StoreFrontsEntityFactory.getInstance().getStoreFrontsEntityInstance()
            storeFrontNamesBasicArrayList: BasicArrayList = storeFrontsEntity.getStoreFrontNames()
            size: int = storeFrontNamesBasicArrayList.size()
            nextStore: str = None
            storeFrontInterface: StoreFrontInterface = None
            resourcesPath: str = None
            for index in range(0, size):
                nextStore = storeFrontNamesBasicArrayList.get(index)
                storeFrontInterface = storeFrontsEntity.getStoreFrontInterface(nextStore)
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(self.URLGLOBALS.getWebappPath())
                stringBuffer.append(storeFrontInterface.getCurrentHostNamePath())
                stringBuffer.append(storeFrontInterface.getCategoryPath())
                resourcesPath = str(stringBuffer)
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append("Backup Store Resrouces: ")
                stringBuffer.append(nextStore)
                stringBuffer.append(" from: ")
                stringBuffer.append(resourcesPath)
                PreLogUtil.put(str(stringBuffer), self, "backupResources()")
                fileBasicArrayList.addAllList(self.getFileBasicArrayList(resourcesPath))
            self.backup(fileBasicArrayList, str(path.toFileSystemString()) + "backupResources.zip")
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "backupResources()", e)
    

    def backupJsps(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, "backupJsps()")
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.URLGLOBALS.getWebappPath())
            stringBuffer.append(self.PATH_GLOBALS.getInstance().BACKUP_PATH)
            backupPath: str = str(stringBuffer)
            path: AbPath = AbPath(backupPath, self.stringUtil.EMPTY_STRING)
            fileBasicArrayList: BasicArrayList = BasicArrayListD()
            storeFrontsEntity: StoreFrontsEntity = StoreFrontsEntityFactory.getInstance().getStoreFrontsEntityInstance()
            storeFrontNamesBasicArrayList: BasicArrayList = storeFrontsEntity.getStoreFrontNames()
            size: int = storeFrontNamesBasicArrayList.size()
            nextStore: str = None
            for index in range(0, size):
                nextStore = storeFrontNamesBasicArrayList.get(index)
                PreLogUtil.put("Backup Store Jsps: " + nextStore, self, "backupJsps()")
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(self.URLGLOBALS.getWebappPath())
                stringBuffer.append(nextStore)
                fileBasicArrayList.addAllList(self.getFileBasicArrayList(str(stringBuffer)))
            self.backup(fileBasicArrayList, str(path.toFileSystemString()) + "backupJsps.zip")
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "backupJsps()", e)
    

    # Java overloaded method: Python keeps the last definition
    def backup(self, fileBasicArrayList: BasicArrayList, zipFile: str) -> None:
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append("ZipFile: ")
            stringBuffer.append(zipFile)
            stringBuffer.append(" BasicArrayList: ")
            stringBuffer.appendint(fileBasicArrayList.size())
            PreLogUtil.put("Creating Backup Zip File: " + str(stringBuffer), self, "backup()")
            ZipFileUtil.getInstance().create(zipFile, fileBasicArrayList)
            self.logUtil.putF("Created Backup Zip File", self, "backup()")
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "backup()", e)
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.data.tables.context.module.storefronts.StoreFrontsEntity import StoreFrontsEntity
from org.allbinary.data.tables.context.module.storefronts.StoreFrontsEntityFactory import StoreFrontsEntityFactory
from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.directory.Directory import Directory
from org.allbinary.logic.io.file.zip.ZipFileUtil import ZipFileUtil
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


BlisketBackupFactory.instance = BlisketBackupFactory()


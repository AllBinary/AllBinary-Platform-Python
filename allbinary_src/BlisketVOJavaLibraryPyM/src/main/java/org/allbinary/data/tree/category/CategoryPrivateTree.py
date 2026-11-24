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
# package org.allbinary.data.tree.category

from __future__ import annotations

import threading


class CategoryPrivateTree:
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.categoryFactoryInterface: CategoryFactoryInterface = None
    

    def __init__(self, categoryFactoryInterface: CategoryFactoryInterface) -> None:
        from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        self._init_fields()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORY):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, "CategoryPrivateTree(CategoryFactoryInterface categoryFactoryInterface)")
        self.categoryFactoryInterface = categoryFactoryInterface
    

    # throws Exception
    def save(self, categoryInterface: CategoryInterface) -> None:
        with self._lock:
            return self._save_unlocked(categoryInterface)

    def _save_unlocked(self, categoryInterface: CategoryInterface) -> None:
        from org.allbinary.business.category.CategoryComponent import CategoryComponent
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.logic.control.crypt.file.CryptFileWriter import CryptFileWriter
        from org.w3c.dom.Document import Document
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
            self.logUtil.putF("Saving Category File: " + str(categoryInterface.getFilePath()), self, "save()")
        document: Document = CategoryComponent(categoryInterface).toXmlDoc()
        cryptFileWriter: CryptFileWriter = CryptFileWriter(CategoryData.getInstance().UNCRYPTED_EXTENSION, CategoryData.getInstance().ENCRYPTED_EXTENSION)
        cryptFileWriter.write(categoryInterface.getFilePath(), document)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
            self.logUtil.putF("end", self, "save()")
    

    # throws Exception
    def delete(self, categoryInterface: CategoryInterface) -> None:
        with self._lock:
            return self._delete_unlocked(categoryInterface)

    def _delete_unlocked(self, categoryInterface: CategoryInterface) -> None:
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if categoryInterface.isLeaf():
            categoryFile: AbFile = AbFile.createAbFileFromAbPath(categoryInterface.getFilePath())
            if categoryFile.delete():
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF("Removed: " + str(categoryInterface.getFilePath()), self, "delete(CategoryInterface)")
        else:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF("Not a leaf unable to remove", self, "delete(CategoryInterface)")
# from org.allbinary.business.category.CategoryComponent import CategoryComponent
# from org.allbinary.business.category.CategoryData import CategoryData
# from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
# from org.allbinary.business.category.CategoryInterface import CategoryInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.crypt.file.CryptFileWriter import CryptFileWriter
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



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
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.category.CategoryPrivateTree import CategoryPrivateTree
from org.allbinary.data.tree.category.CategoryModifierTreeInterface import CategoryModifierTreeInterface


class CategoryModifierTree(*java_bases(CategoryPrivateTree, CategoryModifierTreeInterface)):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.io.file.directory.Directory import Directory
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.directory: Directory = Directory.getInstance()
    

    def __init__(self, categoryFactoryInterface: CategoryFactoryInterface) -> None:
        from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__(categoryFactoryInterface)
        self._init_fields()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF(self.commonStrings.START, self, "CategoryModifierTree(CategoryFactoryInterface categoryFactoryInterface)")
    

    def insert(self, parentCategoryInterface: CategoryInterface, newChildCategoryInterface: CategoryInterface) -> None:
        with self._lock:
            return self._insert_unlocked(parentCategoryInterface, newChildCategoryInterface)

    def _insert_unlocked(self, parentCategoryInterface: CategoryInterface, newChildCategoryInterface: CategoryInterface) -> None:
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORY):
                self.logUtil.putF("Inserting", self, "insert()")
            if parentCategoryInterface.isValid():
                parentCategoryInterface.addChild(newChildCategoryInterface)
                directoryToBeCreatedAbPath: AbPath = AbPath(str(newChildCategoryInterface.getRootFilePath()) + str(newChildCategoryInterface.getPath()), StringUtil.getInstance().EMPTY_STRING)
                self.directory.create(directoryToBeCreatedAbPath)
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORY):
                    self.logUtil.putF("Saving", self, "insert()")
                self.save(parentCategoryInterface)
                self.save(newChildCategoryInterface)
            else:
                raise Exception("Will Not Add Null Category")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "insert", e)
    

    def delete(self, parentCategoryInterface: CategoryInterface, existingChildCategoryInterface: CategoryInterface) -> None:
        with self._lock:
            return self._delete_unlocked(parentCategoryInterface, existingChildCategoryInterface)

    def _delete_unlocked(self, parentCategoryInterface: CategoryInterface, existingChildCategoryInterface: CategoryInterface) -> None:
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if parentCategoryInterface.isValid():
                parentCategoryInterface.addChild(existingChildCategoryInterface)
                directoryToBeDeletedAbPath: AbPath = AbPath(str(existingChildCategoryInterface.getRootFilePath()) + str(existingChildCategoryInterface.getPath()), StringUtil.getInstance().EMPTY_STRING)
                self.delete(existingChildCategoryInterface)
                parentCategoryInterface.removeChild(existingChildCategoryInterface)
                self.save(parentCategoryInterface)
                self.directory.remove(directoryToBeDeletedAbPath)
            else:
                raise Exception("Will Not Add Null Category")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.delete, e)
# from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
# from org.allbinary.business.category.CategoryInterface import CategoryInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.file.directory.Directory import Directory
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes



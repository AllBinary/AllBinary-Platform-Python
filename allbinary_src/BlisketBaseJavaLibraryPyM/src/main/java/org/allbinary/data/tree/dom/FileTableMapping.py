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
# package org.allbinary.data.tree.dom

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface


class FileTableMapping(TableMappingInterface):

    def _init_fields(self) -> None:
        self.file: AbFile = None
    

    def __init__(self, file: AbFile) -> None:
        self._init_fields()
        self.file = file
    

    # throws Exception
    def getKey(self) -> object:
        return self.file.getPath()
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        filePropertyVector: BasicArrayList = BasicArrayListD()
        filePropertyVector.add(self.file.getAbsolutePath())
        filePropertyVector.add(self.file.getCanonicalPath())
        filePropertyVector.add(self.file.getName())
        filePropertyVector.add(self.file.getParent())
        filePropertyVector.add(self.file.getPath())
        return filePropertyVector
    

    # throws Exception
    def toHashMap(self) -> dict:
        filePropertyHashMap: dict = StdUtil.getInstance().createHashMap()
        pathData: AbPathData = AbPathData.getInstance()
        pathUtil: PathUtil = PathUtil.getInstance()
        rootFileName: str = pathData.getNameFromPath(pathUtil.getWithoutExtension(self.file.getPath()))
        fileData: FileData = FileData.getInstance()
        filePropertyHashMap.put(fileData.ROOT_NAME, rootFileName)
        filePropertyHashMap.put(fileData.ISFILE, str(str(self.file.isFile())))
        filePropertyHashMap.put(fileData.ISDIRECTORY, str(str(self.file.isDirectory())))
        filePropertyHashMap.put(fileData.ISHIDDEN, str(str(self.file.isHidden())))
        filePropertyHashMap.put(fileData.ISABSOLUTE, str(str(self.file.isAbsolute())))
        filePropertyHashMap.put(fileData.ABSOLUTE_PATH, self.file.getAbsolutePath())
        filePropertyHashMap.put(fileData.CANONICAL_PATH, self.file.getCanonicalPath())
        filePropertyHashMap.put(fileData.NAME, self.file.getName())
        filePropertyHashMap.put(fileData.PARENT, self.file.getParent())
        filePropertyHashMap.put(fileData.PATH, self.file.getPath())
        return filePropertyHashMap
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FileData import FileData
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.io.path.PathUtil import PathUtil



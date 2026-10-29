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
# package org.allbinary.logic.io.file.filter

from __future__ import annotations



class BasicFileFilterUtil:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance(extension: str) -> FileFilter:
        from org.allbinary.logic.io.file.filter.VisitorFileFilter import VisitorFileFilter
        vector: BasicArrayList = BasicArrayListD()
        vector.add(extension)
        includeFileExtensionsBooleanFileVisitor: IncludeFileExtensionsBooleanFileVisitor = IncludeFileExtensionsBooleanFileVisitor(vector)
        return VisitorFileFilter(includeFileExtensionsBooleanFileVisitor)
# from java.io.FileFilter import FileFilter
from org.allbinary.logic.io.file.visitor.IncludeFileExtensionsBooleanFileVisitor import IncludeFileExtensionsBooleanFileVisitor
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD



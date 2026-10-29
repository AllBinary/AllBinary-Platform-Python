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
# package org.allbinary.logic.system.loader

from __future__ import annotations

import gc


class NativeLibraryHelperWrapper:

    def _init_fields(self) -> None:
        self.libraryName: str = None
        self.loader: ClassLoader = None
        self.anyType: object = None
    

    def __init__(self, libraryName: str) -> None:
        self._init_fields()
        self.setLibraryName(libraryName)
    

    # throws Exception
    def load(self) -> None:
        from org.allbinary.logic.system.loader.NativeLibraryClassLoader import NativeLibraryClassLoader
        params: list[object] = [None] * (1)
        params[0] = self.getLibraryName()
        classes: list[type] = [None] * (1)
        classes[0] = type(self.getLibraryName())
        self.loader = NativeLibraryClassLoader(type(self).getClassLoader())
        myClass: type = self.loader.loadClass("dynamic.NativeLibraryHelper")
        constructor: Constructor = myClass.getConstructor(classes)
        self.anyType = constructor.newInstance(params)
        commonStrings: CommonStrings = CommonStrings.getInstance()
        method: Method = type(self.anyType).getMethod(commonStrings.LOAD, None)
        method.invoke(self.anyType, None)
    

    def unload(self) -> None:
        self.anyType = None
        self.loader = None
        gc.collect()
        gc.collect()
    

    def toString(self) -> str:
        return "Library: " + str(self.getLibraryName())

    def __str__(self) -> str:
        return self.toString()
    

    def getLibraryName(self) -> str:
        return self.libraryName
    

    def setLibraryName(self, libraryName: str) -> None:
        self.libraryName = libraryName
# from java.lang.reflect.Constructor import Constructor
# from java.lang.reflect.Method import Method
from org.allbinary.string.CommonStrings import CommonStrings



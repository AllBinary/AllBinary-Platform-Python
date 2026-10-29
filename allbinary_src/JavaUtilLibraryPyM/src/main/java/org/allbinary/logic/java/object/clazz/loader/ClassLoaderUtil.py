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
# package org.allbinary.logic.java.anyType.clazz.loader

from __future__ import annotations



class ClassLoaderUtil:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getName(anyType: object) -> str:
        classLoader: ClassLoader = type(anyType).getClassLoader()
        if classLoader is not None:
            return "ClassLoader: " + type(classLoader).__module__ + "." + type(classLoader).__qualname__
        raise Exception("Unable to get ClassLoader")



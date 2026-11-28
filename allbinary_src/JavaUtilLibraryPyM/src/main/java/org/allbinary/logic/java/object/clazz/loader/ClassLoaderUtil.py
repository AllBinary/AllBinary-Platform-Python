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

from java.lang.ClassLoader import ClassLoader


class ClassLoaderUtil:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getName(anyType: object) -> str:
        classLoader: ClassLoader = __import__("java.lang.ClassLoader", fromlist=["ClassLoader"]).ClassLoader.getSystemClassLoader()
        if classLoader is not None:
            return "ClassLoader: " + __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(classLoader))
        raise Exception("Unable to get ClassLoader")



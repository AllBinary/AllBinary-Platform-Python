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
# package org.allbinary.logic.visual.transform.info

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.visual.transform.info.TransformInfoFactoryInterface import TransformInfoFactoryInterface


class TransformInfoHttpStoreFactory(TransformInfoFactoryInterface):
    instance: TransformInfoHttpStoreFactory = None
    

    @staticmethod
    def getInstance_j0() -> TransformInfoHttpStoreFactory:
        return TransformInfoHttpStoreFactory.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def getInstance_j3(self, databaseHashMap: HashMap, propertiesHashMap: HashMap, pageContext: PageContext) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpStore import TransformInfoHttpStore
        from java.util.HashMap import HashMap
        return TransformInfoHttpStore(databaseHashMap, propertiesHashMap, pageContext)

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext


def _TransformInfoHttpStoreFactory_instance() -> object:
    return TransformInfoHttpStoreFactory()

lazy_static(TransformInfoHttpStoreFactory, "instance", _TransformInfoHttpStoreFactory_instance)


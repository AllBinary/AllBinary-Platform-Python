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

from org.allbinary.logic.visual.transform.info.TransformInfoFactoryInterface import TransformInfoFactoryInterface


class TransformInfoHttpStoreFactory(TransformInfoFactoryInterface):
    instance: TransformInfoHttpStoreFactory = None
    

    @staticmethod
    def getInstance() -> TransformInfoHttpStoreFactory:
        return TransformInfoHttpStoreFactory.instance
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, databaseHashMap: dict, propertiesHashMap: dict, pageContext: PageContext) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpStore import TransformInfoHttpStore
        return TransformInfoHttpStore(databaseHashMap, propertiesHashMap, pageContext)
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext


TransformInfoHttpStoreFactory.instance = TransformInfoHttpStoreFactory()


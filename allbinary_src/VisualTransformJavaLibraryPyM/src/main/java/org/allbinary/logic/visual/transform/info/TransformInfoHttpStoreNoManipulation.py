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

from org.allbinary.logic.visual.transform.info.TransformInfoHttpStore import TransformInfoHttpStore


class TransformInfoHttpStoreNoManipulation(TransformInfoHttpStore):
    

    def __init__(self, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__(propertiesHashMap, pageContext)
    

    # throws Exception
    def setObjectConfigFile(self, value: str) -> None:
        self.setObjectConfigFileName(value)
        self.setObjectConfigInterface(TransformInfoObjectConfigNoManipulationFactory.getInstance().getInstance(self, self.getObjectConfigFilePath()))
    

    # throws Exception
    def setObjectConfig(self, value: str) -> None:
        raise Exception("Should not set from config")
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigNoManipulationFactory import TransformInfoObjectConfigNoManipulationFactory



# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.logic.visual.transform.info.objectConfig

from __future__ import annotations

from org.allbinary.logic.visual.transform.info.objectConfig.TransformInfoObjectConfigAndManipulatorFactoryInterface import TransformInfoObjectConfigAndManipulatorFactoryInterface


class TransformInfoObjectConfigAndManipulatorFactoryBase(TransformInfoObjectConfigAndManipulatorFactoryInterface):

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getInstance(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, objectConfigFileAbPath: AbPath) -> TransformInfoObjectConfigInterface:
        raise RuntimeError()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> TransformInfoObjectConfigInterface:
        raise RuntimeError()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, document: Document) -> TransformInfoObjectConfigInterface:
        raise RuntimeError()
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document



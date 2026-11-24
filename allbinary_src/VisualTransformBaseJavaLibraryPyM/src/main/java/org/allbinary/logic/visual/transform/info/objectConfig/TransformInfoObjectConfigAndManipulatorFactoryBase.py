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
        from org.allbinary.string.CommonStrings import CommonStrings
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_1(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, objectConfigFileAbPath: AbPath) -> TransformInfoObjectConfigInterface:
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        raise RuntimeError()
    

    # throws Exception
    def getInstance_j2(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> TransformInfoObjectConfigInterface:
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        raise RuntimeError()
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_2(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, document: Document) -> TransformInfoObjectConfigInterface:
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.w3c.dom.Document import Document
        raise RuntimeError()

    def getInstance(self, *args):
        if len(args) == 3 and True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and not isinstance(args[2], (str, list, int, float)):
            return self.getInstance_j3_1(*args)
        if len(args) == 3:
            return self.getInstance_j3_2(*args)
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document



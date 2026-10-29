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
# package org.allbinary.logic.visual.transform.info.objectConfig

from __future__ import annotations

from org.allbinary.logic.visual.transform.info.objectConfig.GenericStoreTransformInfoObjectConfig import GenericStoreTransformInfoObjectConfig


class OverrideStoreTransformInfoObjectConfig(GenericStoreTransformInfoObjectConfig):

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 4:
            self._constructor4(*args)
    

    def _constructor2(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(abeClientInformation, transformInfoInterface)
    

    def _constructor3(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, document: Document) -> None:
        super().__init__(abeClientInformation, transformInfoInterface, document)
        self.setDocument(self.generate(self.toXmlDoc()))
    

    def _constructor4(self, abeClientInformation: AbeClientInformationInterface, transformInfoInterface: TransformInfoInterface, name: str, type_: str) -> None:
        super().__init__(abeClientInformation, transformInfoInterface, name, type_)
        self.setDocument(self.generate(self.toXmlDoc()))
    

    # throws Exception
    def generate(self, objectConfigDocument: Document) -> Document:
        newObjectConfigDocument: Document = super().generate(objectConfigDocument)
        return newObjectConfigDocument
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document



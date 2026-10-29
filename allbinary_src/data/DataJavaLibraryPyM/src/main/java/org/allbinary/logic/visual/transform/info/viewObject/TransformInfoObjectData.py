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
# package org.allbinary.logic.visual.transform.info.viewObject

from __future__ import annotations



class TransformInfoObjectData:
    instance: TransformInfoObjectData = None

    def _init_fields(self) -> None:
        self.UNCRYPTED_EXTENSION: str = "class"
        self.ENCRYPTED_EXTENSION: str = "abw"
    

    @staticmethod
    def getInstance() -> TransformInfoObjectData:
        return TransformInfoObjectData.instance
    

    def __init__(self) -> None:
        self._init_fields()


TransformInfoObjectData.instance = TransformInfoObjectData()


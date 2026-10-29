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



class TransformInfosData:
    instance: TransformInfosData = None

    def _init_fields(self) -> None:
        self.NAME: str = "TRANSFORM_INFOS_NAME"
        self.GROUP: str = "TRANSFORM_INFOS_GROUP"
        self.ALL: str = "TRANSFORM_INFOS_ALL"
        self.PREVIEW: str = "TRANSFORM_INFOS_PREVIEW"
        self.SMALL_PREVIEW: str = "TRANSFORM_INFOS_SMALL_PREVIEW"
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> TransformInfosData:
        return TransformInfosData.instance


TransformInfosData.instance = TransformInfosData()


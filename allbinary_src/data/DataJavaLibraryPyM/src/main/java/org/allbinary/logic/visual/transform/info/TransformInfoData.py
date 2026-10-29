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



class TransformInfoData:
    instance: TransformInfoData = None

    def _init_fields(self) -> None:
        self.PARENT: str = "TRANSFORM_INFO_PARENT"
        self.MAPPED: str = "TRANSFORM_INFO_MAPPED"
        self.NAME: str = "TRANSFORM_INFO_NAME"
        self.DESCRIPTION: str = "TRANSFORM_INFO_DESCRIPTION"
        self.CATEGORY: str = "TRANSFORM_INFO_CATEGORY"
        self.OBJECTFILENAME: str = "TRANSFORM_INFO_OBJECTFILENAME"
        self.OBJECT: str = "TRANSFORM_INFO_OBJECT"
        self.OBJECTCONFIGFILENAME: str = "TRANSFORM_INFO_OBJECTCONFIGFILENAME"
        self.OBJECTCONFIG: str = "TRANSFORM_INFO_OBJECTCONFIG"
        self.TEMPLATEFILENAME: str = "TRANSFORM_INFO_TEMPLATEFILENAME"
        self.TEMPLATE: str = "TRANSFORM_INFO_TEMPLATE"
        self.DATAFILENAME: str = "TRANSFORM_INFO_DATAFILENAME"
        self.DATA: str = "TRANSFORM_INFO_DATA"
        self.LABEL: str = "TRANSFORM_INFO_LABEL"
        self.OWNER: str = "OWNER_" + self.NAME
        self.PARTIAL: str = "PARTIAL_" + self.NAME
    

    @staticmethod
    def getInstance() -> TransformInfoData:
        return TransformInfoData.instance
    

    def __init__(self) -> None:
        self._init_fields()


TransformInfoData.instance = TransformInfoData()


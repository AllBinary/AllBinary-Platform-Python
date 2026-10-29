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
# package org.allbinary.logic.visual.transform.template

from __future__ import annotations



class XslData:
    instance: XslData = None

    def _init_fields(self) -> None:
        self.NAME: str = "XSL_NAME"
        self.ROOT_IMPORT_URI: str = "ROOT_IMPORT_URI"
    

    @staticmethod
    def getInstance() -> XslData:
        return XslData.instance
    

    def __init__(self) -> None:
        self._init_fields()


XslData.instance = XslData()


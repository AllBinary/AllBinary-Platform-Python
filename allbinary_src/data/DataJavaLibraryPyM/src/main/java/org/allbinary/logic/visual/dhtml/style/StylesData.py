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
# package org.allbinary.logic.visual.dhtml.style

from __future__ import annotations



class StylesData:
    instance: StylesData = None

    def _init_fields(self) -> None:
        self.NAME: str = "STYLES_NAME"
    

    @staticmethod
    def getInstance() -> StylesData:
        return StylesData.instance
    

    def __init__(self) -> None:
        self._init_fields()


StylesData.instance = StylesData()


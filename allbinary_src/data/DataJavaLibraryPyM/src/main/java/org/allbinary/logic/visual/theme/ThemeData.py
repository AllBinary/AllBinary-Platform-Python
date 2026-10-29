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
# package org.allbinary.logic.visual.theme

from __future__ import annotations



class ThemeData:
    instance: ThemeData = None

    def _init_fields(self) -> None:
        self.NAME: str = "THEME_NAME"
        self.PATH: str = "THEME_PATH"
        self.PREVIEW_IMAGE_NAME: str = "THEME_PREVIEW_IMAGE_NAME"
        self.PREVIEW_IMAGE_PATH: str = "THEME_PREVIEW_IMAGE_PATH"
    

    @staticmethod
    def getInstance() -> ThemeData:
        return ThemeData.instance
    

    def __init__(self) -> None:
        self._init_fields()


ThemeData.instance = ThemeData()


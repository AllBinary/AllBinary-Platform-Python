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
# package org.allbinary.logic.visual.transform.template.customizer.widgets.title

from __future__ import annotations



class TitleData:
    instance: TitleData = None

    def _init_fields(self) -> None:
        self.NAME: str = "TITLE_NAME"
        self.TEXT: str = "TITLE_TEXT"
        self.VIEWNAMEKEY: str = "Title"
        self.MAXLEN: int = 255
    

    @staticmethod
    def getInstance() -> TitleData:
        return TitleData.instance
    

    def __init__(self) -> None:
        self._init_fields()


TitleData.instance = TitleData()


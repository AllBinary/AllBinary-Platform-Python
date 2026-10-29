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
# package org.allbinary.logic.visual.dhtml.style.css.property.color.background

from __future__ import annotations



class BackgroundColorData:
    instance: BackgroundColorData = None

    def _init_fields(self) -> None:
        self.VALUE: str = "background-color"
    

    @staticmethod
    def getInstance() -> BackgroundColorData:
        return BackgroundColorData.instance
    

    def __init__(self) -> None:
        self._init_fields()


BackgroundColorData.instance = BackgroundColorData()


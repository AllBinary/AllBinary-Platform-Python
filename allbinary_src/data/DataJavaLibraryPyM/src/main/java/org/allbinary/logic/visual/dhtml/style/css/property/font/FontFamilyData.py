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
# package org.allbinary.logic.visual.dhtml.style.css.property.font

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class FontFamilyData:
    instance: FontFamilyData = None

    def _init_fields(self) -> None:
        self.NAME: str = "FONT_FAMILY_NAME"
        self.VALUE: str = "font-family"
    

    @staticmethod
    def getInstance() -> FontFamilyData:
        return FontFamilyData.instance
    

    def __init__(self) -> None:
        self._init_fields()


def _FontFamilyData_instance() -> object:
    return FontFamilyData()

lazy_static(FontFamilyData, "instance", _FontFamilyData_instance)


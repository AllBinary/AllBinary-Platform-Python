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
# package org.allbinary.logic.visual.dhtml.html.table

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class HtmlTableData:
    instance: HtmlTableData = None

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self.LEFT: str = CommonStrings.getInstance().LEFT
        self.RIGHT: str = CommonStrings.getInstance().RIGHT
        self.NONE: str = "none"
        self.TOP: str = "top"
        self.BOTTOM: str = "bottom"
        self.TOPBOT: str = "topbot"
        self.SIDES: str = "sides"
        self.ALL: str = "all"
        self.BORDERED: str = "border"
        self.BASIC: str = "basic"
        self.ROWS: str = "rows"
        self.FRAMES: list[str] = [self.NONE, self.TOP, self.BOTTOM, self.TOPBOT, self.SIDES, self.ALL, self.BORDERED]

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> HtmlTableData:
        return HtmlTableData.instance
# from org.allbinary.string.CommonStrings import CommonStrings


def _HtmlTableData_instance() -> object:
    return HtmlTableData()

lazy_static(HtmlTableData, "instance", _HtmlTableData_instance)


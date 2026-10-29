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
# package org.allbinary.logic.visual.dhtml.html.name

from __future__ import annotations



class HtmlNameMathData:
    instance: HtmlNameMathData = None

    def _init_fields(self) -> None:
        self.EQUALS: str = "_EQUALS_"
        self.PLUS: str = "_PLUS_"
        self.MINUS: str = "_MINUS_"
        self.DIVIDE: str = "_DIVIDE_"
        self.MULTIPLY: str = "_MULTIPLY_"
    

    @staticmethod
    def getInstance() -> HtmlNameMathData:
        return HtmlNameMathData.instance
    

    def __init__(self) -> None:
        self._init_fields()


HtmlNameMathData.instance = HtmlNameMathData()


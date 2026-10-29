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
# package org.allbinary.logic.visual.dhtml.html.input

from __future__ import annotations

from org.allbinary.logic.visual.dhtml.html.input.HtmlValueInput import HtmlValueInput


class HtmlRadioInput(HtmlValueInput):

    def _init_fields(self) -> None:
        self.CHECKED: str = "checked"
    

    def __init__(self, before: str, name: str, value: str, after: str) -> None:
        from org.allbinary.logic.visual.dhtml.html.input.HtmlInputData import HtmlInputData
        super().__init__(before, HtmlInputData.getInstance().RADIO, name, value, after)
        self._init_fields()
    

    def setSelected(self) -> None:
        super().addAttribute(self.CHECKED, BooleanFactory.getInstance().TRUE_STRING)
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory



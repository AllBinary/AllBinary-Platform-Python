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

from org.allbinary.logic.visual.dhtml.html.input.HtmlLengthInput import HtmlLengthInput


class HtmlTextInput(HtmlLengthInput):
    

    def __init__(self, before: str, name: str, value: str, after: str) -> None:
        from org.allbinary.logic.visual.dhtml.html.input.HtmlInputData import HtmlInputData
        super().__init__(before, HtmlInputData.getInstance().TEXT, name, value, after)
        self.setSize(int(19))
        self.setMaxLength(int(60))



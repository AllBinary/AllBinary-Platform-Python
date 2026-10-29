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

from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertyView import CssPropertyView


class FontFamilyView(CssPropertyView):

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        from org.allbinary.logic.visual.dhtml.style.css.property.font.FontFamilyData import FontFamilyData
        super().__init__(FontFamilyData.getInstance().VALUE)
    

    def _constructor1(self, node: Node) -> None:
        super().__init__(node)
from org.w3c.dom.Node import Node



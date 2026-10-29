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
# package org.allbinary.logic.visual.dhtml.html

from __future__ import annotations

from org.allbinary.logic.visual.dhtml.html.HtmlForm import HtmlForm


class HtmlPostForm(HtmlForm):
    

    def __init__(self, action: str) -> None:
        super().__init__(action)
        self.setPost()



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
# package org.allbinary.graphics.displayable.screen

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.canvas.Processor import Processor


@java_inherited_overloads
class ScreenRepaintProcessor(Processor):
    def _java_defaults(self):
        vars(self).setdefault("displayable", None)

    def _init_fields(self) -> None:
        if "displayable" not in vars(self): self.displayable: Displayable = None
    

    def __init__(self, displayable: Displayable) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Displayable import Displayable
        super().__init__()
        __class__._init_fields(self)
        self.displayable = displayable
    

    # throws Exception
    def process(self) -> None:
        from org.allbinary.graphics.displayable.screen.ScreenRepaintUtil import ScreenRepaintUtil
        ScreenRepaintUtil.repaint(self.displayable)
# from javax.microedition.lcdui.Displayable import Displayable



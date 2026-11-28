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
# package org.allbinary.midlet

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.canvas.Processor import Processor


@java_inherited_overloads
class MidletExitProcessor(Processor):
    def _java_defaults(self):
        vars(self).setdefault("midlet", None)

    def _init_fields(self) -> None:
        if "midlet" not in vars(self): self.midlet: MIDlet = None
    

    def __init__(self, midlet: MIDlet) -> None:
        __class__._java_defaults(self)
        from javax.microedition.midlet.MIDlet import MIDlet
        super().__init__()
        __class__._init_fields(self)
        self.midlet = midlet
    

    # throws Exception
    def process(self) -> None:
        pass
# from javax.microedition.midlet.MIDlet import MIDlet



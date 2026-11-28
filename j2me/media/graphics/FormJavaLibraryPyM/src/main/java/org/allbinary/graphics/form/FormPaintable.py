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
# package org.allbinary.graphics.form

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.paint.Paintable import Paintable


@java_inherited_overloads
class FormPaintable(Paintable):
    def _java_defaults(self):
        vars(self).setdefault("form", None)

    def _init_fields(self) -> None:
        if "form" not in vars(self): self.form: PaintableForm = None
    

    def __init__(self, form: PaintableForm) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.form = form
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.form.paint(graphics)
    

    def getForm(self) -> PaintableForm:
        return self.form
# from javax.microedition.lcdui.Graphics import Graphics



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

from org.allbinary.graphics.paint.Paintable import Paintable


class FormPaintable(Paintable):

    def _init_fields(self) -> None:
        self.form: PaintableForm = None
    

    def __init__(self, form: PaintableForm) -> None:
        super().__init__()
        self._init_fields()
        self.form = form
    

    def paint(self, graphics: Graphics) -> None:
        self.form.paint(graphics)
    

    def getForm(self) -> PaintableForm:
        return self.form
# from javax.microedition.lcdui.Graphics import Graphics



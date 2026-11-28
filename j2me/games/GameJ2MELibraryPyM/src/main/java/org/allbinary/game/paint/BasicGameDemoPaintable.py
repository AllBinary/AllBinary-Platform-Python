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
# package org.allbinary.game.paint

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.paint.StatePaintable import StatePaintable


@java_inherited_overloads
class BasicGameDemoPaintable(StatePaintable):
    def _java_defaults(self):
        vars(self).setdefault("mainDemoStatePaintable", None)
        vars(self).setdefault("ownershipPaintable", None)
        vars(self).setdefault("helpPaintableInterface", None)
        vars(self).setdefault("currentStatePaintable", None)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.paint.NullPaintable import NullPaintable
        if "mainDemoStatePaintable" not in vars(self): self.mainDemoStatePaintable: Paintable = None
        if "ownershipPaintable" not in vars(self): self.ownershipPaintable: Paintable = None
        if "helpPaintableInterface" not in vars(self): self.helpPaintableInterface: Paintable = None
        self.currentStatePaintable: Paintable = NullPaintable.getInstance()
    

    def __init__(self, mainDemoStatePaintable: Paintable, ownershipPaintable: Paintable, helpPaintableInterface: Paintable) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.paint.NullPaintable import NullPaintable
        from org.allbinary.graphics.paint.Paintable import Paintable
        super().__init__()
        __class__._init_fields(self)
        self.mainDemoStatePaintable = mainDemoStatePaintable
        self.setCurrentStatePaintable(NullPaintable.getInstance())
        self.ownershipPaintable = ownershipPaintable
        self.helpPaintableInterface = helpPaintableInterface
    

    def setState(self, state: int) -> None:
        if state == 0:
            self.setCurrentStatePaintable(self.getMainDemoStatePaintable())
        elif state == 1:
            self.setCurrentStatePaintable(self.helpPaintableInterface)
        else:
            self.setCurrentStatePaintable(self.ownershipPaintable)
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.getCurrentStatePaintable().paint(graphics)
    

    def getHelpPaintableInterface(self) -> Paintable:
        from org.allbinary.graphics.paint.Paintable import Paintable
        return self.helpPaintableInterface
    

    def setCurrentStatePaintable(self, currentStatePaintable: Paintable) -> None:
        from org.allbinary.graphics.paint.Paintable import Paintable
        self.currentStatePaintable = currentStatePaintable
    

    def getCurrentStatePaintable(self) -> Paintable:
        from org.allbinary.graphics.paint.Paintable import Paintable
        return self.currentStatePaintable
    

    def getMainDemoStatePaintable(self) -> Paintable:
        from org.allbinary.graphics.paint.Paintable import Paintable
        return self.mainDemoStatePaintable
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.paint.NullPaintable import NullPaintable
# from org.allbinary.graphics.paint.Paintable import Paintable



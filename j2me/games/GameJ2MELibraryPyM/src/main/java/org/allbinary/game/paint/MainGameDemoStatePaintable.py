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
from org.allbinary.graphics.paint.Paintable import Paintable


@java_inherited_overloads
class MainGameDemoStatePaintable(Paintable):
    def _java_defaults(self):
        vars(self).setdefault("ownershipPaintableInterface", None)
        vars(self).setdefault("menuPaintableInterface", None)

    def _init_fields(self) -> None:
        if "ownershipPaintableInterface" not in vars(self): self.ownershipPaintableInterface: Paintable = None
        if "menuPaintableInterface" not in vars(self): self.menuPaintableInterface: Paintable = None
    

    def __init__(self, ownershipPaintableInterface: Paintable, menuPaintableInterface: Paintable) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.ownershipPaintableInterface = ownershipPaintableInterface
        self.menuPaintableInterface = menuPaintableInterface
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.menuPaintableInterface.paint(graphics)
        self.ownershipPaintableInterface.paint(graphics)
    

    def getOwnershipPaintableInterface(self) -> Paintable:
        return self.ownershipPaintableInterface
    

    def getMenuPaintableInterface(self) -> Paintable:
        return self.menuPaintableInterface
# from javax.microedition.lcdui.Graphics import Graphics



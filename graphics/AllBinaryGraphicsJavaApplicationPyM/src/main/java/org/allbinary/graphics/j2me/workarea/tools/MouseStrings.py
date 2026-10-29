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
# package org.allbinary.graphics.j2me.workarea.tools

from __future__ import annotations



class MouseStrings:
    instance: MouseStrings = None

    def _init_fields(self) -> None:
        self.MOUSE_PRESSED: str = "mousePressed"
        self.MOUSE_RELEASED: str = "mouseReleased"
        self.MOUSE_CLICKED: str = "mouseClicked"
        self.MOUSE_DRAGGED: str = "mouseDragged"
        self.MOUSE_MOVED: str = "mouseMoved"
        self.MOUSE_PRESSED_LABEL: str = "MousePressed" + str(CommonSeps.getInstance().COLON_SEP)
        self.MOUSE_RELEASED_LABEL: str = "MouseReleased" + str(CommonSeps.getInstance().COLON_SEP)
        self.MOUSE_CLICKED_LABEL: str = "MouseClicked" + str(CommonSeps.getInstance().COLON_SEP)
        self.MOUSE_DRAGGED_LABEL: str = "MouseDragged" + str(CommonSeps.getInstance().COLON_SEP)
        self.MOUSE_MOVED_LABEL: str = "MouseMoved" + str(CommonSeps.getInstance().COLON_SEP)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> MouseStrings:
        return MouseStrings.instance
from org.allbinary.string.CommonSeps import CommonSeps


MouseStrings.instance = MouseStrings()


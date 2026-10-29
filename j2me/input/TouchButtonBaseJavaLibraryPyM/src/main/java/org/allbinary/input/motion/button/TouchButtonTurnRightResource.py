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
# package org.allbinary.input.motion.button

from __future__ import annotations

from org.allbinary.input.motion.button.TouchButtonResource import TouchButtonResource


class TouchButtonTurnRightResource(TouchButtonResource):
    instance: TouchButtonResource = None
    

    @staticmethod
    def getInstance() -> TouchButtonResource:
        return TouchButtonTurnRightResource.instance
    

    def __init__(self) -> None:
        super().__init__("/touch_button_turn_right_arrow_64_by_64.png", "/touch_button_turn_right_arrow_hint_64_by_64.png")


TouchButtonTurnRightResource.instance = TouchButtonTurnRightResource()


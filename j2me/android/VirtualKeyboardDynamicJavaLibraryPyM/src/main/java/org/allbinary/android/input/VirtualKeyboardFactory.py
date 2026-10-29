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
# package org.allbinary.android.input

from __future__ import annotations

from org.allbinary.android.input.VirtualKeyboard import VirtualKeyboard


class VirtualKeyboardFactory:
    virtualKeyboard: VirtualKeyboard = VirtualKeyboard.NULL_VIRTUAL_KEYBOARD
    

    @staticmethod
    def init(activity: Activity) -> None:
        SDK_VERSION: int = AndroidInfoFactory.getInstance().getVersion()
        if SDK_VERSION <= 2:
            VirtualKeyboardFactory.virtualKeyboard = VirtualKeyboardAPI1(activity)
        else:
            VirtualKeyboardFactory.virtualKeyboard = VirtualKeyboardAPI3(activity)
    

    @staticmethod
    def getInstance() -> VirtualKeyboard:
        return VirtualKeyboardFactory.virtualKeyboard
from org.allbinary.android.AndroidInfoFactory import AndroidInfoFactory
from org.allbinary.android.input.api1.VirtualKeyboardAPI1 import VirtualKeyboardAPI1
from org.allbinary.android.input.api3.VirtualKeyboardAPI3 import VirtualKeyboardAPI3
from android.app.Activity import Activity



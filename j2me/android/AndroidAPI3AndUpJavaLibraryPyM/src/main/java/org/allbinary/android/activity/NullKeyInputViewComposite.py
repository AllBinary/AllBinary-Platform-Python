# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.android.activity

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.android.activity.KeyInputViewCompositeInterface import KeyInputViewCompositeInterface


class NullKeyInputViewComposite(KeyInputViewCompositeInterface):
    NULL_KEY_INPUT_VIEW_COMPOSITE: NullKeyInputViewComposite = None
    

    def setKeyInputView(self, keyInputView: View) -> None:
        from android.view.View import View
        pass
    

    def getRootView(self) -> View:
        from android.view.View import View
        raise RuntimeError()
    

    def getView(self) -> View:
        from android.view.View import View
        raise RuntimeError()
    

    def runOnUiThread(self, action: object) -> None:
        pass
# from android.view.View import View


def _NullKeyInputViewComposite_NULL_KEY_INPUT_VIEW_COMPOSITE() -> object:
    return NullKeyInputViewComposite()

lazy_static(NullKeyInputViewComposite, "NULL_KEY_INPUT_VIEW_COMPOSITE", _NullKeyInputViewComposite_NULL_KEY_INPUT_VIEW_COMPOSITE)


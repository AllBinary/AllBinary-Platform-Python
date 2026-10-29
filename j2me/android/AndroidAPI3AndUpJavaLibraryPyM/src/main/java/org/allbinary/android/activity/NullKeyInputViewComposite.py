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

from org.allbinary.android.activity.KeyInputViewCompositeInterface import KeyInputViewCompositeInterface


class NullKeyInputViewComposite(KeyInputViewCompositeInterface):
    NULL_KEY_INPUT_VIEW_COMPOSITE: NullKeyInputViewComposite = None
    

    def setKeyInputView(self, keyInputView: View) -> None:
        pass
    

    def getRootView(self) -> View:
        raise RuntimeError()
    

    def getView(self) -> View:
        raise RuntimeError()
    

    def runOnUiThread(self, action: object) -> None:
        pass
from android.view.View import View


NullKeyInputViewComposite.NULL_KEY_INPUT_VIEW_COMPOSITE = NullKeyInputViewComposite()


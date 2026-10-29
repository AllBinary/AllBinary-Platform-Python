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
# package org.allbinary.android.activity

from __future__ import annotations



# Java interface
class SimpleProgressActivityInterface:
    

    def runOnUiThread(self, action: object) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def onSetProgress(self, value: int, text: str) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def onDismissProgress(self, animationSequence: list[int]) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def onShowProgress(self, indeterminate: bool, animationSequence: list[int]) -> None:
        raise NotImplementedError()



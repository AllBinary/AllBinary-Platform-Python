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

from org.allbinary.android.activity.ProgressActivityInterface import ProgressActivityInterface


class NullProgressActivity(ProgressActivityInterface):
    NULL_PROGRESS_ACTIVITY: NullProgressActivity = None
    

    def runOnUiThread(self, action: object) -> None:
        pass
    

    def onDismissTitleProgressBar(self) -> None:
        pass
    

    def onShowTitleProgressBar(self, value: int, indeterminate: bool) -> None:
        pass
    

    def onTitleProgressBarSetProgress(self, value: int) -> None:
        pass


NullProgressActivity.NULL_PROGRESS_ACTIVITY = NullProgressActivity()


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
# package org.allbinary.android.view

from __future__ import annotations

from org.allbinary.android.view.BaseViewWrapper import BaseViewWrapper


class ViewWrapper(BaseViewWrapper):

    def _init_fields(self) -> None:
        self.view: View = None
    

    def __init__(self, view: View) -> None:
        super().__init__()
        self._init_fields()
        self.view = view
    

    def invalidate(self) -> None:
        self.view.invalidate()
    

    def postInvalidate(self) -> None:
        self.view.postInvalidate()
from android.view.View import View



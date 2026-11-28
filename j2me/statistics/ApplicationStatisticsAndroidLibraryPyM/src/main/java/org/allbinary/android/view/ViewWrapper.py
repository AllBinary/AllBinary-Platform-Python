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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.android.view.BaseViewWrapper import BaseViewWrapper


@java_inherited_overloads
class ViewWrapper(BaseViewWrapper):
    def _java_defaults(self):
        vars(self).setdefault("view", None)

    def _init_fields(self) -> None:
        if "view" not in vars(self): self.view: View = None
    

    def __init__(self, view: View) -> None:
        __class__._java_defaults(self)
        from android.view.View import View
        super().__init__()
        __class__._init_fields(self)
        self.view = view
    

    def invalidate(self) -> None:
        self.view.invalidate()
    

    def postInvalidate(self) -> None:
        self.view.postInvalidate()
# from android.view.View import View



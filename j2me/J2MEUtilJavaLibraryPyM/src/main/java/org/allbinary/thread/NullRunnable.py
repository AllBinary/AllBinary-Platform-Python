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
# package org.allbinary.thread

from __future__ import annotations

from org.allbinary.thread.ARunnable import ARunnable


class NullRunnable(ARunnable):
    instance: NullRunnable = None
    

    @staticmethod
    def getInstance() -> NullRunnable:
        return NullRunnable.instance
    

    def __init__(self) -> None:
        super().__init__()
from jsinterop.annotations.JsType import JsType
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsConstructor import JsConstructor


NullRunnable.instance = NullRunnable()


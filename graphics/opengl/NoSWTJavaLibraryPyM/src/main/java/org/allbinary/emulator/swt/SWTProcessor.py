# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.emulator.swt

from __future__ import annotations

import time


class SWTProcessor:
    instance: SWTProcessor = None

    def _init_fields(self) -> None:
        self.runnable: object = NullRunnable.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> SWTProcessor:
        return SWTProcessor.instance
    

    def process(self, display: Display) -> None:
        display.sleep()
from org.eclipse.swt.widgets.Display import Display
from org.allbinary.thread.NullRunnable import NullRunnable


SWTProcessor.instance = SWTProcessor()


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

from org.allbinary.emulator.swt.SWTProcessor import SWTProcessor


class SWTRunnableProcessor(SWTProcessor):
    instanceR: SWTRunnableProcessor = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> SWTRunnableProcessor:
        return SWTRunnableProcessor.instanceR
    

    def process(self, display: Display) -> None:
        pass
from org.eclipse.swt.widgets.Display import Display


SWTRunnableProcessor.instanceR = SWTRunnableProcessor()


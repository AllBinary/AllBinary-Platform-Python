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
# package org.allbinary.game.input

from __future__ import annotations



class InputProcessorFactory:
    instance: InputProcessorFactory = None

    def _init_fields(self) -> None:
        self.inputProcessor: InputProcessor = InputProcessor()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> InputProcessorFactory:
        return InputProcessorFactory.instance
    

    def getInputProcessor(self) -> InputProcessor:
        return self.inputProcessor
from org.allbinary.game.input.InputProcessor import InputProcessor


InputProcessorFactory.instance = InputProcessorFactory()


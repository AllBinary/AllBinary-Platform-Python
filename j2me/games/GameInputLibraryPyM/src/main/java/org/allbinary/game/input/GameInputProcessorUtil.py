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



class GameInputProcessorUtil:
    

    @staticmethod
    def init(inputProcessorArray: list[GameInputProcessor]) -> None:
        from org.allbinary.game.input.GameInputProcessor import GameInputProcessor
        from org.allbinary.game.input.InputFactory import InputFactory
        noInputProcessor: GameInputProcessor = GameInputProcessor.getInstance()
        total: int = InputFactory.getInstance().MAX
        for index in range(0, total):
            inputProcessorCanBeNull: GameInputProcessor = inputProcessorArray[index]
            if inputProcessorCanBeNull is None:
                inputProcessorArray[index] = noInputProcessor



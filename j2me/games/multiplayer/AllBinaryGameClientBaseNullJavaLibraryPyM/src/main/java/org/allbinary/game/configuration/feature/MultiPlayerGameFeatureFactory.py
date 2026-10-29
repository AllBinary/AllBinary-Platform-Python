# Generated Code Do Not Modify
# package org.allbinary.game.configuration.feature

from __future__ import annotations



class MultiPlayerGameFeatureFactory:
    instance: MultiPlayerGameFeatureFactory = None
    

    @staticmethod
    def getInstance() -> MultiPlayerGameFeatureFactory:
        return MultiPlayerGameFeatureFactory.instance
    

    def __init__(self) -> None:
        pass
    

    def addCommands(self, anyType: object) -> None:
        gameCommandsFactory: GameCommandsFactory = GameCommandsFactory.getInstance()
        canvas: Canvas = anyType
        canvas.addCommand(gameCommandsFactory.QUIT_COMMAND)
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory


MultiPlayerGameFeatureFactory.instance = MultiPlayerGameFeatureFactory()


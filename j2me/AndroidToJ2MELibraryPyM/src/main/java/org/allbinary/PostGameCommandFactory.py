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
# package org.allbinary

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class PostGameCommandFactory:
    instance: PostGameCommandFactory = None
    

    @staticmethod
    def getInstance() -> PostGameCommandFactory:
        return PostGameCommandFactory.instance
    

    def addCommands(self, canvas: MyCanvas) -> None:
        from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
        from org.allbinary.game.configuration.feature.MultiPlayerGameFeatureFactory import MultiPlayerGameFeatureFactory
        from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
        from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
        from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
        operatingSystemInterface: GenericOperatingSystem = OperatingSystemFactory.getInstance().getOperatingSystemInstance()
        gameCommandsFactory: GameCommandsFactory = GameCommandsFactory.getInstance()
        if not operatingSystemInterface.isOverScan():
            canvas.addCommand(gameCommandsFactory.TOGGLE_KEYBOARD)
        MultiPlayerGameFeatureFactory.getInstance().addCommands(canvas)
# from org.allbinary.game.commands.GameCommandsFactory import GameCommandsFactory
# from org.allbinary.game.configuration.feature.MultiPlayerGameFeatureFactory import MultiPlayerGameFeatureFactory
# from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
# from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
# from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory


def _PostGameCommandFactory_instance() -> object:
    return PostGameCommandFactory()

lazy_static(PostGameCommandFactory, "instance", _PostGameCommandFactory_instance)


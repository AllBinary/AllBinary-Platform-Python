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
# package org.allbinary.game.init

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.game.init.BaseGameInitialization import BaseGameInitialization


@java_inherited_overloads
class CommonGameInitialization(BaseGameInitialization):
    def _java_defaults(self):
        vars(self).setdefault("commonStrings", None)

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self, resourceInitializationArray: list[ResourceInitialization], portion: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.resource.ResourceInitialization import ResourceInitialization
        super().__init__(resourceInitializationArray, portion)
        __class__._init_fields(self)
    

    # throws Exception
    def init(self, abeClientInformation: AbeClientInformationInterface, commandListener: CommandListener, level: int) -> None:
        from javax.microedition.lcdui.CommandListener import CommandListener
        from org.allbinary.game.resource.ResourceLoadingLevelFactory import ResourceLoadingLevelFactory
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
        from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
        from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
        from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
        from org.allbinary.math.AngleFactory import AngleFactory
        java_super_call(super(), "init", abeClientInformation, commandListener, level)
        resourceLoadingLevelFactory: ResourceLoadingLevelFactory = ResourceLoadingLevelFactory.getInstance()
        if not (java_predicate(self, "isGameInitialized")) and level == resourceLoadingLevelFactory.LOAD_ALL.getLevel():
            self.setGameInitialized(True)
            progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
            SmallIntegerSingletonFactory.getInstance().init()
            progressCanvas.addNormalPortion(50, "Integers")
            PointFactory.getInstance().init()
            progressCanvas.addNormalPortion(50, "Points")
            AngleFactory.getInstance()
            progressCanvas.addNormalPortion(50, "Angles")
            self.initGame()
            self.resourceInitializationArray[self.GAME_RESOURCES].init()
        java_super_call(super(), "resourceInitialization", level)
    

    # throws Exception
    def initGame(self) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
# from javax.microedition.lcdui.CommandListener import CommandListener
# from org.allbinary.game.resource.ResourceInitialization import ResourceInitialization
# from org.allbinary.game.resource.ResourceLoadingLevelFactory import ResourceLoadingLevelFactory
# from org.allbinary.graphics.PointFactory import PointFactory
# from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
# from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
# from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.math.AngleFactory import AngleFactory
# from org.allbinary.string.CommonStrings import CommonStrings



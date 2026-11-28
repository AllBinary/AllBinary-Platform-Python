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
# package org.allbinary.game.ag.ai

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.game.ag.ai.KeyPressesAI import KeyPressesAI


@java_inherited_overloads
class MultiKeyPressesAI(KeyPressesAI):
    def _java_defaults(self):
        vars(self).setdefault("toggleTimeHelper", None)
        vars(self).setdefault("gameTickTimeDelayHelper", None)

    def _init_fields(self) -> None:
        from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        self.toggleTimeHelper: TimeDelayHelper = TimeDelayHelper(600)
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
    

    def __init__(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.input.GameInput import GameInput
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.util.ABHashtable import ABHashtable
        super().__init__(hashtable, ownerLayerInterface, gameInput)
        __class__._init_fields(self)
        self.update()
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        pass
    

    # throws Exception
    def update(self) -> None:
        from org.allbinary.game.input.GameInput import GameInput
        gameInput: GameInput = self.getGameInput()
        keys: list[int] = self.keys
        size: int = len(keys)
        if java_predicate(self, "isOn"):
            for index in range(0, size):
                key: int = int(keys[index])
                if key != -1:
                    gameInput.add(self.gameKeyEventFactory.getInstanceForKey(self, key))
        else:
            for index in range(0, size):
                key: int = int(keys[index])
                if key != -1:
                    gameInput.addForRemoval(self.gameKeyEventFactory.getInstanceForKey(self, key))
    

    # throws Exception
    def toggle(self) -> None:
        if self.toggleTimeHelper.isTime(self.gameTickTimeDelayHelper.startTime):
            java_super_call(super(), "toggle")
            self.update()
    

    # throws Exception
    def disable(self) -> None:
        if self.toggleTimeHelper.isTime(self.gameTickTimeDelayHelper.startTime):
            java_super_call(super(), "disable")
            self.update()
    

    # throws Exception
    def enable(self) -> None:
        if self.toggleTimeHelper.isTime(self.gameTickTimeDelayHelper.startTime):
            java_super_call(super(), "enable")
            self.update()
# from org.allbinary.game.input.GameInput import GameInput
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
# from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
# from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
# from org.allbinary.util.ABHashtable import ABHashtable



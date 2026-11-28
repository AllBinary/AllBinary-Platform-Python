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
# package org.allbinary.game.layer

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.input.PlayerGameInputCompositeInterface import PlayerGameInputCompositeInterface
from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer


@java_inherited_overloads
class PlayerGameInputGameLayer(*java_bases(AllBinaryGameLayer, PlayerGameInputCompositeInterface)):
    def _java_defaults(self):
        vars(self).setdefault("playerGameInput", None)

    def _init_fields(self) -> None:
        if "playerGameInput" not in vars(self): self.playerGameInput: PlayerGameInput = None
    

    def __init__(self, playerInputId: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.input.PlayerGameInput import PlayerGameInput
        from org.allbinary.graphics.PointFactory import PointFactory
        from org.allbinary.graphics.Rectangle import Rectangle
        from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.view.StaticViewPosition import StaticViewPosition
        super().__init__(StringUtil.getInstance().EMPTY_STRING, Rectangle(PointFactory.getInstance().ZERO_ZERO, 0, 0), StaticViewPosition(0, 0, 0))
        __class__._init_fields(self)
        self.playerGameInput = PlayerGameInput(self.getGameKeyEventList(), BasicArrayListD(), playerInputId)
        canvasStrings: CanvasStrings = CanvasStrings.getInstance()
        self.logUtil.putF("Danger Danger Danger: Should Not Be Called Except For Testing Input", self, canvasStrings.PAINT)
    

    def getPlayerGameInput(self) -> PlayerGameInput:
        from org.allbinary.game.input.PlayerGameInput import PlayerGameInput
        return self.playerGameInput
    

    def initInputProcessors(self) -> None:
        pass
    

    # throws Exception
    def processInput(self, myManager: AllBinaryLayerManager) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        pass
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.game.input.PlayerGameInput import PlayerGameInput
# from org.allbinary.graphics.PointFactory import PointFactory
# from org.allbinary.graphics.Rectangle import Rectangle
# from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.view.StaticViewPosition import StaticViewPosition



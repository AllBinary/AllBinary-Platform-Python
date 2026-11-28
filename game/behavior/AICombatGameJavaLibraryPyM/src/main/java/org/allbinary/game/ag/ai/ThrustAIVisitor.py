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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.util.visitor.Visitor import Visitor


@java_inherited_overloads
class ThrustAIVisitor(Visitor):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("TRUE", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.TRUE: bool = BooleanFactory.getInstance().TRUE
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def visit(self, anyType: object) -> object:
        from javax.microedition.lcdui.Canvas import Canvas
        from org.allbinary.game.ai.BasicAI import BasicAI
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            basicAI: BasicAI = anyType
            basicAI.processKeyAI(Canvas.UP)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.VISIT, e)
        return self.TRUE
# from javax.microedition.lcdui.Canvas import Canvas
# from org.allbinary.game.ai.BasicAI import BasicAI
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
# from org.allbinary.string.CommonStrings import CommonStrings



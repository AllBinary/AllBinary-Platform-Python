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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class DemoLimitedCommandTextItemArrayFactory:
    instance: DemoLimitedCommandTextItemArrayFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.graphics.form.item.CommandTextItemArrayFactory import CommandTextItemArrayFactory
        from org.allbinary.graphics.form.item.LimitCommandsVisitor import LimitCommandsVisitor
        self.commandTextItemArrayFactory: CommandTextItemArrayFactory = CommandTextItemArrayFactory(LimitCommandsVisitor())

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> DemoLimitedCommandTextItemArrayFactory:
        return DemoLimitedCommandTextItemArrayFactory.instance
    

    def getCommandTextItemArrayFactory(self) -> CommandTextItemArrayFactory:
        from org.allbinary.graphics.form.item.CommandTextItemArrayFactory import CommandTextItemArrayFactory
        return self.commandTextItemArrayFactory
# from org.allbinary.graphics.form.item.CommandTextItemArrayFactory import CommandTextItemArrayFactory
# from org.allbinary.graphics.form.item.LimitCommandsVisitor import LimitCommandsVisitor


def _DemoLimitedCommandTextItemArrayFactory_instance() -> object:
    return DemoLimitedCommandTextItemArrayFactory()

lazy_static(DemoLimitedCommandTextItemArrayFactory, "instance", _DemoLimitedCommandTextItemArrayFactory_instance)


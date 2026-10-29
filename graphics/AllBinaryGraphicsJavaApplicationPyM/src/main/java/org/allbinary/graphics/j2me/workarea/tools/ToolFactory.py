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
# package org.allbinary.graphics.j2me.workarea.tools

from __future__ import annotations



class ToolFactory:
    instance: ToolFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.selectedTool: GraphicsItemInterfaceFactoryInterface = None
        self.tool: str = None
        self.SELECTED_LABEL: str = "Selected: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ToolFactory:
        return ToolFactory.instance
    

    def setSelectedTool(self, tool: str) -> None:
        try:
            StatusFactory.getInstance().setStatus(self.SELECTED_LABEL + tool)
            self.tool = tool
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "setSelectionTool", e)
    

    def getSelectedToolFactory(self) -> GraphicsItemInterfaceFactoryInterface:
        from org.allbinary.graphics.j2me.workarea.tools.GraphicItemFactory import GraphicItemFactory
        StatusFactory.getInstance().setStatus("Tool In Use: " + self.tool)
        if self.tool is not None:
            self.selectedTool = GraphicItemFactory.getInstance().getInstance(self.tool)
            self.logUtil.putF("New Tool: " + str(self.selectedTool), self, "getSelectedToolFactory")
            return self.selectedTool
        else:
            return None
from org.allbinary.graphics.j2me.StatusFactory import StatusFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


ToolFactory.instance = ToolFactory()


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
# package org.allbinary.logic.control.workflow

from __future__ import annotations



class WorkFlowData:
    instance: WorkFlowData = None

    def _init_fields(self) -> None:
        self.WORKFLOWS: str = "WORKFLOWS"
        self.WORKFLOW: str = "WORKFLOW"
        self.NAME: str = "WORKFLOW_NAME"
        self.DATA: str = "WORKFLOW_DATA"
    

    @staticmethod
    def getInstance() -> WorkFlowData:
        return WorkFlowData.instance
    

    def __init__(self) -> None:
        self._init_fields()


WorkFlowData.instance = WorkFlowData()


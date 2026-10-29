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
# package org.allbinary.string

from __future__ import annotations



class CommonLabels:
    instance: CommonLabels = None

    def _init_fields(self) -> None:
        self.WIDTH_LABEL: str = " Width: "
        self.HEIGHT_LABEL: str = " Height: "
        self.END_LABEL: str = "End: "
        self.TOTAL_LABEL: str = "Total: "
        self.INDEX_LABEL: str = "index: "
        self.START_LABEL: str = "Start: "
        self.COMMAND_LABEL: str = "Command: "
        self.NAME_LABEL: str = "Name: "
        self.START: str = self.START_LABEL
        self.ELAPSED: str = " Elapsed: "
        self.CURRENT: str = " Current: "
        self.NEXT: str = "Next"
        self.ITEM_LABEL: str = "Item: "
        self.RESULT_: str = "Result: "
        self.COLON_SEP: str = ": "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CommonLabels:
        return CommonLabels.instance
from jsinterop.annotations.JsType import JsType
from jsinterop.annotations.JsMethod import JsMethod
from jsinterop.annotations.JsProperty import JsProperty


CommonLabels.instance = CommonLabels()


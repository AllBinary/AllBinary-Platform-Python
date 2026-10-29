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



class CommonStateStrings:
    instance: CommonStateStrings = None

    def _init_fields(self) -> None:
        self.CONTEXT: str = "Context: "
        self.FINISH: str = "finish"
        self.CREATE: str = "onCreate"
        self.START: str = "onStart"
        self.RESTART: str = "onRestart"
        self.RESUME: str = "onResume"
        self.PAUSE: str = "onPause"
        self.STOP: str = "onStop"
        self.DESTROY: str = "onDestroy"
        self.BIND: str = "onBind"
        self.ON_SAVE_INSTANCE_STATE: str = "onSaveInstanceState"
        self.ON_START_COMMAND: str = "onStartCommand"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CommonStateStrings:
        return CommonStateStrings.instance


CommonStateStrings.instance = CommonStateStrings()


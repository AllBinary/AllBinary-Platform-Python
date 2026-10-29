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
# package org.allbinary.android.input.motion

from __future__ import annotations



class AnalogControllerConfigurationFactory:
    instance: AnalogControllerConfigurationFactory = None

    def _init_fields(self) -> None:
        self.SCALE_FACTOR: int = ScaleFactorFactory.getInstance().DEFAULT_SCALE_FACTOR
        self.SCALE_VALUE: int = ScaleFactorFactory.getInstance().DEFAULT_SCALE_VALUE
        self.available: bool = False
        self.analogControllerConfigurationEvent: AnalogControllerConfigurationEvent = AnalogControllerConfigurationEvent(self)
    

    @staticmethod
    def getInstance() -> AnalogControllerConfigurationFactory:
        return AnalogControllerConfigurationFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def isAvailable(self) -> bool:
        return self.available
    

    # throws Exception
    def setAvailable(self, available: bool) -> None:
        self.available = available
        AnalogControllerConfigurationEventHandler.getInstance().fireEvent(self.analogControllerConfigurationEvent)
from org.allbinary.android.input.motion.event.AnalogControllerConfigurationEvent import AnalogControllerConfigurationEvent
from org.allbinary.android.input.motion.event.AnalogControllerConfigurationEventHandler import AnalogControllerConfigurationEventHandler
from org.allbinary.logic.math.ScaleFactorFactory import ScaleFactorFactory


AnalogControllerConfigurationFactory.instance = AnalogControllerConfigurationFactory()


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



#extends ValidationComponentInterface, ValidationInterface, ComponentInterface, DomNodeInterface, DataMappingInterface
# Java interface
class WorkFlowInterface:
    

    # throws Exception
    def getName(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def process(self) -> int:
        raise NotImplementedError()



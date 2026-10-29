# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.business.advertisement

from __future__ import annotations



# Java interface
class GameAdStateFactoryInterface:
    

    # throws Exception
    def getInstanceForApp(self, softwareInformation: SoftwareInformation) -> GameAdStateBase:
        raise NotImplementedError()
from org.allbinary.logic.system.SoftwareInformation import SoftwareInformation



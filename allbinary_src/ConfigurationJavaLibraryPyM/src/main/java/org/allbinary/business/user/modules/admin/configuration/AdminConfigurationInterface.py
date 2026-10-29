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
# package org.allbinary.business.user.modules.admin.configuration

from __future__ import annotations



# Java interface
class AdminConfigurationInterface:
    

    # throws Exception
    def write(self) -> None:
        raise NotImplementedError()
    

    def getContextConfigurationInterface(self) -> ContextConfigurationInterface:
        raise NotImplementedError()
    

    def setContextConfigurationInterface(self, contextConfigurationInterface: ContextConfigurationInterface) -> None:
        raise NotImplementedError()
from org.allbinary.business.context.configuration.ContextConfigurationInterface import ContextConfigurationInterface



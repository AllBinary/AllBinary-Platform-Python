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
# package org.allbinary.business.context.configuration

from __future__ import annotations



# Java interface
class ContextConfigurationInterface:
    

    def getEmailServerConfigurationInterface(self) -> EmailServerConfigurationInterface:
        raise NotImplementedError()
    

    def setEmailServerConfigurationInterface(self, emailServerConfigurationInterface: EmailServerConfigurationInterface) -> None:
        raise NotImplementedError()
from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationInterface import EmailServerConfigurationInterface



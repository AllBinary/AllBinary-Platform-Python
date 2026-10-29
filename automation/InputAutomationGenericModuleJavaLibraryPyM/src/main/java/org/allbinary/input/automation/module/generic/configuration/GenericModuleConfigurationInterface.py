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
# package org.allbinary.input.automation.module.generic.configuration

from __future__ import annotations



# Java interface
class GenericModuleConfigurationInterface:
    

    def getSelectedGenericProfile(self) -> GenericProfile:
        raise NotImplementedError()
    

    def setSelectedGenericProfile(self, selectedGenericProfile: GenericProfile) -> None:
        raise NotImplementedError()
from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfile import GenericProfile



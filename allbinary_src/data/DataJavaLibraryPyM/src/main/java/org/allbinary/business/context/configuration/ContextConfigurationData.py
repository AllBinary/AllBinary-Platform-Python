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

from java.lang.JavaRuntimeStatic import lazy_static


class ContextConfigurationData:
    instance: ContextConfigurationData = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.io.file.CommonDataFileStrings import CommonDataFileStrings
        self.NAME: str = "CONTEXT_CONFIGURATION_NAME"
        self.UNCRYPTED_EXTENSION: str = CommonDataFileStrings.getInstance().UNCRYPTED_EXTENSION
        self.ENCRYPTED_EXTENSION: str = CommonDataFileStrings.getInstance().ENCRYPTED_EXTENSION
    

    @staticmethod
    def getInstance() -> ContextConfigurationData:
        return ContextConfigurationData.instance
    

    def __init__(self) -> None:
        self._init_fields()
# from org.allbinary.logic.io.file.CommonDataFileStrings import CommonDataFileStrings


def _ContextConfigurationData_instance() -> object:
    return ContextConfigurationData()

lazy_static(ContextConfigurationData, "instance", _ContextConfigurationData_instance)


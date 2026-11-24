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
# package org.allbinary.business.user.modules.configuration

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class UserConfigurationData:
    NAME: str = "USER_CONFIGURATION_NAME"
    UNCRYPTED_EXTENSION: str = None
    ENCRYPTED_EXTENSION: str = None
    

    def __init__(self) -> None:
        pass
# from org.allbinary.logic.io.file.CommonDataFileStrings import CommonDataFileStrings


def _UserConfigurationData_UNCRYPTED_EXTENSION() -> object:
    from org.allbinary.logic.io.file.CommonDataFileStrings import CommonDataFileStrings
    return CommonDataFileStrings.getInstance().UNCRYPTED_EXTENSION

lazy_static(UserConfigurationData, "UNCRYPTED_EXTENSION", _UserConfigurationData_UNCRYPTED_EXTENSION)

def _UserConfigurationData_ENCRYPTED_EXTENSION() -> object:
    from org.allbinary.logic.io.file.CommonDataFileStrings import CommonDataFileStrings
    return CommonDataFileStrings.getInstance().ENCRYPTED_EXTENSION

lazy_static(UserConfigurationData, "ENCRYPTED_EXTENSION", _UserConfigurationData_ENCRYPTED_EXTENSION)


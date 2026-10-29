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
# package org.allbinary.input.automation.module.generic

from __future__ import annotations



class GenericConfigData:
    RELATIVE_PATH: str = "./"
    CONFIG_PATH: str = "modules/configs/"
    MODULE_RELATIVE_PATH: str = None
    GAME_MODULE_RELATIVE_PATH: str = None
    MMO_GAME_MODULE_RELATIVE_PATH: str = None
    FREE_MMO_GAME_MODULE_RELATIVE_PATH: str = "free/"
    

    def __init__(self) -> None:
        pass


GenericConfigData.MODULE_RELATIVE_PATH = str(GenericConfigData.RELATIVE_PATH + GenericConfigData.CONFIG_PATH) + "allbinary/input/automation/module/"

GenericConfigData.GAME_MODULE_RELATIVE_PATH = str(GenericConfigData.MODULE_RELATIVE_PATH) + "game/"

GenericConfigData.MMO_GAME_MODULE_RELATIVE_PATH = str(GenericConfigData.GAME_MODULE_RELATIVE_PATH) + "mmog/"


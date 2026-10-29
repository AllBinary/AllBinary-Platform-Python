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
# package tags

from __future__ import annotations



class TagStrings:
    instance: TagStrings = None

    def _init_fields(self) -> None:
        self.DO_START_TAG: str = "doStartTag"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> TagStrings:
        return TagStrings.instance


TagStrings.instance = TagStrings()


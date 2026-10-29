# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations



class CaptionResources:
    instance: CaptionResources = None

    def _init_fields(self) -> None:
        self.RESOURCE: str = "/unit_message_bubbled_box.png"
    

    @staticmethod
    def getInstance() -> CaptionResources:
        return CaptionResources.instance
    

    def __init__(self) -> None:
        self._init_fields()


CaptionResources.instance = CaptionResources()


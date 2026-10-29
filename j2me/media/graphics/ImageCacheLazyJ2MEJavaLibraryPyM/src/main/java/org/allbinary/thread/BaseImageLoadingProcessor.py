# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.thread

from __future__ import annotations



class BaseImageLoadingProcessor:
    instance: BaseImageLoadingProcessor = None
    

    @staticmethod
    def getInstance() -> BaseImageLoadingProcessor:
        return BaseImageLoadingProcessor.instance
    

    def runTask(self) -> None:
        pass


BaseImageLoadingProcessor.instance = BaseImageLoadingProcessor()


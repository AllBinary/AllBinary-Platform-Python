# 
# AllBinary Open License Version 1 
# Copyright (c) 2007 AllBinary 
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
# package org.allbinary.logic.util.cache

from __future__ import annotations



class AutomaticCacheInterfaceFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(cacheableInterfaceFactoryInterface: CacheableInterfaceFactoryInterface, cacheType: CacheType, cachePolicy: CachePolicy) -> AutomaticCacheInterface:
        raise Exception("No such " + str(cacheType))



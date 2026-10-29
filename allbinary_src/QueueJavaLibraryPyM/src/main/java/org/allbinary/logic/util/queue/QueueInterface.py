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
# package org.allbinary.logic.util.queue

from __future__ import annotations



# Java interface
class QueueInterface:
    

    # throws Exception
    def offer(self, anyType: object) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def remove(self, anyType: object) -> None:
        raise NotImplementedError()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def remove(self) -> object:
        raise NotImplementedError()



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
# package org.allbinary.thread

from __future__ import annotations

from org.allbinary.thread.PriorityRunnable import PriorityRunnable


class NullPriorityRunnable(PriorityRunnable):
    

    def getPriority(self) -> int:
        return 0
    

    def isDone(self) -> bool:
        return True
    

    def reset(self) -> None:
        pass
    

    def run(self) -> None:
        pass



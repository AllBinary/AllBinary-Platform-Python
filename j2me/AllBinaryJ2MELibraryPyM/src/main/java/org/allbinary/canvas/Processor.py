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
# package org.allbinary.canvas

from __future__ import annotations



class Processor:
    SINGLETON: Processor = None
    

    @staticmethod
    def getInstance() -> Processor:
        return Processor.SINGLETON
    

    # throws Exception
    def process(self) -> None:
        pass
    

    # throws Exception
    def processt(self, timeDelta: int) -> None:
        pass


Processor.SINGLETON = Processor()


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



class ThreadPoolStrings:
    instance: ThreadPoolStrings = None

    def _init_fields(self) -> None:
        self.ADD_TASK: str = "addTask"
        self.START_TASK: str = "Started Task: "
        self.COMPLETE_TASK: str = "Completed Task: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ThreadPoolStrings:
        return ThreadPoolStrings.instance


ThreadPoolStrings.instance = ThreadPoolStrings()


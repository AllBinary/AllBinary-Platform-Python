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
# package org.allbinary.game.configuration.persistance

from __future__ import annotations

# from javax.microedition.rms.RecordFilter import RecordFilter


class NullRecordFilter(RecordFilter):
    NULL_RECORD_FILTER: NullRecordFilter = None
    

    def matches(self, candidate: list[int]) -> bool:
        return True


NullRecordFilter.NULL_RECORD_FILTER = NullRecordFilter()


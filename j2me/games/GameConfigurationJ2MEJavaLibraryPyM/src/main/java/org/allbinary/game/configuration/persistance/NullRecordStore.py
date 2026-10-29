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

# from javax.microedition.rms.RecordStore import RecordStore


class NullRecordStore(RecordStore):
    NULL_RECORD_STORE: NullRecordStore = None

    def __init__(self) -> None:
        super().__init__()


NullRecordStore.NULL_RECORD_STORE = NullRecordStore()


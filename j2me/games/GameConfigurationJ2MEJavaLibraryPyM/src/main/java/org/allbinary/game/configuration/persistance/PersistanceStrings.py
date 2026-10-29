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



class PersistanceStrings:
    instance: PersistanceStrings = None

    def _init_fields(self) -> None:
        self.SAVING: str = "Saving: "
        self.NUMBER_OF_RECORDS: str = "Number of records: "
        self.LOADING_ID: str = "Loading data with id: "
        self.LOAD_ALL: str = "loadAll"
        self.DELETING_WITH_ID: str = "Deleting data with id: "
        self.CLOSING_RECORDSTORE: str = "Closing RecordStore"
        self.NOT_SAVING: str = "Not Saving: "
        self.ERROR_LOADING: str = "Error Loading gameActionInput: "
        self.ERROR_LOADING_ID: str = "Error Loading id: "
        self.ID: str = " id: "
        self.GAME_ACTION_INPUT: str = " GameActionInput: "

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PersistanceStrings:
        return PersistanceStrings.instance


PersistanceStrings.instance = PersistanceStrings()


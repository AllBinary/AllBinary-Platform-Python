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
# package org.allbinary.game.score.remote

from __future__ import annotations



class RemoteHighScoresData:
    SINGLETON: RemoteHighScoresData = None

    def _init_fields(self) -> None:
        self.HIGH_SCORES: str = "HIGH_SCORES"
        self.CUSTOMER_USER_NAME: str = "CUSTOMER_USER_NAME"
        self.DISPLAY_NAME: str = "DISPLAY_NAME"
        self.SCORE: str = "SCORE"
        self.GAME_INFO: str = "GAME_INFO"
        self.GAME_CONFIGURATION: str = "GAME_CONFIGURATION"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> RemoteHighScoresData:
        return RemoteHighScoresData.SINGLETON


RemoteHighScoresData.SINGLETON = RemoteHighScoresData()


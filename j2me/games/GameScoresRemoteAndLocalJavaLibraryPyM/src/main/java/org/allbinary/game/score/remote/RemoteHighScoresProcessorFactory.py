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

from java.lang.JavaRuntimeStatic import lazy_static


class RemoteHighScoresProcessorFactory:
    SINGLETON: RemoteHighScoresProcessorInterface = None
    

    @staticmethod
    def getInstance() -> RemoteHighScoresProcessorInterface:
        return RemoteHighScoresProcessorFactory.SINGLETON


def _RemoteHighScoresProcessorFactory_SINGLETON() -> object:
    from org.allbinary.game.score.remote.RemoteHighScoresProcessor import RemoteHighScoresProcessor
    return RemoteHighScoresProcessor()

lazy_static(RemoteHighScoresProcessorFactory, "SINGLETON", _RemoteHighScoresProcessorFactory_SINGLETON)


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


class RemoteHighScoresSubmissionProcessorFactory:
    SINGLETON: RemoteHighScoresSubmissionProcessorInterface = None
    

    @staticmethod
    def getInstance() -> RemoteHighScoresSubmissionProcessorInterface:
        return RemoteHighScoresSubmissionProcessorFactory.SINGLETON


def _RemoteHighScoresSubmissionProcessorFactory_SINGLETON() -> object:
    from org.allbinary.game.score.remote.RemoteHighScoresSubmissionProcessor import RemoteHighScoresSubmissionProcessor
    return RemoteHighScoresSubmissionProcessor()

lazy_static(RemoteHighScoresSubmissionProcessorFactory, "SINGLETON", _RemoteHighScoresSubmissionProcessorFactory_SINGLETON)


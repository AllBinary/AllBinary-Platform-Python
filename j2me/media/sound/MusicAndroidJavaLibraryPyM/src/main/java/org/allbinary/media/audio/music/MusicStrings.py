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
# package org.allbinary.media.audio.music

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class MusicStrings:
    instance: MusicStrings = None

    def _init_fields(self) -> None:
        self.SONG_EXTRA: str = "SONG"
        self.LEFT_VOLUME: str = "LEFT_VOLUME"
        self.RIGHT_VOLUME: str = "RIGHT_VOLUME"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> MusicStrings:
        return MusicStrings.instance


def _MusicStrings_instance() -> object:
    return MusicStrings()

lazy_static(MusicStrings, "instance", _MusicStrings_instance)


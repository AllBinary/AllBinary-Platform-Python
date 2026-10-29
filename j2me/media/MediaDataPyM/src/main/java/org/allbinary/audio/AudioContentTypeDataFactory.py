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
# package org.allbinary.audio

from __future__ import annotations



class AudioContentTypeDataFactory:
    instance: AudioContentTypeDataFactory = None

    def _init_fields(self) -> None:
        self.MIME_AUDIO_TONE: AudioContentTypeData = AudioContentTypeData("audio/x-tone-seq")
        self.MIME_AUDIO_AMR: AudioContentTypeData = AudioContentTypeData("audio/amr")
        self.MIME_AUDIO_AMR_WB: AudioContentTypeData = AudioContentTypeData("audio/amr-wb")
        self.MIME_AUDIO_WAV: AudioContentTypeData = AudioContentTypeData("audio/x-wav")
        self.MIME_AUDIO_MIDI: AudioContentTypeData = AudioContentTypeData("audio/midi")
        self.MIME_AUDIO_SP_MIDI: AudioContentTypeData = AudioContentTypeData("audio/sp-midi")
    

    @staticmethod
    def getInstance() -> AudioContentTypeDataFactory:
        return AudioContentTypeDataFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
from org.allbinary.audio.AudioContentTypeData import AudioContentTypeData


AudioContentTypeDataFactory.instance = AudioContentTypeDataFactory()

